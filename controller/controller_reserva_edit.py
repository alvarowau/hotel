from PySide6.QtWidgets import QWidget

from iu.iu_reserva_edit import Ui_reserva_edit
from util.mostrar_mensajes import mostrar_advertencia, mostrar_error, mostrar_informacion


class ControladorReservas(QWidget):
    """
    Controlador para la interfaz de gestión de reservas.
    Maneja eventos y validaciones dentro del formulario de reservas.
    """

    def __init__(self, conexion, cliente_id = None):
        
            super().__init__()  # Inicializa el QDialog
            self.ui = Ui_reserva_edit()  # Instancia de la interfaz de usuario
            self.ui.setupUi(self)  # Configura la UI

