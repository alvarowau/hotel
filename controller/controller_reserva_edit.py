from PySide6.QtCore import QDate
from PySide6.QtWidgets import QDialog

from dao.clientes_dao import ClienteDao
from dao.reserva_dao import ReservaDao
from dao.salones_dao import SalonDao
from dao.tipo_cocina_dao import TipoCocinaDao
from dao.tipo_reserva_dao import TipoReservasDao
from iu.iu_reserva_edit import Ui_reserva_edit
from model.reserva import Reserva
from util.mostrar_mensajes import mostrar_error

# ! modificar el limite de la fecha


# ? ¿Está correcto este enfoque? Necesitamos revisar si es la mejor solución.
# // Esto ya no es relevante y se eliminará en la siguiente versión.
# TODO: Implementar la validación de entrada más tarde.
# * Nota: Este es un comportamiento esperado en la mayoría de los casos.


class ControladorReservas(QDialog):
    """
    Controlador para la interfaz de gestión de reservas.
    Maneja eventos y validaciones dentro del formulario de reservas.
    """

    TIPO_RESERVA_ESPECIAL = 3  # Constante para el tipo de reserva especial

    def __init__(self, id_tipo_salon, conexion, id_reserva=None):
        super().__init__()
        self.ui = Ui_reserva_edit()
        self.ui.setupUi(self)
        self.id_salon_recivido = id_tipo_salon
        self.conexion = conexion
        self._inicializar_interfaz()
        self._iniciar_daos()

        if self._listar_datos():
            self._llenar_combo_box()
            self._resucitar_widget()
            self.ui.tipo_reserva_comboBox.currentIndexChanged.connect(
                self._resucitar_widget
            )
            if id_reserva:
                self._iniciar_modificacion()
            else:
                self._iniciar_creacion()
        else:
            mostrar_error("No se han podido recuperar datos de la base de datos")

    def _inicializar_interfaz(self):
        """Inicializa la interfaz de usuario."""
        self._establece_fecha_interface()

    def _resucitar_widget(self):
        """Muestra u oculta el widget oculto según el tipo de reserva seleccionado."""
        tipo_reserva = self.ui.tipo_reserva_comboBox.currentData()
        self.ui.widget_oculto.setVisible(tipo_reserva == self.TIPO_RESERVA_ESPECIAL)

    def _llenar_combo_box(self):
        """Llena los combobox con los datos correspondientes."""
        self._combo_box_tipo_reserva()
        self._combo_box_tipo_cocina()
        self._combo_box_salon()
        self._combo_box_clientes()

    def _iniciar_modificacion(self):
        """Inicia la modificación de una reserva existente."""
        # Aquí va la lógica para la modificación de una reserva
        pass

    def _salir_pantalla(self):
        """Cierra la ventana actual."""
        self.accept()
        self.close()

    def _iniciar_creacion(self):
        """Inicia la creación de una nueva reserva."""
        if self.id_salon_recivido:
            self.ui.title_label.setText("Creacion Reserva")
            self.ui.boton_izquierdo_pushButton.setText("Salir")
            self.ui.boton_izquierdo_pushButton.setStyleSheet(
                "background-color: #DB4437; color: white;"
            )
            self.ui.boton_derecho_pushButton.setText("Guardar")

            self.ui.boton_izquierdo_pushButton.clicked.connect(self._salir_pantalla)
            self.ui.boton_derecho_pushButton.clicked.connect(
                self._guardar_reserva_nueva
            )
            self._combobox_seleccionar_salon_por_id(self.id_salon_recivido)
        else:
            mostrar_error("Ha ocurrido un error")
            self._salir_pantalla()

    def _recoger_datos(self):
        # Recolectar los datos del formulario
        cliente_id = self.ui.cliente_comboBox.currentData()
        salon_id = self.ui.salon_comboBox.currentData()
        tipo_reserva_id = self.ui.tipo_reserva_comboBox.currentData()
        tipo_cocina_id = self.ui.tipo_cocina_comboBox.currentData()
        asistentes = self.ui.asistentes_spinBox.value()
        fecha = self.ui.fecha_dateEdit.date().toString("yyyy-MM-dd")

        # Crear un diccionario con los datos
        datos = {
            "id_cliente": cliente_id,
            "salon_id": salon_id,
            "tipo_reserva_id": tipo_reserva_id,
            "tipo_cocina_id": tipo_cocina_id,
            "ocupacion": asistentes,
            "fecha": fecha,
        }

        # Si el tipo de reserva es 3, agregar más datos
        if tipo_reserva_id == 3:
            jornadas = self.ui.jornadas_spinBox.value()
            habitaciones = self.ui.habitaciones_checkBox.isChecked()

            # Agregar estos datos al diccionario
            datos["jornadas"] = jornadas
            datos["habitaciones"] = habitaciones
        else:
            datos["jornadas"] = 0
            datos["habitaciones"] = False
        # Retornar el diccionario con todos los datos
        return datos

    # ! terminar este metodo para continuar
    def _guardar_reserva_nueva(self):
        """Guarda una nueva reserva en la base de datos."""
        datos = self._recoger_datos()
        if self.reserva_dao.is_fecha_dispon(datos["salon_id"], datos["fecha"]):
            """reserva = Reserva(
                tipo_reserva_id=datos["tipo_reserva_id"],
                salon_id=datos["salon_id"],
                tipo_cocina_id=datos["tipo_cocina_id"],
                id_cliente=datos["id_cliente"],
                fecha=datos["fecha"],
                ocupacion=datos["ocupacion"],
                jornadas=datos["jornadas"],
                habitaciones=datos["habitaciones"],
            )"""
            reserva_dos = Reserva.from_dict(datos)
            print(reserva_dos)
        else:
            mostrar_error("La fecha no esta disponible para este salon")

    def _iniciar_daos(self):
        """Inicializa los DAOs necesarios."""
        self.cliente_dao = ClienteDao(self.conexion)
        self.reserva_dao = ReservaDao(self.conexion)
        self.salon_dao = SalonDao(self.conexion)
        self.tipo_cocina_dao = TipoCocinaDao(self.conexion)
        self.tipo_reserva_dao = TipoReservasDao(self.conexion)

    def _listar_datos(self) -> bool:
        """
        Obtiene y almacena las listas de objetos de la base de datos.
        Retorna True si todas las consultas fueron exitosas y devolvieron datos.
        """
        self.lista_salones = self.salon_dao.find_all() or []
        self.lista_tipo_cocina = self.tipo_cocina_dao.find_all() or []
        self.lista_tipo_reserva = self.tipo_reserva_dao.find_all() or []
        self.lista_clientes = self.cliente_dao.find_all_activos()

        return bool(
            self.lista_salones
            and self.lista_tipo_cocina
            and self.lista_tipo_reserva
            and self.lista_clientes
        )

    def _combobox_seleccionar_cliente_por_id(self, id_cliente):
        """Selecciona el cliente en el comboBox por su ID."""
        for index in range(self.ui.cliente_comboBox.count()):
            cliente_id = self.ui.cliente_comboBox.itemData(index)
            if cliente_id == id_cliente:
                self.ui.cliente_comboBox.setCurrentIndex(index)
                return
        mostrar_error(f"No se encontró un cliente con ID {id_cliente}")

    def _combobox_seleccionar_salon_por_id(self, id_salon):
        """Selecciona el salón en el comboBox por su ID."""
        for index in range(self.ui.salon_comboBox.count()):
            salon_id = self.ui.salon_comboBox.itemData(index)
            if salon_id == id_salon:
                self.ui.salon_comboBox.setCurrentIndex(index)
                return
        mostrar_error(f"No se encontró un salón con ID {id_salon}")

    def _combobox_seleccionar_tipo_cocina_por_id(self, id_tipo_cocina):
        """Selecciona el tipo de cocina en el comboBox por su ID."""
        for index in range(self.ui.tipo_cocina_comboBox.count()):
            tipo_cocina_id = self.ui.tipo_cocina_comboBox.itemData(index)
            if tipo_cocina_id == id_tipo_cocina:
                self.ui.tipo_cocina_comboBox.setCurrentIndex(index)
                return
        mostrar_error(f"No se encontró un tipo de cocina con ID {id_tipo_cocina}")

    def _combobox_seleccionar_tipo_reserva_por_id(self, id_tipo_reserva):
        """Selecciona el tipo de reserva en el comboBox por su ID."""
        for index in range(self.ui.tipo_reserva_comboBox.count()):
            tipo_reserva_id = self.ui.tipo_reserva_comboBox.itemData(index)
            if tipo_reserva_id == id_tipo_reserva:
                self.ui.tipo_reserva_comboBox.setCurrentIndex(index)
                return
        mostrar_error(f"No se encontró un tipo de reserva con ID {id_tipo_reserva}")

    def _combo_box_clientes(self):
        """Carga los clientes en el ComboBox."""
        if self.lista_clientes:
            for cliente in self.lista_clientes:
                nombre_completo = f"{cliente.Nombre} {cliente.Apellidos}"
                self.ui.cliente_comboBox.addItem(nombre_completo, cliente.Id)
        else:
            mostrar_error("Ocurrió un error al cargar los clientes")
            self.close()

    def _combo_box_salon(self):
        """Carga los salones en el ComboBox."""
        if self.lista_salones:
            for salon in self.lista_salones:
                self.ui.salon_comboBox.addItem(salon.nombre, salon.salon_id)
        else:
            mostrar_error("Ocurrió un error al cargar los salones")
            self.close()

    def _combo_box_tipo_cocina(self):
        """Carga los tipos de cocina en el ComboBox."""
        if self.lista_tipo_cocina:
            for tipo_cocina in self.lista_tipo_cocina:
                self.ui.tipo_cocina_comboBox.addItem(
                    tipo_cocina.nombre, tipo_cocina.tipo_cocina_id
                )
        else:
            mostrar_error("Ocurrió un error al cargar los tipos de cocina")
            self.close()

    def _combo_box_tipo_reserva(self):
        """Carga los tipos de reserva en el ComboBox."""
        if self.lista_tipo_reserva:
            for tipo_reserva in self.lista_tipo_reserva:
                self.ui.tipo_reserva_comboBox.addItem(
                    tipo_reserva.nombre, tipo_reserva.tipo_reserva_id
                )
        else:
            mostrar_error("Ocurrió un error al cargar los tipos de reserva")
            self.close()

    def _establece_fecha_interface(self, fecha=None):
        """
        Establece la fecha en la interfaz.

        Args:
            fecha (QDate | None): Fecha a establecer. Si es None, se usa la fecha actual.
        """
        fecha = fecha or QDate.currentDate()
        self.ui.fecha_dateEdit.setDate(fecha)
        # self.ui.fecha_dateEdit.setMinimumDate(fecha)
        self.ui.fecha_dateEdit.setCalendarPopup(True)
        self.ui.fecha_dateEdit.setDisplayFormat("yyyy-MM-dd")
