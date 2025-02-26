# Importaciones necesarias para el Widget de Bienvenida
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor, QFont, QLinearGradient, QPalette
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class BienvenidaWidget(QWidget):
    """Widget que muestra un mensaje de bienvenida atractivo y estilizado."""

    def __init__(self):
        super().__init__()
        self._configurar_ui()
        self._configurar_estilos()

    def _configurar_ui(self):
        """Configura la interfaz del widget de bienvenida."""
        layout = QVBoxLayout(self)

        # Mensaje principal
        mensaje_bienvenida = QLabel("¡Bienvenido al Sistema de Gestión Hotelera!")
        mensaje_bienvenida.setAlignment(Qt.AlignCenter)
        mensaje_bienvenida.setFont(QFont("Arial", 20, QFont.Bold))

        # Subtítulo
        mensaje_subtitulo = QLabel("Administra tu hotel de manera fácil y eficiente.")
        mensaje_subtitulo.setAlignment(Qt.AlignCenter)
        mensaje_subtitulo.setFont(QFont("Arial", 14, QFont.Normal))

        # Agregar los elementos al layout
        layout.addStretch()
        layout.addWidget(mensaje_bienvenida)
        layout.addWidget(mensaje_subtitulo)
        layout.addStretch()

        self.setLayout(layout)

    def _configurar_estilos(self):
        """Aplica estilos al widget, incluyendo un fondo con degradado."""
        # Crear un degradado de color como fondo
        palette = QPalette()
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0.0, QColor(30, 144, 255))  # Azul vibrante
        gradient.setColorAt(1.0, QColor(0, 191, 255))  # Azul celeste

        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setAutoFillBackground(True)
        self.setPalette(palette)
