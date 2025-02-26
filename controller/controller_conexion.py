from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog

from bbdd.comprobar_conexion import ComprobadorMySQL
from iu.iu_conexion import Ui_conexion
from util.mostrar_mensajes import mostrar_error, mostrar_informacion


class ConexionController(QDialog):
    """Controlador de la configuración de la base de datos.

    Este controlador gestiona la interfaz de usuario para configurar la conexión
    a una base de datos MySQL. Permite al usuario ingresar los datos de conexión,
    probar la conexión y, si es exitosa, enviar la configuración para ser utilizada
    por la aplicación.

    Signals:
        configuracion_finalizada (Signal(dict)): Señal emitida cuando la configuración
                                                  de la conexión se ha finalizado y se
                                                  envían los datos de conexión.
    """

    configuracion_finalizada = Signal(dict)  # Señal para enviar datos de conexión

    def __init__(self, datos_conexion):
        """Inicializa el controlador de conexión.

        Crea una instancia de `ConexionController`, configura la interfaz de usuario
        cargada desde `iu_conexion.Ui_conexion`, guarda los datos de conexión iniciales,
        inicializa la interfaz de usuario y llena los campos del formulario con los datos
        de conexión proporcionados.

        Args:
            datos_conexion (dict): Diccionario con los datos de conexión iniciales
                                     (host, user, password, database, port).
        """
        super().__init__()
        self.ui = Ui_conexion()
        self.ui.setupUi(self)
        self.datos_conexion = datos_conexion
        self._inicializar_ui()
        self._llenar_campos()

    def _inicializar_ui(self):
        """Inicializa elementos específicos de la interfaz de usuario.

        Oculta el botón "Conectar" inicialmente y conecta la señal del botón
        "Probar Conexión" a la función `_probar_conexion`.
        """
        self.ui.pushButton_conectar.setVisible(False)
        self.ui.pushButton_probar.clicked.connect(self._probar_conexion)

    def _llenar_campos(self):
        """Llena los campos de los QLineEdit con los datos de conexión.

        Utiliza los datos de conexión almacenados en `self.datos_conexion`
        para rellenar los campos de texto de la interfaz de usuario, permitiendo
        al usuario ver y, opcionalmente, editar la configuración actual.
        """
        self.ui.lineEdit_host.setText(self.datos_conexion["host"])
        self.ui.lineEdit_user.setText(self.datos_conexion["user"])
        self.ui.lineEdit_pass.setText(self.datos_conexion["password"])
        self.ui.lineEdit_db.setText(self.datos_conexion["database"])
        self.ui.lineEdit_port.setText(self.datos_conexion["port"])

    def obtener_datos(self):
        """Obtiene los datos ingresados por el usuario desde la interfaz.

        Recoge los valores de texto de cada campo de entrada en la interfaz de usuario
        (host, user, password, database, port), elimina los espacios en blanco al inicio
        y al final de cada valor, y los retorna en un diccionario.

        Returns:
            dict: Diccionario con los datos de conexión ingresados por el usuario, con las claves:
                  'host', 'user', 'password', 'database', 'port'.
        """
        return {
            "host": self.ui.lineEdit_host.text().strip(),
            "user": self.ui.lineEdit_user.text().strip(),
            "password": self.ui.lineEdit_pass.text().strip(),
            "database": self.ui.lineEdit_db.text().strip(),
            "port": self.ui.lineEdit_port.text().strip(),
        }

    def validar_campos(self, datos):
        """Valida que los campos de conexión no estén vacíos.

        Verifica que ninguno de los valores en el diccionario de datos de conexión
        sea `None` o una cadena vacía.

        Args:
            datos (dict): Diccionario con los datos de conexión a validar.

        Returns:
            bool: `True` si todos los campos contienen un valor no vacío, `False` si alguno está vacío.
        """
        return all(valor not in [None, ""] for valor in datos.values())

    def _probar_conexion(self):
        """Prueba la conexión a la base de datos utilizando los datos ingresados.

        Llama a `_comprobar_conexion` para intentar establecer una conexión
        con los parámetros actuales. Si la conexión es exitosa, muestra un mensaje
        de éxito, hace visible el botón "Conectar", oculta el botón "Probar Conexión"
        y conecta el botón "Conectar" a la función `enviar_datos`. Si la conexión falla,
        muestra un mensaje de error.
        """
        if self._comprobar_conexion():
            mostrar_informacion("La conexión ha sido efectuada")
            self.ui.pushButton_conectar.setVisible(True)
            self.ui.pushButton_probar.setVisible(False)
            self.ui.pushButton_conectar.clicked.connect(self.enviar_datos)
        else:
            mostrar_error("No se ha podido establecer la conexión")

    def enviar_datos(self):
        """Emite una señal para enviar los datos de conexión y cierra el diálogo.

        Emite la señal `configuracion_finalizada` con los datos de conexión validados
        y probados exitosamente (almacenados en `self.datos_conexion_true`). Luego,
        acepta el diálogo, cerrándolo.
        """
        # Utiliza self.datos_conexion_true en lugar de self.datos_conexion
        self.configuracion_finalizada.emit(self.datos_conexion_true)
        self.accept()

    def _comprobar_conexion(self):
        """Verifica la conexión a la base de datos utilizando ComprobadorMySQL.

        Crea una instancia de `ComprobadorMySQL`, obtiene los datos de conexión
        actuales utilizando `obtener_datos()`, y utiliza `ComprobadorMySQL.comprobar_conexion()`
        para verificar la conexión. Si la conexión es exitosa, guarda los datos de conexión
        en `self.datos_conexion_true` y retorna `True`. Si falla, retorna `False`.

        Returns:
            bool: `True` si la conexión se estableció correctamente, `False` en caso contrario.
        """
        comprobador = ComprobadorMySQL()
        dict_conexion = self.obtener_datos()
        respuesta = comprobador.comprobar_conexion(**dict_conexion)
        if respuesta:
            self.datos_conexion_true = dict_conexion
            return True
        else:
            return False
