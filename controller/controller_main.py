from PySide6.QtWidgets import QMainWindow

from controller.controller_acerca_de import AcercaDeController
from controller.controller_clientes import ClientesController
from controller.controller_documentacion import ReadMeController
from controller.controller_bienvenida import BienvenidaWidget
from controller.controller_reservas import ReservasController
from iu.iu_main_windows import Ui_HOTEL


class MainController(QMainWindow):
    """Controlador principal que gestiona la ventana principal y los cambios de vista."""

    def __init__(self, conexion):
        super().__init__()
        self.ui = Ui_HOTEL()
        self.conexion = conexion
        self.ui.setupUi(self)

        # Controladores de las vistas
        self.clientes_controller = ClientesController(self.conexion)
        self.reserva_controller = ReservasController(self.conexion)
        self.acerca_de_controller = AcercaDeController()

        # Crear el controlador y cargar el archivo README
        self.readme_controller = ReadMeController(self)
        self.readme_controller.load_readme("README.md")  # Cargar el archivo README

        # Crear el Widget de Bienvenida
        self.bienvenida_widget = BienvenidaWidget()

        # Agregar las vistas al QStackedWidget
        self.ui.stackedWidget.addWidget(self.bienvenida_widget)  # Widget de Bienvenida
        self.ui.stackedWidget.addWidget(self.clientes_controller)  # Vista de clientes
        self.ui.stackedWidget.addWidget(self.reserva_controller)  # Vista de reservas
        self.ui.stackedWidget.addWidget(self.acerca_de_controller)  # Vista "Acerca de"
        self.ui.stackedWidget.addWidget(self.readme_controller)  # Vista del README

        # Conectar las acciones de menú a las funciones que cambian de vista
        self.ui.actionReserva.triggered.connect(self.mostrar_clientes)
        self.ui.actionReservar.triggered.connect(self.mostrar_reservas)
        self.ui.actionAcerca_de.triggered.connect(self.mostrar_acerca_de)
        self.ui.actionDocumentaci_n.triggered.connect(self.mostrar_readme)

        # Mostrar el Widget de Bienvenida al inicio
        self.mostrar_bienvenida()

    def mostrar_bienvenida(self):
        """Cambia la vista al widget de bienvenida."""
        self.ui.stackedWidget.setCurrentWidget(self.bienvenida_widget)

    def mostrar_clientes(self):
        """Cambia la vista a la ventana de clientes dentro del QStackedWidget."""
        self.ui.stackedWidget.setCurrentWidget(self.clientes_controller)

    def mostrar_reservas(self):
        """Cambia la vista a la ventana de reservas dentro del QStackedWidget."""
        self.ui.stackedWidget.setCurrentWidget(self.reserva_controller)

    def mostrar_acerca_de(self):
        """Cambia la vista a la ventana 'Acerca de' dentro del QStackedWidget."""
        self.ui.stackedWidget.setCurrentWidget(self.acerca_de_controller)

    def mostrar_readme(self):
        """Cambia la vista a la ventana del README."""
        self.ui.stackedWidget.setCurrentWidget(
            self.readme_controller
        )  # Función para mostrar el README
