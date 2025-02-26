import controller.imagenes_rc  

# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices
from iu.iu_acerca_de import Ui_a


class AcercaDeController(QWidget):
    """
    Controlador para la ventana "Acerca De".

    Esta clase gestiona la lógica y la interacción de la interfaz de usuario
    de la ventana "Acerca De", que muestra información sobre la aplicación.
    """

    def __init__(self, parent=None):
        """
        Inicializa el controlador "Acerca De".

        Crea una instancia de `AcercaDeController`, configura la interfaz de usuario
        cargada desde el archivo `iu_acerca_de.Ui_a` y conecta los eventos
        de los widgets (en este caso, el botón "Repositorio").

        Args:
            parent (QWidget, optional): Widget padre del controlador. Por defecto None.
        """
        super().__init__(parent)
        self.ui = Ui_a()
        self.ui.setupUi(self)

        # Conecta el botón "Repositorio" a la función `abrir_repositorio`
        self.ui.pushButton.clicked.connect(self.abrir_repositorio)

    def abrir_repositorio(self):
        """
        Abre el navegador web con la URL del repositorio del proyecto.

        Utiliza `QDesktopServices.openUrl` para abrir la URL especificada
        en el navegador web predeterminado del sistema operativo.

        Raises:
            Ninguna excepción se lanza explícitamente, pero `QDesktopServices.openUrl`
            podría fallar si no hay un navegador web configurado o si la URL es inválida.

        Examples:
            Para abrir el repositorio del proyecto (ejemplo con una URL ficticia):

            >>> controller = AcercaDeController() # Crear instancia del controlador
            >>> controller.abrir_repositorio()    # Llamar a la función para abrir el repo
            # (Esto abriría "https://github.com/alvarowau/hotel" en el navegador)
        """
        url = QUrl(
            "https://github.com/alvarowau/hotel"
        )
        QDesktopServices.openUrl(url)


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication, QStackedWidget

    app = QApplication([])
    stacked_widget = QStackedWidget()

    # Crea una instancia del controlador "Acerca De"
    acerca_de_controller = AcercaDeController()

    # Añade el controlador al StackedWidget
    stacked_widget.addWidget(acerca_de_controller)

    stacked_widget.setCurrentWidget(
        acerca_de_controller
    )  # Muestra este widget por defecto
    stacked_widget.setWindowTitle("Ejemplo de StackedWidget con Controller Acerca De")
    stacked_widget.show()

    app.exec()
