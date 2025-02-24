from PySide6.QtCore import QDate
from PySide6.QtWidgets import QDialog

from dao.clientes_dao import ClienteDao
from iu.iu_clientes_edit import Ui_clientes_edit
from model.cliente import Cliente
from util.mostrar_mensajes import (
    confirmar_mensaje,
    mostrar_advertencia,
    mostrar_error,
    mostrar_informacion,
)


class ControladorClientesEdit(QDialog):
    """
    Controlador para la edición y creación de clientes.

    Esta clase maneja la lógica de la interfaz de usuario para la creación, edición y eliminación de clientes.
    Permite cargar datos de un cliente existente para su edición o preparar el formulario para la creación de un nuevo cliente.

    Attributes:
        conexion: Conexión a la base de datos.
        cliente_dao (ClienteDao): Objeto para interactuar con la capa de acceso a datos de clientes.
        cliente_edicion (Cliente | None): Cliente que se está editando, si es None, se está creando un nuevo cliente.
        id_cliente (int | None): ID del cliente que se está editando. Si es None, se está creando un nuevo cliente.
        ui (Ui_clientes_edit): Interfaz de usuario generada por Qt Designer.
    """

    def __init__(self, conexion, id_cliente=None):
        """
        Inicializa el controlador.

        Args:
            conexion: Conexión a la base de datos.
            id_cliente (int | None): ID del cliente que se está editando. Si es None, se está creando un nuevo cliente.
        """
        super().__init__()
        self.ui = Ui_clientes_edit()
        self.ui.setupUi(self)
        self.conexion = conexion
        self.cliente_dao = ClienteDao(self.conexion)
        self.__llenar_combox_sexo()
        self.cliente_edicion = None

        if id_cliente:
            self.id_cliente = id_cliente
            self.configurar_ventana_cliente_edicion()
        else:
            self.configurar_ventana_cliente_nuevo()

    def configurar_ventana_cliente_edicion(self):
        """
        Configura la interfaz para la edición de un cliente existente.

        Carga los datos del cliente en la interfaz y configura los botones para editar o eliminar.
        """
        self.setWindowTitle("Edicion")
        self.ui.title_label.setText("")
        self.semaforo_campos(False)
        self.cliente_edicion = self.cliente_dao.find_all_by_id(self.id_cliente)

        if self.cliente_edicion:
            self.ui.title_label.setText(
                f"saber más de {self.cliente_edicion.Nombre} {self.cliente_edicion.Apellidos}"
            )
            self.cargar_datos(self.cliente_edicion)
            self.ui.boton_izquierdo_pushButton.setText("Eliminar")
            self.ui.boton_derecho_pushButton.setText("Editar")
            self.ui.boton_izquierdo_pushButton.clicked.connect(self._eliminar_cliente)
            self.ui.boton_derecho_pushButton.clicked.connect(self._habilitar_edicion)

    def _habilitar_edicion(self):
        """
        Habilita la edición de los campos del cliente.

        Cambia el texto del botón derecho a "Guardar" y habilita los campos del formulario.
        """
        self.semaforo_campos(True)
        self.ui.boton_izquierdo_pushButton.setVisible(False)
        self.ui.boton_derecho_pushButton.setText("Guardar")
        self.ui.boton_derecho_pushButton.clicked.disconnect()
        self.ui.boton_derecho_pushButton.clicked.connect(self.guardar_edicion)

    def _es_edicion_posible(self, cliente_guardar) -> bool:
        """
        Verifica si es posible editar un cliente con base en el número de identificación.

        Args:
            cliente_guardar (Cliente): Cliente con los datos a guardar.

        Returns:
            bool: True si la edición es posible, False si el DNI ya existe.
        """
        if self.cliente_edicion:
            if (
                self.cliente_edicion.Num_Identificacion
                == cliente_guardar.Num_Identificacion
            ):
                return True
        return not self.cliente_dao.existe_numero_identificacion(
            cliente_guardar.Num_Identificacion
        )

    def guardar_edicion(self):
        """
        Guarda los cambios realizados en un cliente existente.

        Recoge los datos del formulario, valida si la edición es posible y guarda los cambios.
        """
        cliente_guardar = self._recoger_datos_cliente()
        if not cliente_guardar:
            mostrar_error("No se puede guardar")
            return

        cliente_guardar.Id = self.id_cliente

        if self._es_edicion_posible(cliente_guardar):
            self._guardar_cliente(cliente_guardar)
        else:
            mostrar_error("El DNI ya existe")

    def _guardar_cliente(self, cliente_guardar):
        """
        Guarda los datos de un cliente editado o creado.

        Args:
            cliente_guardar (Cliente): Cliente con los datos a guardar.
        """
        respuesta = self.cliente_dao.update(
            nombre=cliente_guardar.Nombre,
            apellidos=cliente_guardar.Apellidos,
            fec_nac=cliente_guardar._Fec_Nac.toString("yyyy-MM-dd"),
            pais=cliente_guardar.Pais,
            telefono=cliente_guardar.Telefono,
            email=cliente_guardar.email,
            sexo=cliente_guardar.Sexo,
            menores=cliente_guardar.Menores,
            numero_identificacion=cliente_guardar.Num_Identificacion,
            id=self.id_cliente,
        )
        if respuesta:
            mostrar_informacion("El cliente se guardó correctamente")
            self.accept()
            self.close()
        else:
            mostrar_error("No se ha podido guardar")

    def _eliminar_cliente(self):
        """
        Elimina un cliente tras confirmación.

        Muestra un mensaje de confirmación y, si el usuario acepta, elimina el cliente.
        """
        nombre_completo = self.cliente_dao.find_nombre_by_id(self.id_cliente)
        mensaje = f"¿Está seguro que desea eliminar el cliente {nombre_completo}?"
        if confirmar_mensaje(mensaje):
            if self.cliente_dao.deactivate(self.id_cliente):
                mostrar_informacion(f"El cliente {nombre_completo} ha sido eliminado")
            else:
                mostrar_error(f"No se pudo eliminar el cliente {nombre_completo}")
        self.accept()

    def semaforo_campos(self, estado):
        """
        Habilita o deshabilita los campos de la interfaz.

        Args:
            estado (bool): True para habilitar los campos, False para deshabilitarlos.
        """
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
        """
        Configura la interfaz para la creación de un nuevo cliente.

        Prepara el formulario para la creación de un nuevo cliente y configura los botones.
        """
        self.setWindowTitle("Crear Nuevo")
        self.ui.boton_izquierdo_pushButton.setText("Limpiar")
        self.ui.boton_derecho_pushButton.setText("Guardar")
        self.establece_fecha_interface()
        self.ui.boton_izquierdo_pushButton.clicked.connect(
            self._limpiar_campos_cliente_nuevo
        )
        self.ui.boton_derecho_pushButton.clicked.connect(self._creacion_cliente)

    def _creacion_cliente(self):
        """
        Crea un nuevo cliente.

        Recoge los datos del formulario, valida que no haya campos vacíos y crea el cliente.
        """
        cliente_creacion = self._recoger_datos_cliente()
        if not cliente_creacion:
            mostrar_error("Debe completar todos los campos")
            return

        cliente_creacion.Fec_Nac = cliente_creacion._Fec_Nac.toString("yyyy-MM-dd")
        if self.cliente_dao.create(cliente_creacion):
            mostrar_advertencia("El cliente se creó satisfactoriamente")
            self.accept()
            self.close()
        else:
            mostrar_error("Hubo un problema, no se pudo crear el cliente")

    def __llenar_combox_sexo(self):
        """
        Llena el comboBox de selección de sexo.

        Agrega las opciones "Hombre", "Mujer" y "Otro" al comboBox.
        """
        self.ui.sex_comboBox.addItems(["Hombre", "Mujer", "Otro"])

    def seleccionar_sexo(self, sexo):
        """
        Selecciona el sexo en el comboBox basado en el valor almacenado.

        Args:
            sexo (str): Valor del sexo almacenado ("H", "M" o "O").
        """
        opciones = {"H": "Hombre", "M": "Mujer", "O": "Otro"}
        self.ui.sex_comboBox.setCurrentText(opciones.get(sexo, "Otro"))

    def obtener_sexo_seleccionado(self):
        """
        Devuelve el valor seleccionado en el comboBox de sexo.

        Returns:
            str: Valor del sexo seleccionado ("H", "M" o "O").
        """
        opciones = {"Hombre": "H", "Mujer": "M", "Otro": "O"}
        return opciones.get(self.ui.sex_comboBox.currentText(), "O")

    def _limpiar_campos_cliente_nuevo(self):
        """
        Limpia los campos del formulario para un nuevo cliente.

        Restablece todos los campos del formulario a sus valores por defecto.
        """
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
        """
        Carga los datos de un cliente en la interfaz.

        Args:
            cliente (Cliente): Cliente cuyos datos se cargarán en la interfaz.
        """
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
        """
        Establece la fecha en la interfaz.

        Args:
            fecha (QDate | None): Fecha a establecer. Si es None, se usa la fecha actual.
        """
        fecha = fecha or QDate.currentDate()
        self.ui.fecha_dateEdit.setDate(fecha)
        self.ui.fecha_dateEdit.setMaximumDate(QDate.currentDate())
        self.ui.fecha_dateEdit.setCalendarPopup(True)
        self.ui.fecha_dateEdit.setDisplayFormat("yyyy-MM-dd")

    def is_campo_vacio(self, texto):
        """
        Verifica si el texto proporcionado está vacío o contiene solo espacios.

        Args:
            texto (str): Texto a verificar.

        Returns:
            bool: True si el texto está vacío o contiene solo espacios, False en caso contrario.
        """
        return not texto.strip()

    def _recoger_datos_cliente(self) -> Cliente | None:
        """
        Recoge los datos del formulario y valida que no haya campos vacíos críticos.

        Returns:
            Cliente | None: Objeto Cliente con los datos recogidos, o None si hay campos vacíos.
        """
        nombre = self.ui.nombre_lineEdit.text()
        apellidos = self.ui.apellidos_lineEdit.text()
        dni = self.ui.dni_lineEdit.text()
        pais = self.ui.pais_lineEdit.text()
        telefono = self.ui.telefono_lineEdit.text()
        email = self.ui.mail_lineEdit.text()

        if any(
            map(self.is_campo_vacio, [nombre, apellidos, dni, pais, telefono, email])
        ):
            return None

        return Cliente(
            Nombre=nombre,
            Apellidos=apellidos,
            Num_Identificacion=dni,
            Fec_Nac=self.ui.fecha_dateEdit.date(),
            Pais=pais,
            Telefono=telefono,
            email=email,
            Sexo=self.obtener_sexo_seleccionado(),
            Menores=self.ui.menores_checkBox.isChecked(),
        )
