from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox


class MensajePersonalizado(QMessageBox):
    def __init__(
        self, titulo, mensaje, icono=None, detalles=None, mostrar_detalles=False
    ):
        """
        Inicializa un cuadro de mensaje personalizado con un diseño acorde a la interfaz.

        Args:
            titulo (str): El título del mensaje.
            mensaje (str): El texto principal del mensaje.
            icono (QMessageBox.Icon, opcional): Ícono a mostrar en el cuadro de mensaje.
            detalles (str, opcional): Detalles adicionales a mostrar en errores.
            mostrar_detalles (bool): Si es True, se muestra el botón "Hide Details...".
        """
        super().__init__()
        self.setWindowTitle(titulo)
        self.setText(f"<b>{mensaje}</b>")
        self.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.setDefaultButton(QMessageBox.StandardButton.Ok)

        # Estilos con colores personalizados para cada tipo de mensaje
        self.setStyleSheet(
            """
            QMessageBox {
                background-color: #121212;  /* Fondo oscuro */
                font-family: "Segoe UI", Arial, sans-serif;
                font-size: 14px;
                color: #E0E0E0;  /* Texto en gris claro */
                border: 2px solid #333333;
                border-radius: 8px;
            }
            QLabel {
                font-weight: bold;
                color: #E0E0E0;  /* Texto claro */
                font-size: 14px;
            }
            QPushButton {
                background-color: #6200EE;  /* Violeta para botones */
                color: #FFFFFF;
                border-radius: 8px;
                padding: 6px 12px;
                font-size: 14px;
                border: 2px solid #6200EE;
            }
            QPushButton:hover {
                background-color: #3700B3;
                border: 2px solid #3700B3;
            }
            QPushButton:pressed {
                background-color: #3100A0;
                border: 2px solid #3100A0;
            }
            /* Color para error */
            QMessageBox[critical="true"] {
                color: #D32F2F;  /* Rojo para errores */
            }
            QLabel[critical="true"] {
                color: #D32F2F;
            }
            QPushButton[critical="true"] {
                background-color: #D32F2F;
                color: #FFFFFF;
                border: 2px solid #D32F2F;
            }
            QPushButton[critical="true"]:hover {
                background-color: #B71C1C;
            }
            QPushButton[critical="true"]:pressed {
                background-color: #9A0007;
            }
            /* Color para advertencia */
            QMessageBox[warning="true"] {
                color: #FF9800;  /* Naranja para advertencias */
            }
            QLabel[warning="true"] {
                color: #FF9800;
            }
            QPushButton[warning="true"] {
                background-color: #FF9800;
                color: #FFFFFF;
                border: 2px solid #FF9800;
            }
            QPushButton[warning="true"]:hover {
                background-color: #F57C00;
            }
            QPushButton[warning="true"]:pressed {
                background-color: #E65100;
            }
        """
        )

        self.setIcon(icono if icono else QMessageBox.Icon.Information)

        if detalles and mostrar_detalles:
            self.setDetailedText(detalles)

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

    @staticmethod
    def mostrar(titulo, mensaje, icono=None, detalles=None, mostrar_detalles=False):
        """
        Muestra un cuadro de mensaje personalizado.

        Args:
            titulo (str): El título del mensaje.
            mensaje (str): El texto principal del mensaje.
            icono (QMessageBox.Icon, opcional): Ícono a mostrar en el cuadro de mensaje.
            detalles (str, opcional): Detalles adicionales a mostrar en errores.
            mostrar_detalles (bool): Si es True, se muestra el botón "Hide Details...".
        """
        dialogo = MensajePersonalizado(
            titulo, mensaje, icono, detalles, mostrar_detalles
        )
        dialogo.exec()


def mostrar_error(mensaje, detalles=None):
    """
    Muestra un cuadro de mensaje de error con opción de ver detalles.

    Args:
        mensaje (str): Mensaje de error a mostrar.
        detalles (str, opcional): Detalles adicionales del error.
    """
    MensajePersonalizado.mostrar(
        "Error",
        mensaje,
        QMessageBox.Icon.Critical,
        detalles,
        mostrar_detalles=True,
    )


def mostrar_informacion(mensaje):
    """
    Muestra un cuadro de mensaje de información sin detalles.

    Args:
        mensaje (str): Mensaje de información a mostrar.
    """
    MensajePersonalizado.mostrar("Información", mensaje, QMessageBox.Icon.Information)


def mostrar_advertencia(mensaje):
    """
    Muestra un cuadro de mensaje de advertencia sin opción de detalles.

    Args:
        mensaje (str): Mensaje de advertencia a mostrar.
    """
    MensajePersonalizado.mostrar("Advertencia", mensaje, QMessageBox.Icon.Warning)


def confirmar_eliminacion_usuario(mensaje):
    """
    Muestra un cuadro de diálogo de confirmación para eliminar un usuario.

    Returns:
        bool: True si el usuario confirma, False en caso contrario.
    """
    dialogo = QMessageBox()
    dialogo.setWindowTitle("Confirmación")
    dialogo.setText(mensaje)
    dialogo.setStandardButtons(
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
    )
    dialogo.setDefaultButton(QMessageBox.StandardButton.No)
    dialogo.setIcon(QMessageBox.Icon.Warning)
    return dialogo.exec() == QMessageBox.StandardButton.Yes
