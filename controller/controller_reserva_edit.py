from datetime import datetime

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
    confirmar_mensaje,
    mostrar_advertencia,
    mostrar_error,
    mostrar_informacion,
)


class ControladorReservas(QDialog):
    """Controlador para la interfaz de gestión de reservas.

    Maneja eventos y validaciones dentro del formulario de reservas.
    """

    SALON_CONGRESO_ID = 3
    TIPO_RESERVA_CONGRESO_ID = 3

    def __init__(self, salon_id, conexion, reserva_id=None):
        """Constructor de ControladorReservas.

        Args:
            salon_id (int): ID del salón para la reserva.
            conexion (QSqlDatabase): Conexión a la base de datos.
            reserva_id (int, optional): ID de la reserva a editar. Defaults to None.
        """
        super().__init__()
        self.ui = Ui_reserva_edit()
        self.ui.setupUi(self)
        self.salon_id = salon_id
        self.conexion = conexion
        self._inicializar_ui()
        self._inicializar_daos()
        self.setWindowTitle("Gestión de Reservas")
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
        """Carga los datos iniciales desde la base de datos.

        Returns:
            bool: True si todos los datos se cargaron correctamente, False en caso contrario.
        """
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
        """Configura la vista para mostrar los detalles de una reserva."""
        self.reserva_pasada = self.reserva_dao.find_by_id(self.reserva_id_pasada)
        if self.reserva_pasada:
            self.llenar_campos_edicion()
            self._semaforo_campos(False)
            self.ui.title_label.setText("Detalles de la reserva")
            if self._is_editable_fecha_reserva():
                if self._is_editable_cliente_reserva():
                    self.ui.boton_izquierdo_pushButton.setText("Eliminar")
                    self.ui.boton_derecho_pushButton.setText("Editar")
                    self.ui.boton_derecho_pushButton.clicked.connect(
                        self._configurar_para_editar
                    )
                    self.ui.boton_izquierdo_pushButton.clicked.connect(
                        self._eliminar_reserva
                    )
                else:
                    mostrar_advertencia(
                        "La reservas con cliente eliminado no pueden ser editadas ni eliminadas"
                    )
                    self.ui.cliente_comboBox.clear()
                    self.ui.cliente_comboBox.addItem("Cliente eliminado")
                    self.ui.boton_izquierdo_pushButton.setVisible(False)
                    self.ui.boton_derecho_pushButton.setText("Salir")
                    self.ui.boton_derecho_pushButton.clicked.connect(
                        self._salir_de_la_no_edicion
                    )
            else:
                mostrar_advertencia(
                    "La reservas con fechas pasadas no pueden ser editas ni eliminadas"
                )
                if not self._is_editable_cliente_reserva():
                    self.ui.cliente_comboBox.clear()
                    self.ui.cliente_comboBox.addItem("Cliente eliminado")
                self.ui.boton_izquierdo_pushButton.setVisible(False)
                self.ui.boton_derecho_pushButton.setText("Salir")
                self.ui.boton_derecho_pushButton.clicked.connect(
                    self._salir_de_la_no_edicion
                )
        else:
            mostrar_error("No se ha podido recuperar la reserva")
            self.accept()

    def _salir_de_la_no_edicion(self):
        """Sale del modo no editable."""
        self.accept()

    def _is_editable_cliente_reserva(self) -> bool:
        """Verifica si el cliente de la reserva es editable.

        Returns:
            bool: True si el cliente es editable, False en caso contrario.
        """
        if self.reserva_pasada:
            cliente = self.cliente_dao.find_all_by_id(self.reserva_pasada.id_cliente)
            return bool(cliente)
        return False

    def _is_editable_fecha_reserva(self) -> bool:
        """Verifica si la fecha de la reserva es editable.

        Returns:
            bool: True si la fecha es editable, False en caso contrario.
        """
        fecha_hoy = datetime.now().date()
        if self.reserva_pasada:
            fecha_reserva = self.reserva_pasada.fecha
            return fecha_reserva >= fecha_hoy # type: ignore
        return False

    def _configurar_para_editar(self):
        """Configura la vista para la edición de una reserva."""
        self._semaforo_campos(True)
        self.ui.boton_izquierdo_pushButton.setVisible(False)
        self.ui.boton_derecho_pushButton.setText("Guardar")
        self.ui.boton_derecho_pushButton.clicked.connect(self._guardar_modificacion)

    def _comprobar_fechas_modificacion(self, datos: dict) -> bool:
        """Comprueba si la fecha para la modificación es válida.

        Args:
            datos (dict): Diccionario con los datos de la reserva.

        Returns:
            bool: True si la fecha es válida, False en caso contrario.
        """
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
        """Guarda la modificación de la reserva en la base de datos."""
        datos = self._obtener_datos_reserva()
        if self._comprobar_fechas_modificacion(datos):
            reserva_nueva = Reserva.from_dict(datos)
            reserva_nueva.reserva_id = self.reserva_id_pasada
            respuesta = self.reserva_dao.update(reserva_nueva)
            if respuesta:
                mostrar_advertencia("La reserva se modifico correctamente")
                self.accept()
            else:
                mostrar_error("La reserva no pudo ser modifcada")

    def _eliminar_reserva(self):
        """Elimina la reserva actual tras confirmación del usuario."""
        detalles_reserva = self.reserva_dao.traer_details_delete(self.reserva_id_pasada)
        mensaje = f"¿Está seguro de que desea eliminar la reserva?\n{detalles_reserva}"

        if confirmar_mensaje(mensaje):
            try:
                if self.reserva_dao.delete(self.reserva_id_pasada):
                    mostrar_advertencia("La reserva ha sido eliminada correctamente.")
                else:
                    mostrar_error(
                        "No se pudo eliminar la reserva. Verifique el ID proporcionado."
                    )
            except Exception as e:
                mostrar_error(f"Hubo un error al eliminar la reserva: {e}")
        else:
            mostrar_informacion("Eliminación de reserva cancelada por el usuario.")

    def llenar_campos_edicion(self):
        """Llena los campos del formulario con los datos de la reserva para edición."""
        if self.reserva_pasada:
            self._seleccionar_cliente_por_id(self.reserva_pasada.id_cliente)  # type: ignore
            self._seleccionar_salon_por_id(self.reserva_pasada.salon_id)  # type: ignore
            self._seleccionar_tipo_cocina_por_id(self.reserva_pasada.tipo_cocina_id)  # type: ignore
            self._seleccionar_tipo_reserva_por_id(self.reserva_pasada.tipo_reserva_id)  # type: ignore
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
        """Habilita o deshabilita los campos de edición del formulario.

        Args:
            semaforo (bool): True para habilitar, False para deshabilitar.
        """
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
        """Recoge los datos del formulario para crear o modificar una reserva.

        Returns:
            dict: Diccionario con los datos de la reserva.
        """
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

    def _establecer_fecha_por_defecto(self, fecha=None):
        """Establece la fecha por defecto en el DateEdit.

        Args:
            fecha (QDate, optional): Fecha a establecer. Defaults to None (fecha actual).
        """
        fecha = fecha or QDate.currentDate()
        self.ui.fecha_dateEdit.setDate(fecha)
        self.ui.fecha_dateEdit.setMinimumDate(fecha)
        self.ui.fecha_dateEdit.setCalendarPopup(True)
        self.ui.fecha_dateEdit.setDisplayFormat("yyyy-MM-dd")

    def _seleccionar_salon_por_id(self, salon_id: int):
        """Selecciona un salón en el ComboBox de salones por su ID.

        Args:
            salon_id (int): ID del salón a seleccionar.
        """
        for index in range(self.ui.salon_comboBox.count()):
            if self.ui.salon_comboBox.itemData(index) == salon_id:
                self.ui.salon_comboBox.setCurrentIndex(index)
                return

    def _seleccionar_cliente_por_id(self, cliente_id: int):
        """Selecciona un cliente en el ComboBox de clientes por su ID.

        Args:
            cliente_id (int): ID del cliente a seleccionar.
        """
        for index in range(self.ui.cliente_comboBox.count()):
            if self.ui.cliente_comboBox.itemData(index) == cliente_id:
                self.ui.cliente_comboBox.setCurrentIndex(index)
                return

    def _seleccionar_tipo_reserva_por_id(self, reserva_id: int):
        """Selecciona un tipo de reserva en el ComboBox de tipos de reserva por su ID.

        Args:
            reserva_id (int): ID del tipo de reserva a seleccionar.
        """
        for index in range(self.ui.tipo_reserva_comboBox.count()):
            if self.ui.tipo_reserva_comboBox.itemData(index) == reserva_id:
                self.ui.tipo_reserva_comboBox.setCurrentIndex(index)
                return

    def _seleccionar_tipo_cocina_por_id(self, cocina_id: int):
        """Selecciona un tipo de cocina en el ComboBox de tipos de cocina por su ID.

        Args:
            cocina_id (int): ID del tipo de cocina a seleccionar.
        """
        for index in range(self.ui.tipo_cocina_comboBox.count()):
            if self.ui.tipo_cocina_comboBox.itemData(index) == cocina_id:
                self.ui.tipo_cocina_comboBox.setCurrentIndex(index)
                return

    def _llenar_combobox_clientes(self):
        """Llena el ComboBox de clientes con la lista de clientes."""
        if self.lista_clientes:
            for cliente in self.lista_clientes:
                self.ui.cliente_comboBox.addItem(
                    f"{cliente.Nombre} {cliente.Apellidos}", cliente.Id
                )

    def _llenar_combobox_salones(self):
        """Llena el ComboBox de salones con la lista de salones."""
        for salon in self.lista_salones:
            self.ui.salon_comboBox.addItem(salon.nombre, salon.salon_id)

    def _llenar_combobox_tipos_cocina(self):
        """Llena el ComboBox de tipos de cocina con la lista de tipos de cocina."""
        for tipo_cocina in self.lista_tipos_cocina:
            self.ui.tipo_cocina_comboBox.addItem(
                tipo_cocina.nombre, tipo_cocina.tipo_cocina_id
            )

    def _llenar_combobox_tipos_reserva(self):
        """Llena el ComboBox de tipos de reserva con la lista de tipos de reserva."""
        for tipo_reserva in self.lista_tipos_reserva:
            self.ui.tipo_reserva_comboBox.addItem(
                tipo_reserva.nombre, tipo_reserva.tipo_reserva_id
            )
