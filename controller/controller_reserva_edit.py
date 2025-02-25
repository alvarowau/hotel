from PySide6.QtCore import QDate
from PySide6.QtWidgets import QDialog

from dao.clientes_dao import ClienteDao
from dao.reserva_dao import ReservaDao
from dao.salones_dao import SalonDao
from dao.tipo_cocina_dao import TipoCocinaDao
from dao.tipo_reserva_dao import TipoReservasDao
from iu.iu_reserva_edit import Ui_reserva_edit
from model.reserva import Reserva
from util.mostrar_mensajes import (
    mostrar_advertencia,
    mostrar_error,
    mostrar_informacion,
)


class ControladorReservas(QDialog):
    """
    Controlador para la interfaz de gestión de reservas.
    Maneja eventos y validaciones dentro del formulario de reservas.
    """

    SALON_CONGRESO_ID = 3

    def __init__(self, salon_id, conexion, reserva_id=None):
        super().__init__()
        self.ui = Ui_reserva_edit()
        self.ui.setupUi(self)
        self.salon_id = salon_id
        self.conexion = conexion
        self._inicializar_ui()
        self._inicializar_daos()

        if self._cargar_datos_iniciales():
            self._llenar_campos_combobox()
            self._actualizar_visibilidad_widget_congreso()
            self.ui.tipo_reserva_comboBox.currentIndexChanged.connect(
                self._actualizar_visibilidad_widget_congreso
            )
            if reserva_id:
                self.reserva_id_pasada = reserva_id
                self._configurar_ver_detalles()
            else:
                self._configurar_para_creacion()
        else:
            mostrar_error("No se pudieron recuperar datos de la base de datos.")

    def _inicializar_ui(self):
        """Configura la interfaz inicial."""
        self._establecer_fecha_por_defecto()

    def _inicializar_daos(self):
        """Inicializa los DAOs necesarios."""
        self.cliente_dao = ClienteDao(self.conexion)
        self.reserva_dao = ReservaDao(self.conexion)
        self.salon_dao = SalonDao(self.conexion)
        self.tipo_cocina_dao = TipoCocinaDao(self.conexion)
        self.tipo_reserva_dao = TipoReservasDao(self.conexion)

    def _cargar_datos_iniciales(self) -> bool:
        """Carga los datos iniciales desde la base de datos."""
        self.lista_salones = self.salon_dao.find_all() or []
        self.lista_tipos_cocina = self.tipo_cocina_dao.find_all() or []
        self.lista_tipos_reserva = self.tipo_reserva_dao.find_all() or []
        self.lista_clientes = self.cliente_dao.find_all_activos()
        return all(
            [
                self.lista_salones,
                self.lista_tipos_cocina,
                self.lista_tipos_reserva,
                self.lista_clientes,
            ]
        )

    def _llenar_campos_combobox(self):
        """Llena los ComboBox con los datos disponibles."""
        self._llenar_combobox_tipos_reserva()
        self._llenar_combobox_tipos_cocina()
        self._llenar_combobox_salones()
        self._llenar_combobox_clientes()

    def _actualizar_visibilidad_widget_congreso(self):
        """Muestra u oculta el widget según el tipo de reserva seleccionado."""
        tipo_reserva_id = self.ui.tipo_reserva_comboBox.currentData()
        self.ui.widget_oculto.setVisible(tipo_reserva_id == self.SALON_CONGRESO_ID)

    def _configurar_ver_detalles(self):
        self.reserva_pasada = self.reserva_dao.find_by_id(self.reserva_id_pasada)
        if self.reserva_pasada:
            self.ui.title_label.setText("Detalles de la reserva")
            self.ui.boton_izquierdo_pushButton.setText("Eliminar")
            self.ui.boton_derecho_pushButton.setText("Editar")
            self.llenar_campos_edicion()
            self._semaforo_campos(False)
            self.ui.boton_derecho_pushButton.clicked.connect(
                self._configurar_para_editar
            )
            self.ui.boton_izquierdo_pushButton.clicked.connect(self._eliminar_reserva)
        else:
            mostrar_error("No se ha podido recuperar la reserva")
            self.accept()

    def _configurar_para_editar(self):
        self._semaforo_campos(True)
        self.ui.boton_izquierdo_pushButton.setVisible(False)
        self.ui.boton_derecho_pushButton.setText("Guardar")
        self.ui.boton_derecho_pushButton.clicked.connect(self._guardar_modificacion)

    def _comprobar_fechas_modificacion(self, datos):
        if self.reserva_pasada:
            if (
                str(self.reserva_pasada.fecha) == datos["fecha"]
                and self.reserva_pasada.salon_id == datos["salon_id"]
            ):
                return True
            else:
                if self.reserva_dao.is_fecha_dispon(
                    fecha=datos["fecha"], salon_id=datos["salon_id"]
                ):
                    return True
                else:
                    mostrar_error("La fecha no esta disponible")
                    return False
        else:
            mostrar_error("Ocurrio un error")
            return False

    def _guardar_modificacion(self):
        datos = self._obtener_datos_reserva()
        if self._comprobar_fechas_modificacion(datos):
            if self.reserva_dao.update(Reserva.from_dict(datos)):
                mostrar_advertencia("La reserva se modifico correctamente")
            else:
                mostrar_error("La reserva no pudo ser modifcada")

        print(f"quiere modificar la reserva: {datos}")

    def _eliminar_reserva(self):
        print(f"quiere eliminar la reserva {self.reserva_pasada}")

    def llenar_campos_edicion(self):
        if self.reserva_pasada:
            self._seleccionar_cliente_por_id(self.reserva_pasada.id_cliente)
            self._seleccionar_salon_por_id(self.reserva_pasada.salon_id)
            self._seleccionar_tipo_cocina_por_id(self.reserva_pasada.tipo_cocina_id)
            self._seleccionar_tipo_reserva_por_id(self.reserva_pasada.tipo_reserva_id)
            self._establecer_fecha_por_defecto(self.reserva_pasada.fecha)
            self.ui.habitaciones_checkBox.setChecked(
                bool(self.reserva_pasada.habitaciones)
            )
            self.ui.jornadas_spinBox.setValue(
                0
                if self.reserva_pasada.jornadas is None
                else self.reserva_pasada.jornadas
            )
            self.ui.asistentes_spinBox.setValue(
                0
                if self.reserva_pasada.ocupacion is None
                else self.reserva_pasada.ocupacion
            )

    def _semaforo_campos(self, semaforo: bool):
        self.ui.cliente_comboBox.setEnabled(semaforo)
        self.ui.fecha_dateEdit.setEnabled(semaforo)
        self.ui.salon_comboBox.setEnabled(semaforo)
        self.ui.tipo_reserva_comboBox.setEnabled(semaforo)
        self.ui.tipo_cocina_comboBox.setEnabled(semaforo)
        self.ui.asistentes_spinBox.setEnabled(semaforo)
        self.ui.jornadas_spinBox.setEnabled(semaforo)
        self.ui.habitaciones_checkBox.setEnabled(semaforo)

    def _configurar_para_creacion(self):
        """Configura la interfaz para la creación de una nueva reserva."""
        if self.salon_id:
            self.ui.title_label.setText("Creación de Reserva")
            self.ui.boton_izquierdo_pushButton.setText("Salir")
            self.ui.boton_izquierdo_pushButton.setStyleSheet(
                "background-color: #DB4437; color: white;"
            )
            self.ui.boton_derecho_pushButton.setText("Guardar")

            self.ui.boton_izquierdo_pushButton.clicked.connect(self.accept)
            self.ui.boton_derecho_pushButton.clicked.connect(self._guardar_reserva)
            self._seleccionar_salon_por_id(self.salon_id)
        else:
            mostrar_error("Ha ocurrido un error.")
            self.accept()

    def _obtener_datos_reserva(self) -> dict:
        """Recoge los datos ingresados por el usuario."""
        tipo_reserva_id = self.ui.tipo_reserva_comboBox.currentData()
        return {
            "id_cliente": self.ui.cliente_comboBox.currentData(),
            "salon_id": self.ui.salon_comboBox.currentData(),
            "tipo_reserva_id": tipo_reserva_id,
            "tipo_cocina_id": self.ui.tipo_cocina_comboBox.currentData(),
            "ocupacion": self.ui.asistentes_spinBox.value(),
            "fecha": self.ui.fecha_dateEdit.date().toString("yyyy-MM-dd"),
            "jornadas": self.ui.jornadas_spinBox.value() if tipo_reserva_id == 3 else 0,
            "habitaciones": (
                self.ui.habitaciones_checkBox.isChecked()
                if tipo_reserva_id == 3
                else False
            ),
        }

    def _guardar_reserva(self):
        """Guarda una nueva reserva en la base de datos."""
        datos = self._obtener_datos_reserva()
        if self.reserva_dao.is_fecha_dispon(datos["salon_id"], datos["fecha"]):
            nueva_reserva = Reserva.from_dict(datos)
            if self.reserva_dao.create(nueva_reserva):
                mostrar_informacion("La reserva ha sido creada.")
                self.accept()
            else:
                mostrar_error("No se pudo crear la reserva.")
        else:
            mostrar_error("La fecha no está disponible para este salón.")

    def _seleccionar_salon_por_id(self, salon_id):
        """Selecciona un salón en el ComboBox según su ID."""
        for index in range(self.ui.salon_comboBox.count()):
            if self.ui.salon_comboBox.itemData(index) == salon_id:
                self.ui.salon_comboBox.setCurrentIndex(index)
                return
        mostrar_error(f"No se encontró un salón con ID {salon_id}.")

    def _seleccionar_cliente_por_id(self, cliente_id):
        for index in range(self.ui.cliente_comboBox.count()):
            if self.ui.cliente_comboBox.itemData(index) == cliente_id:
                self.ui.cliente_comboBox.setCurrentIndex(index)
                return
        mostrar_error(f"no se encontro cliente con el id {cliente_id}")

    def _seleccionar_tipo_reserva_por_id(self, reserva_id):
        for index in range(self.ui.tipo_reserva_comboBox.count()):
            if self.ui.tipo_reserva_comboBox.itemData(index) == reserva_id:
                self.ui.tipo_reserva_comboBox.setCurrentIndex(index)
                return
        mostrar_error(f"no se encontro tipo_reserva con el id {reserva_id}")

    def _seleccionar_tipo_cocina_por_id(self, cocina_id):
        for index in range(self.ui.tipo_cocina_comboBox.count()):
            if self.ui.tipo_cocina_comboBox.itemData(index) == cocina_id:
                self.ui.tipo_cocina_comboBox.setCurrentIndex(index)
                return
        mostrar_error(f"no se tipo_cocina con el id {cocina_id}")

    def _llenar_combobox_clientes(self):
        """Llena el ComboBox de clientes."""
        if self.lista_clientes:
            for cliente in self.lista_clientes:
                self.ui.cliente_comboBox.addItem(
                    f"{cliente.Nombre} {cliente.Apellidos}", cliente.Id
                )

    def _llenar_combobox_salones(self):
        """Llena el ComboBox de salones."""
        for salon in self.lista_salones:
            self.ui.salon_comboBox.addItem(salon.nombre, salon.salon_id)

    def _llenar_combobox_tipos_cocina(self):
        """Llena el ComboBox de tipos de cocina."""
        for tipo_cocina in self.lista_tipos_cocina:
            self.ui.tipo_cocina_comboBox.addItem(
                tipo_cocina.nombre, tipo_cocina.tipo_cocina_id
            )

    def _llenar_combobox_tipos_reserva(self):
        """Llena el ComboBox de tipos de reserva."""
        for tipo_reserva in self.lista_tipos_reserva:
            self.ui.tipo_reserva_comboBox.addItem(
                tipo_reserva.nombre, tipo_reserva.tipo_reserva_id
            )

    def _establecer_fecha_por_defecto(self, fecha=None):
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
