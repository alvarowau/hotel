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
    """Controlador para la vista de reservas."""

    def __init__(self, conexion):
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
        """Inicializa los DAOs."""
        self.cliente_dao = ClienteDao(self.conexion)
        self.reserva_dao = ReservaDao(self.conexion)
        self.salon_dao = SalonDao(self.conexion)
        self.tipo_cocina_dao = TipoCocinaDao(self.conexion)
        self.tipo_reserva_dao = TipoReservasDao(self.conexion)

    def init_ui(self):
        """Inicializa la interfaz de usuario y conecta los eventos."""
        self.ui.nuevo_pushButton.clicked.connect(self.nueva_reserva)
        self.ui.saber_pushButton.clicked.connect(self.saber_mas)
        self.llenar_listWid_salones()
        self.iniciar_tabla()

    def nueva_reserva(self):
        if self.salon_seleccionado:
            id_salon = self.traer_id_salon_by_nombre(self.salon_seleccionado)
            self.abrir_modal(id_salon)
        else:
            mostrar_advertencia("Debe selecionar un salon")

    def saber_mas(self):
        """Lógica para mostrar más información sobre la reserva seleccionada."""
        index = self.ui.reservas_tableView.selectedIndexes()
        if index:
            id_reserva = self.model.item(index[0].row(),0).text()
            self.abrir_modal(0, id_reserva)
        else:
            mostrar_error("Debe selecionar una reserva")

    def abrir_modal(self, id_salon, id_reserva = None):
        ventana_edicion = ControladorReservas(
            id_salon,
            self.conexion,
            reserva_id=id_reserva
        )
        ventana_edicion.exec_()
        self.recargar_tabla()

    def iniciar_tabla(self):
        """Configura la tabla inicialmente sin datos."""
        self.tableView = self.ui.reservas_tableView
        headers = ["ID", "Tipo reserva", "Tipo cocina", "Cliente", "Fecha"]
        self.model.setHorizontalHeaderLabels(headers)
        self.tableView.setModel(self.model)
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.setStyleSheet(estilo_tabla)

    def llenar_listWid_salones(self):
        """Llena el QListWidget con la lista de salones disponibles."""
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
        """Muestra el salón seleccionado."""
        if current:
            self.salon_seleccionado = current.text()
            self.recargar_tabla()

    def listar_datos(self):
        """Obtiene todas las listas necesarias para cargar los datos en la interfaz."""
        self.lista_reservas = self.reserva_dao.find_all()
        self.lista_clientes = self.cliente_dao.find_all_activos()
        self.lista_salones = self.salon_dao.find_all()
        self.lista_tipo_cocinas = self.tipo_cocina_dao.find_all()
        self.lista_tipo_reservas = self.tipo_reserva_dao.find_all()

    def traer_id_salon_by_nombre(self, nombre_salon):
        """Devuelve el ID del salón dado su nombre."""
        if self.lista_salones:
            salon = next(
                (s for s in self.lista_salones if s.nombre == nombre_salon), None
            )
            return salon.salon_id if salon else None

    def recargar_tabla(self):
        """Recarga la tabla con datos actualizados."""
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
        """Devuelve el nombre completo de un cliente."""
        if self.lista_clientes:
            cliente = next((c for c in self.lista_clientes if c.Id == id_cliente), None)
            return f"{cliente.Nombre} {cliente.Apellidos}" if cliente else "Eliminado"
        return "No se encuentra"

    def nombre_tipo_cocina(self, id_tipo_cocina):
        """Devuelve el nombre del tipo de cocina dado su ID."""
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
        """Devuelve el nombre del tipo de reserva dado su ID."""
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
        """Devuelve el nombre del salón dado su ID."""
        if self.lista_salones:
            salon = next(
                (s for s in self.lista_salones if s.salon_id == id_salon), None
            )
            return salon.nombre if salon else "Algo va mal"
        return "Algo va mal"
