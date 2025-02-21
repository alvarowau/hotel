from PySide6.QtWidgets import (
    QLineEdit,
    QMessageBox,
    QWidget,
)

from dao.user_dao import UserDao
from iu.iu_login import Ui_Form
from util.mostrar_mensajes import mostrar_advertencia, mostrar_informacion, mostrar_error


class LoginController(QWidget):
    """
    Controlador de la ventana de inicio de sesión.

    Se encarga de gestionar la interacción del usuario con la interfaz de login,
    validando las credenciales a través de `UserDao` y mostrando los mensajes
    correspondientes según el resultado.
    """

    def __init__(self, conexion):
        """
        Inicializa el controlador del login.

        :param conexion: Objeto de conexión a la base de datos.
        """
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.user_dao = UserDao(conexion)
        self.ui.lineEdit_2.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        self.ui.pushButton.clicked.connect(self.cerrar_ventana)
        self.ui.pushButton_2.clicked.connect(self.loguear_usuario)

    def cerrar_ventana(self):
        """
        Cierra la ventana de login.
        """
        self.close()

    def loguear_usuario(self):
        """
        Valida las credenciales ingresadas y muestra el resultado.

        Si las credenciales son correctas, muestra un mensaje de éxito;
        en caso contrario, muestra un mensaje de error.
        """
        usuario = self.ui.lineEdit.text().strip()
        password = self.ui.lineEdit_2.text().strip()

        if not usuario or not password:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")
            return

        if self.user_dao.login(username=usuario, password=password):
            mostrar_advertencia("Login correcto")
        else:
            mostrar_error("Credenciales incorrectas")
