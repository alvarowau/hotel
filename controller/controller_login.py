from PySide6.QtWidgets import (
    QLineEdit,  # Import necesario para setEchoMode
    QMessageBox,
    QWidget,
)

from dao.user_dao import UserDao
from iu.iu_login import Ui_Form
from util.mostrar_mensajes import mostrar_advertencia, mostrar_error


class LoginController(QWidget):
    def __init__(self, conexion):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.user_dao = UserDao(conexion)
        self.ui.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)

        # Conexiones de eventos
        self.ui.pushButton.clicked.connect(self.cerrar_ventana)  # Salir
        self.ui.pushButton_2.clicked.connect(self.loguear_usuario)  # Loguear

    def cerrar_ventana(self):
        self.close()  # Cierra la ventana de login

    def loguear_usuario(self):
        usuario = self.ui.lineEdit.text().strip()
        password = self.ui.lineEdit_2.text().strip()

        if not usuario or not password:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")
            return

        if self.user_dao.login(username=usuario, password=password):
            mostrar_advertencia("Login correcto", "Puede acceder")
        else:
            mostrar_error(
                "Login incorrecto", "El usuario o la contraseña no son válidos"
            )
