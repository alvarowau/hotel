from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QHeaderView, QWidget

from dao.clientes_dao import ClienteDao
from dao.reserva_dao import ReservaDao
from dao.salones_dao import SalonDao
from dao.tipo_cocina_dao import TipoCocinaDao
from dao.tipo_reserva_dao import TipoReservasDao
from iu.estilo_tabla import estilo_tabla
from iu.iu_reservas import Ui_Reservas
from util.mostrar_mensajes import mostrar_advertencia, mostrar_error
from controller.controller_reserva_edit import ControladorReservas


class ReservasController(QWidget):
    """Controlador para la vista de reservas.

    Gestiona la interfaz de usuario para la visualización y manipulación de reservas.
    Permite la creación de nuevas reservas, la visualización detallada de reservas existentes
    y la selección de salones para filtrar las reservas mostradas.
    """

    def __init__(self, conexion):
        """Inicializa el controlador de reservas.

        Establece la conexión a la base de datos, inicializa los Data Access Objects (DAOs),
        configura la interfaz de usuario desde el archivo `iu_reservas.Ui_Reservas`,
        inicializa el modelo de datos para la tabla y configura la interfaz de usuario inicial.

        Args:
            conexion: Objeto de conexión a la base de datos.
        """
        super().__init__()
        self.conexion = conexion
        self.salon_seleccionado = None
        self.iniciar_daos()
        self.ui = Ui_Reservas()
        self.ui.setupUi(self)
        self.model = QStandardItemModel()
        self.reserva_seleccionada = None
        self.init_ui()

    def iniciar_daos(self):
        """Inicializa los Data Access Objects (DAOs) necesarios para la vista de reservas.

        Crea instancias de los DAOs para interactuar con las tablas de clientes, reservas,
        salones, tipos de cocina y tipos de reserva en la base de datos.
        """
        self.cliente_dao = ClienteDao(self.conexion)
        self.reserva_dao = ReservaDao(self.conexion)
        self.salon_dao = SalonDao(self.conexion)
        self.tipo_cocina_dao = TipoCocinaDao(self.conexion)
        self.tipo_reserva_dao = TipoReservasDao(self.conexion)

    def init_ui(self):
        """Inicializa la interfaz de usuario y conecta los eventos.

        Configura las acciones de los botones (nueva reserva, saber más),
        llena el `QListWidget` con la lista de salones disponibles e inicializa la tabla de reservas.
        """
        self.ui.nuevo_pushButton.clicked.connect(self.nueva_reserva)
        self.ui.saber_pushButton.clicked.connect(self.saber_mas)
        self.llenar_listWid_salones()
        self.iniciar_tabla()

    def nueva_reserva(self):
        """Abre el modal para crear una nueva reserva.

        Verifica si un salón ha sido seleccionado. Si es así, abre el modal de edición de reservas
        para crear una nueva reserva en el salón seleccionado. Si no se ha seleccionado un salón,
        muestra un mensaje de advertencia al usuario.
        """
        if self.salon_seleccionado:
            id_salon = self.traer_id_salon_by_nombre(self.salon_seleccionado)
            self.abrir_modal(id_salon)
        else:
            mostrar_advertencia("Debe selecionar un salon")

    def saber_mas(self):
        """Abre el modal para mostrar información detallada de la reserva seleccionada.

        Obtiene el ID de la reserva seleccionada en la tabla y abre el modal de edición de reservas
        para visualizar la información detallada. Si no se ha seleccionado ninguna reserva,
        muestra un mensaje de error al usuario.
        """
        index = self.ui.reservas_tableView.selectedIndexes()
        if index:
            id_reserva = self.model.item(index[0].row(), 0).text()
            self.abrir_modal(0, id_reserva)
        else:
            mostrar_error("Debe selecionar una reserva")

    def abrir_modal(self, id_salon, id_reserva=None):
        """Abre la ventana modal para edición/creación de reservas.

        Crea una instancia del controlador `ControladorReservas` y ejecuta el modal.
        Recarga la tabla de reservas después de que el modal se cierra para reflejar los cambios.

        Args:
            id_salon (int): ID del salón para el cual se está creando o visualizando la reserva.
            id_reserva (str, optional): ID de la reserva para editar. Defaults to None para crear una nueva reserva.
        """
        ventana_edicion = ControladorReservas(
            id_salon, self.conexion, reserva_id=id_reserva
        )
        ventana_edicion.exec_()
        self.recargar_tabla()

    def iniciar_tabla(self):
        """Configura e inicializa la tabla de reservas.

        Define los encabezados de la tabla, establece el modelo de datos `QStandardItemModel`,
        configura el modo de redimensionamiento de las columnas para que se estiren,
        oculta la cabecera vertical y aplica estilos visuales a la tabla.
        """
        self.tableView = self.ui.reservas_tableView
        headers = ["ID", "Tipo reserva", "Tipo cocina", "Cliente", "Fecha"]
        self.model.setHorizontalHeaderLabels(headers)
        self.tableView.setModel(self.model)
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.setStyleSheet(estilo_tabla)

    def llenar_listWid_salones(self):
        """Llena el QListWidget con la lista de salones disponibles desde la base de datos.

        Recupera la lista de salones utilizando `salon_dao.find_all()` y los añade al `QListWidget`
        para que el usuario pueda seleccionar un salón. Si no se encuentran salones en la base de datos,
        muestra un mensaje de error. Conecta la señal `currentItemChanged` del `QListWidget` al método
        `salon_seleccionado_mod` para manejar la selección de salones.
        """
        self.ui.salones_listWidget.clear()  # Limpia la lista antes de llenarla
        self.lista_salones = self.salon_dao.find_all()  # Obtiene los datos de la BD

        if not self.lista_salones:
            mostrar_error("No se encontraron salones en la base de datos.")
            return

        for salon in self.lista_salones:
            self.ui.salones_listWidget.addItem(salon.nombre)

        self.ui.salones_listWidget.currentItemChanged.connect(
            self.salon_seleccionado_mod
        )

    def salon_seleccionado_mod(self, current, previous):
        """Maneja el evento de cambio de selección de salón en el QListWidget.

        Cuando se selecciona un nuevo salón en el `QListWidget`, este método actualiza
        `self.salon_seleccionado` con el nombre del salón seleccionado y recarga la tabla de reservas
        para mostrar solo las reservas del salón seleccionado.

        Args:
            current (QListWidgetItem): El elemento actualmente seleccionado.
            previous (QListWidgetItem): El elemento previamente seleccionado.
        """
        if current:
            self.salon_seleccionado = current.text()
            self.recargar_tabla()

    def listar_datos(self):
        """Recupera todas las listas de datos necesarias desde la base de datos.

        Obtiene listas de reservas, clientes activos, salones, tipos de cocina y tipos de reserva
        utilizando sus respectivos DAOs para ser utilizadas en la interfaz de usuario.
        """
        self.lista_reservas = self.reserva_dao.find_all()
        self.lista_clientes = self.cliente_dao.find_all_activos()
        self.lista_salones = self.salon_dao.find_all()
        self.lista_tipo_cocinas = self.tipo_cocina_dao.find_all()
        self.lista_tipo_reservas = self.tipo_reserva_dao.find_all()

    def traer_id_salon_by_nombre(self, nombre_salon):
        """Devuelve el ID de un salón dado su nombre.

        Busca en la lista de salones `self.lista_salones` un salón cuyo nombre coincida con `nombre_salon`
        y devuelve su ID.

        Args:
            nombre_salon (str): Nombre del salón a buscar.

        Returns:
            int | None: ID del salón si se encuentra, None si no se encuentra.
        """
        if self.lista_salones:
            salon = next(
                (s for s in self.lista_salones if s.nombre == nombre_salon), None
            )
            return salon.salon_id if salon else None

    def recargar_tabla(self):
        """Recarga los datos de la tabla de reservas, filtrando por el salón seleccionado.

        Limpia el modelo de la tabla, recupera las reservas del salón seleccionado desde la base de datos
        utilizando `reserva_dao.find_all_by_salon_id()` y añade las reservas recuperadas al modelo de la tabla
        para su visualización. Oculta la columna del ID de reserva en la vista de la tabla.
        """
        self.listar_datos()
        self.model.removeRows(0, self.model.rowCount())  # Limpiar la tabla

        if self.salon_seleccionado:
            id_salon = self.traer_id_salon_by_nombre(self.salon_seleccionado)
            if id_salon:
                reservas = self.reserva_dao.find_all_by_salon_id(id_salon)
                if reservas:
                    for r in reservas:
                        row = [
                            QStandardItem(str(r.reserva_id)),
                            QStandardItem(self.nombre_tipo_reserva(r.tipo_reserva_id)),
                            QStandardItem(self.nombre_tipo_cocina(r.tipo_cocina_id)),
                            QStandardItem(self.nombre_completo_clientes(r.id_cliente)),
                            QStandardItem(str(r.fecha)),
                        ]
                        self.model.appendRow(row)

                    self.tableView.setColumnHidden(0, True)

    def nombre_completo_clientes(self, id_cliente):
        """Devuelve el nombre completo de un cliente dado su ID.

        Busca en la lista de clientes `self.lista_clientes` un cliente cuyo ID coincida con `id_cliente`
        y devuelve su nombre completo (Nombre y Apellidos). Si el cliente no se encuentra o la lista de clientes
        no está disponible, devuelve "Eliminado" o "No se encuentra" respectivamente.

        Args:
            id_cliente (int): ID del cliente a buscar.

        Returns:
            str: Nombre completo del cliente o "Eliminado" si no se encuentra en la lista o "No se encuentra" si la lista no está cargada.
        """
        if self.lista_clientes:
            cliente = next((c for c in self.lista_clientes if c.Id == id_cliente), None)
            return f"{cliente.Nombre} {cliente.Apellidos}" if cliente else "Eliminado"
        return "No se encuentra"

    def nombre_tipo_cocina(self, id_tipo_cocina):
        """Devuelve el nombre del tipo de cocina dado su ID.

        Busca en la lista de tipos de cocina `self.lista_tipo_cocinas` un tipo de cocina
        cuyo ID coincida con `id_tipo_cocina` y devuelve su nombre. Si el tipo de cocina no se encuentra
        o la lista no está disponible, devuelve mensajes de error.

        Args:
            id_tipo_cocina (int): ID del tipo de cocina a buscar.

        Returns:
            str: Nombre del tipo de cocina o mensajes de error si no se encuentra.
        """
        if self.lista_tipo_cocinas:
            tipo_cocina = next(
                (
                    t
                    for t in self.lista_tipo_cocinas
                    if t.tipo_cocina_id == id_tipo_cocina
                ),
                None,
            )
            return tipo_cocina.nombre if tipo_cocina else "Algo va mal"
        return "Algo va mal"

    def nombre_tipo_reserva(self, id_tipo_reserva):
        """Devuelve el nombre del tipo de reserva dado su ID.

        Busca en la lista de tipos de reserva `self.lista_tipo_reservas` un tipo de reserva
        cuyo ID coincida con `id_tipo_reserva` y devuelve su nombre. Si el tipo de reserva no se encuentra
        o la lista no está disponible, devuelve mensajes de error.

        Args:
            id_tipo_reserva (int): ID del tipo de reserva a buscar.

        Returns:
            str: Nombre del tipo de reserva o mensajes de error si no se encuentra.
        """
        if self.lista_tipo_reservas:
            tipo_reserva = next(
                (
                    t
                    for t in self.lista_tipo_reservas
                    if t.tipo_reserva_id == id_tipo_reserva
                ),
                None,
            )
            return tipo_reserva.nombre if tipo_reserva else "Algo va mal"
        return "Algo va mal"

    def nombre_salon(self, id_salon):
        """Devuelve el nombre del salón dado su ID.

        Busca en la lista de salones `self.lista_salones` un salón cuyo ID coincida con `id_salon`
        y devuelve su nombre. Si el salón no se encuentra o la lista no está disponible, devuelve mensajes de error.

        Args:
            id_salon (int): ID del salón a buscar.

        Returns:
            str: Nombre del salón o mensajes de error si no se encuentra.
        """
        if self.lista_salones:
            salon = next(
                (s for s in self.lista_salones if s.salon_id == id_salon), None
            )
            return salon.nombre if salon else "Algo va mal"
        return "Algo va mal"
