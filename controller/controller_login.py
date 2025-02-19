from PySide6.QtCore import QCoreApplication, QMetaObject
from PySide6.QtWidgets import QWidget, QMessageBox
from iu.iu_login import Ui_Form  # Importa la interfaz generada por Qt Designer

class LoginController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Conexiones de eventos
        self.ui.pushButton.clicked.connect(self.cerrar_ventana)  # Salir
        self.ui.pushButton_2.clicked.connect(self.loguear_usuario)  # Loguear

    def cerrar_ventana(self):
        self.close()  # Cierra la ventana de login

    def loguear_usuario(self):
        usuario = self.ui.lineEdit.text()
        contrasena = self.ui.lineEdit_2.text()

        # Validación básica (puedes mejorarla)
        if not usuario or not contrasena:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")
            return

        # Aquí iría la lógica de autenticación (ejemplo)
        if usuario == "admin" and contrasena == "password":  # Reemplaza con tu lógica real
            QMessageBox.information(self, "Éxito", "Usuario logueado correctamente.")
            # Abre la siguiente ventana o realiza las acciones necesarias
            # ...
        else:
            QMessageBox.critical(self, "Error", "Credenciales incorrectas.")



