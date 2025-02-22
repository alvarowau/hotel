from PySide6.QtWidgets import QMainWindow

from controller.clientes_controller import ClientesController
from controller.reservas_controller import ReservasControler
from iu.iu_main_windows import Ui_HOTEL


class MainController(QMainWindow):
    """Controlador principal que gestiona la ventana principal y los cambios de vista."""

    def __init__(self, conexion):
        super().__init__()
        self.ui = Ui_HOTEL()
        self.ui.setupUi(self)
        self.conexion = conexion

        # Controladores de las vistas
        self.clientes_controller = ClientesController(self.conexion)
        self.reserva_controller = ReservasControler(self.conexion)

        # Agregar las vistas al QStackedWidget
        self.ui.stackedWidget.addWidget(self.clientes_controller)
        self.ui.stackedWidget.addWidget(
            self.reserva_controller
        )  # Agregar vista de reservas

        # Conectar eventos del menú
        self.ui.actionClientes.triggered.connect(self.mostrar_clientes)
        self.ui.actionReservar.triggered.connect(
            self.mostrar_reservas
        )  # Agregar acción para reservas

    def mostrar_clientes(self):
        """Cambia la vista a la ventana de clientes dentro del QStackedWidget."""
        self.ui.stackedWidget.setCurrentWidget(self.clientes_controller)

    def mostrar_reservas(self):
        """Cambia la vista a la ventana de reservas dentro del QStackedWidget."""
        self.ui.stackedWidget.setCurrentWidget(self.reserva_controller)
