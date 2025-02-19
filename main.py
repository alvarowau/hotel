import sys
from PySide6.QtWidgets import QApplication
from controller.controller_login import LoginController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_controller = LoginController()
    login_controller.show()  # Muestra la ventana de login
    sys.exit(app.exec())