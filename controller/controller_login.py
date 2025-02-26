from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLineEdit, QMessageBox, QWidget

from dao.user_dao import UserDao
from iu.iu_login import Ui_Loguin
from util.mostrar_mensajes import mostrar_error


class LoginController(QWidget):
    """
    Controlador de la ventana de inicio de sesión.

    Se encarga de gestionar la interacción del usuario con la interfaz de login,
    validando las credenciales a través de `UserDao` y mostrando los mensajes
    correspondientes según el resultado.

    Signals:
        login_exitoso (Signal): Señal emitida cuando el inicio de sesión es exitoso.
    """

    login_exitoso = Signal()

    def __init__(self, conexion):
        """
        Inicializa el controlador del login.

        Configura la interfaz de usuario cargada desde `iu_login.Ui_Loguin`,
        establece el modo de eco de la contraseña para ocultar la entrada,
        inicializa el `UserDao` con la conexión a la base de datos, y conecta
        los botones "Cerrar" y "Iniciar Sesión" a sus respectivas funciones.

        Args:
            conexion: Objeto de conexión a la base de datos.
        """
        super().__init__()
        self.ui = Ui_Loguin()
        self.ui.setupUi(self)
        self.user_dao = UserDao(conexion)
        self.ui.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)

        self.ui.pushButton.clicked.connect(self.cerrar_ventana)
        self.ui.pushButton_2.clicked.connect(self.loguear_usuario)

    def cerrar_ventana(self):
        """
        Cierra la ventana de login.

        Simplemente cierra la ventana actual del controlador de login.
        """
        self.close()

    def loguear_usuario(self):
        """
        Valida las credenciales ingresadas y muestra el resultado.

        Obtiene el usuario y la contraseña desde los campos de entrada de la interfaz,
        verifica si ambos campos están completos. Si faltan campos, muestra un mensaje
        de advertencia. Si los campos están completos, utiliza `UserDao.login()` para
        validar las credenciales contra la base de datos. En caso de éxito, emite la señal
        `login_exitoso` y cierra la ventana de login. En caso de fallo en la autenticación,
        muestra un mensaje de error indicando credenciales incorrectas.
        """
        usuario = self.ui.lineEdit.text().strip()
        password = self.ui.lineEdit_2.text().strip()

        if not usuario or not password:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")
            return

        if self.user_dao.login(username=usuario, password=password):
            self.login_exitoso.emit()
            self.close()
        else:
            mostrar_error("Credenciales incorrectas")
