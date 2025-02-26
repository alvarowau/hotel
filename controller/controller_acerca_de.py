import controller.imagenes_rc  

# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices
from iu.iu_acerca_de import Ui_a



class AcercaDeController(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_a()
        self.ui.setupUi(self)

        # Conecta el botón "Repositorio" a una función para abrir un enlace
        self.ui.pushButton.clicked.connect(self.abrir_repositorio)

    def abrir_repositorio(self):
        """
        Función para abrir un enlace al repositorio (ejemplo).
        Reemplaza 'URL_DEL_REPOSITORIO' con la URL real del repositorio.
        """
        url = QUrl(
            "https://github.com/usuario/repositorio_ejemplo"
        )  # Reemplazar con la URL real
        QDesktopServices.openUrl(url)


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication, QStackedWidget

    app = QApplication([])
    stacked_widget = QStackedWidget()

    # Crea una instancia del controlador
    acerca_de_controller = AcercaDeController()

    # Añade el controlador al stackedWidget
    stacked_widget.addWidget(acerca_de_controller)

    stacked_widget.setCurrentWidget(
        acerca_de_controller
    )  # Muestra este widget por defecto
    stacked_widget.setWindowTitle("Ejemplo de StackedWidget con Controller Acerca De")
    stacked_widget.show()

    app.exec()
