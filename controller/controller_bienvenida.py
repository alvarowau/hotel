# Importaciones necesarias para el Widget de Bienvenida
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor, QFont, QLinearGradient, QPalette
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class BienvenidaWidget(QWidget):
    """
    Widget que muestra un mensaje de bienvenida atractivo y estilizado.

    Este widget Qt crea una interfaz de usuario para dar la bienvenida
    a los usuarios del sistema de gestión hotelera.  Incluye un mensaje
    principal y un subtítulo, ambos centrados y con estilos de fuente
    específicos.  Además, aplica un fondo con un degradado de color
    para mejorar la apariencia visual.
    """

    def __init__(self):
        """
        Inicializa el Widget de Bienvenida.

        Configura la interfaz de usuario básica llamando a `_configurar_ui()`
        y aplica los estilos visuales definidos en `_configurar_estilos()`.
        """
        super().__init__()
        self._configurar_ui()
        self._configurar_estilos()

    def _configurar_ui(self):
        """
        Configura la interfaz del widget de bienvenida.

        Crea y organiza los elementos de la interfaz de usuario, que incluyen:
            - Un `QLabel` para el mensaje de bienvenida principal.
            - Un `QLabel` para el subtítulo.
            - Un `QVBoxLayout` para organizar verticalmente los elementos y el espaciado.

        El mensaje principal se establece con una fuente Arial de tamaño 20 y en negrita,
        y el subtítulo con Arial de tamaño 14 en estilo normal. Ambos textos se centran
        en el widget.
        """
        layout = QVBoxLayout(self)

        # Mensaje principal
        mensaje_bienvenida = QLabel("¡Bienvenido al Sistema de Gestión Hotelera!")
        mensaje_bienvenida.setAlignment(Qt.AlignCenter)  # type: ignore
        mensaje_bienvenida.setFont(QFont("Arial", 20, QFont.Bold))  # type: ignore

        # Subtítulo
        mensaje_subtitulo = QLabel("Administra tu hotel de manera fácil y eficiente.")
        mensaje_subtitulo.setAlignment(Qt.AlignCenter)  # type: ignore
        mensaje_subtitulo.setFont(QFont("Arial", 14, QFont.Normal))  # type: ignore

        # Agregar los elementos al layout
        layout.addStretch()
        layout.addWidget(mensaje_bienvenida)
        layout.addWidget(mensaje_subtitulo)
        layout.addStretch()

        self.setLayout(layout)

    def _configurar_estilos(self):
        """
        Aplica estilos al widget, incluyendo un fondo con degradado.

        Define y aplica estilos visuales al widget `BienvenidaWidget`.
        Actualmente, configura un fondo con un degradado lineal vertical
        que va desde un azul vibrante hasta un azul celeste.  Este degradado
        se establece como el pincel de fondo de la paleta de colores del widget.
        """
        # Crear un degradado de color como fondo
        palette = QPalette()
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0.0, QColor(30, 144, 255))  # Azul vibrante
        gradient.setColorAt(1.0, QColor(0, 191, 255))  # Azul celeste

        palette.setBrush(QPalette.Window, QBrush(gradient))  # type: ignore
        self.setAutoFillBackground(True)
        self.setPalette(palette)
