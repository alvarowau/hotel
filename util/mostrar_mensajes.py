from PySide6.QtWidgets import QMessageBox


class MensajePersonalizado(QMessageBox):
    def __init__(self, titulo, mensaje, icono=None, detalles=None):
        """
        Inicializa un cuadro de mensaje personalizado.

        Args:
            titulo (str): El título del mensaje.
            mensaje (str): El texto principal del mensaje.
            icono (QMessageBox.Icon, opcional): El ícono a mostrar en el cuadro de mensaje. Por defecto es Information.
            detalles (str, opcional): Detalles adicionales que se muestran al expandir el mensaje.
        """
        super().__init__()
        self.setWindowTitle(titulo)
        self.setText(f"<b>{mensaje}</b>")
        self.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.setDefaultButton(QMessageBox.StandardButton.Ok)

        self.setStyleSheet(
            """
            QMessageBox {
                background-color: #F8F9FA;
                font-family: "Segoe UI", Arial, sans-serif;
                font-size: 14px;
                color: #333333;
                border: 2px solid #CCCCCC;
                border-radius: 8px;
            }
            QLabel {
                font-weight: bold;
                color: #2A9D8F;
                font-size: 14px;
            }
            QPushButton {
                background-color: #2A9D8F;
                color: #FFFFFF;
                border-radius: 8px;
                padding: 6px 12px;
                font-size: 14px;
                border: 2px solid #2A9D8F;
            }
            QPushButton:hover {
                background-color: #A4C639;
                border: 2px solid #A4C639;
            }
            QPushButton:pressed {
                background-color: #207567;
                border: 2px solid #207567;
            }
        """
        )

        self.setIcon(icono if icono else QMessageBox.Icon.Information)

        if detalles:
            self.setDetailedText(detalles)

    @staticmethod
    def mostrar(titulo, mensaje, icono=None, detalles=None):
        """
        Muestra un cuadro de mensaje personalizado.

        Args:
            titulo (str): El título del mensaje.
            mensaje (str): El texto principal del mensaje.
            icono (QMessageBox.Icon, opcional): El ícono a mostrar en el cuadro de mensaje. Por defecto es Information.
            detalles (str, opcional): Detalles adicionales que se muestran al expandir el mensaje.
        """
        dialogo = MensajePersonalizado(titulo, mensaje, icono, detalles)
        dialogo.exec()


def mostrar_error(mensaje, detalles=None):
    """
    Muestra un cuadro de mensaje de error.

    Args:
        mensaje (str): El mensaje de error a mostrar.
        detalles (str, opcional): Detalles adicionales del error.
    """
    MensajePersonalizado.mostrar("Error", mensaje, QMessageBox.Icon.Critical, detalles)


def mostrar_informacion(mensaje, detalles=None):
    """
    Muestra un cuadro de mensaje de información.

    Args:
        mensaje (str): El mensaje de información a mostrar.
        detalles (str, opcional): Detalles adicionales de la información.
    """
    MensajePersonalizado.mostrar(
        "Información", mensaje, QMessageBox.Icon.Information, detalles
    )


def mostrar_advertencia(mensaje, detalles=None):
    """
    Muestra un cuadro de mensaje de advertencia.

    Args:
        mensaje (str): El mensaje de advertencia a mostrar.
        detalles (str, opcional): Detalles adicionales de la advertencia.
    """
    MensajePersonalizado.mostrar(
        "Advertencia", mensaje, QMessageBox.Icon.Warning, detalles
    )
