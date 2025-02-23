from PySide6.QtCore import QDate
from PySide6.QtWidgets import QDialog

from dao.clientes_dao import ClienteDao
from iu.iu_clientes_edit import Ui_clientes_edit
from model.cliente import Cliente
from util.mostrar_mensajes import confirmar_mensaje, mostrar_error, mostrar_informacion


class ControladorClientesEdit(QDialog):
    """Controlador para la edición y creación de clientes."""

    def __init__(self, conexion, id_cliente=None):
        super().__init__()
        self.ui = Ui_clientes_edit()
        self.ui.setupUi(self)
        self.conexion = conexion
        self.cliente_dao = ClienteDao(self.conexion)
        self.__llenar_combox_sexo()

        if id_cliente:
            self.id_cliente = id_cliente
            self.configurar_ventana_cliente_edicion()
        else:
            self.configurar_ventana_cliente_nuevo()

    def configurar_ventana_cliente_edicion(self):
        """Configura la interfaz para la edición de un cliente existente."""
        self.semaforo_campos(False)
        self.cliente_edicion = self.cliente_dao.find_all_by_id(self.id_cliente)
        if self.cliente_edicion:
            self.cargar_datos(self.cliente_edicion)
            self.ui.boton_izquierdo_pushButton.setText("Eliminar")
            self.ui.boton_derecho_pushButton.setText("Editar")
            self.ui.boton_izquierdo_pushButton.clicked.connect(self._eliminar_cliente)
            self.ui.boton_derecho_pushButton.clicked.connect(self._habilitar_edicion)

    def _habilitar_edicion(self):
        """Habilita la edición de los campos del cliente."""
        self.semaforo_campos(True)
        self.ui.boton_izquierdo_pushButton.setVisible(False)
        self.ui.boton_derecho_pushButton.setText("Guardar")
        self.ui.boton_derecho_pushButton.clicked.disconnect()
        self.ui.boton_derecho_pushButton.clicked.connect(self.guardar_edicion)

    def guardar_edicion(self):
        """Guarda los cambios realizados en la edición del cliente."""
        pass

    def _eliminar_cliente(self):
        """Elimina un cliente tras confirmación."""
        nombre_completo = self.cliente_dao.find_nombre_by_id(self.id_cliente)
        mensaje = f"¿Está seguro que desea eliminar el cliente {nombre_completo}?"
        if confirmar_mensaje(mensaje):
            if self.cliente_dao.deactivate(self.id_cliente):
                mostrar_informacion(f"El cliente {nombre_completo} ha sido eliminado")
            else:
                mostrar_error(f"No se pudo eliminar el cliente {nombre_completo}")
        self.accept()

    def semaforo_campos(self, estado):
        """Habilita o deshabilita los campos de la interfaz."""
        self.ui.dni_lineEdit.setEnabled(estado)
        self.ui.mail_lineEdit.setEnabled(estado)
        self.ui.pais_lineEdit.setEnabled(estado)
        self.ui.nombre_lineEdit.setEnabled(estado)
        self.ui.telefono_lineEdit.setEnabled(estado)
        self.ui.apellidos_lineEdit.setEnabled(estado)
        self.ui.fecha_dateEdit.setEnabled(estado)
        self.ui.sex_comboBox.setEnabled(estado)
        self.ui.menores_checkBox.setEnabled(estado)

    def configurar_ventana_cliente_nuevo(self):
        """Configura la interfaz para la creación de un nuevo cliente."""
        self.ui.boton_izquierdo_pushButton.setText("Limpiar")
        self.ui.boton_derecho_pushButton.setText("Guardar")
        self.establece_fecha_interface()
        self.ui.boton_izquierdo_pushButton.clicked.connect(
            self._limpiar_campos_cliente_nuevo
        )
        self.ui.boton_derecho_pushButton.clicked.connect(self._guardar_cliente_nuevo)

    def _guardar_cliente_nuevo(self):
        """Guarda un nuevo cliente en la base de datos."""
        pass

    def __llenar_combox_sexo(self):
        """Llena el comboBox de selección de sexo."""
        self.ui.sex_comboBox.addItems(["Hombre", "Mujer", "Otro"])

    def seleccionar_sexo(self, sexo):
        """Selecciona el sexo en el comboBox basado en el valor almacenado."""
        opciones = {"H": "Hombre", "M": "Mujer", "O": "Otro"}
        self.ui.sex_comboBox.setCurrentText(opciones.get(sexo, "Otro"))

    def obtener_sexo_seleccionado(self):
        """Devuelve el valor seleccionado en el comboBox de sexo."""
        opciones = {"Hombre": "H", "Mujer": "M", "Otro": "O"}
        return opciones.get(self.ui.sex_comboBox.currentText(), "O")

    def _limpiar_campos_cliente_nuevo(self):
        """Limpia los campos del formulario para un nuevo cliente."""
        self.ui.nombre_lineEdit.clear()
        self.ui.apellidos_lineEdit.clear()
        self.ui.dni_lineEdit.clear()
        self.establece_fecha_interface()
        self.ui.pais_lineEdit.clear()
        self.ui.telefono_lineEdit.clear()
        self.seleccionar_sexo("O")
        self.ui.mail_lineEdit.clear()
        self.ui.menores_checkBox.setChecked(False)

    def cargar_datos(self, cliente: Cliente):
        """Carga los datos de un cliente en la interfaz."""
        self.ui.nombre_lineEdit.setText(cliente.Nombre)
        self.ui.apellidos_lineEdit.setText(cliente.Apellidos)
        self.ui.dni_lineEdit.setText(cliente.Num_Identificacion)
        self.establece_fecha_interface(cliente.Fec_Nac)
        self.ui.pais_lineEdit.setText(cliente.Pais)
        self.ui.telefono_lineEdit.setText(cliente.Telefono)
        self.ui.mail_lineEdit.setText(cliente.email)
        self.seleccionar_sexo(cliente.Sexo)
        self.ui.menores_checkBox.setChecked(cliente.Menores)

    def establece_fecha_interface(self, fecha=None):
        """Establece la fecha en la interfaz."""
        fecha = fecha if fecha else QDate.currentDate()
        self.ui.fecha_dateEdit.setDate(fecha)
        self.ui.fecha_dateEdit.setMaximumDate(QDate.currentDate())
        self.ui.fecha_dateEdit.setCalendarPopup(True)
        self.ui.fecha_dateEdit.setDisplayFormat("yyyy-MM-dd")

    def _recoger_datos_cliente(self):
        return Cliente(
            Nombre=self.ui.nombre_lineEdit.text(),
            Apellidos=self.ui.apellidos_lineEdit.text(),
            Num_Identificacion=self.ui.dni_lineEdit.text(),
            Fec_Nac=self.ui.fecha_dateEdit.date(),
            Pais=self.ui.pais_lineEdit.text(),
            Telefono=self.ui.telefono_lineEdit.text(),
            email=self.ui.mail_lineEdit.text(),
            Sexo=self.obtener_sexo_seleccionado(),
            Menores=self.ui.menores_checkBox.isChecked(),
        )
