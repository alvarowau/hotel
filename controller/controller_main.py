from PySide6.QtWidgets import QMainWindow

from controller.controller_acerca_de import AcercaDeController
from controller.controller_clientes import ClientesController
from controller.controller_documentacion import ReadMeController
from controller.controller_bienvenida import BienvenidaWidget
from controller.controller_reservas import ReservasController
from iu.iu_main_windows import Ui_HOTEL


class MainController(QMainWindow):
    """Controlador principal que gestiona la ventana principal y los cambios de vista.

    Este controlador coordina la interfaz de usuario principal de la aplicación hotelera.
    Gestiona la inicialización de la ventana principal, la creación e integración de
    los controladores para las diferentes vistas (clientes, reservas, acerca de, documentación),
    y la lógica para cambiar entre estas vistas en respuesta a las acciones del usuario
    a través del menú principal.  Utiliza un `QStackedWidget` para gestionar las diferentes vistas.
    """

    def __init__(self, conexion):
        """Inicializa el controlador principal de la aplicación.

        Crea una instancia de `MainController`, configura la interfaz de usuario principal
        cargada desde `iu_main_windows.Ui_HOTEL`, almacena la conexión a la base de datos,
        inicializa los controladores para las diferentes vistas (clientes, reservas, acerca de, README),
        carga el contenido del archivo README, crea el widget de bienvenida, añade todas las vistas
        al `QStackedWidget` para la gestión de vistas, y conecta las acciones del menú principal
        a las funciones correspondientes para cambiar de vista.  Finalmente, muestra la vista de bienvenida
        al inicio de la aplicación.

        Args:
            conexion: Objeto de conexión a la base de datos que se utilizará en los controladores
                      que requieran acceso a datos (como `ClientesController` y `ReservasController`).
        """
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
        """Cambia la vista al widget de bienvenida.

        Establece el `bienvenida_widget` como el widget actual visible en el `QStackedWidget`,
        mostrando así la vista de bienvenida al usuario.
        """
        self.ui.stackedWidget.setCurrentWidget(self.bienvenida_widget)

    def mostrar_clientes(self):
        """Cambia la vista a la ventana de clientes dentro del QStackedWidget.

        Establece el `clientes_controller` como el widget actual visible en el `QStackedWidget`,
        mostrando la interfaz para la gestión de clientes.
        """
        self.ui.stackedWidget.setCurrentWidget(self.clientes_controller)

    def mostrar_reservas(self):
        """Cambia la vista a la ventana de reservas dentro del QStackedWidget.

        Establece el `reserva_controller` como el widget actual visible en el `QStackedWidget`,
        mostrando la interfaz para la gestión de reservas.
        """
        self.ui.stackedWidget.setCurrentWidget(self.reserva_controller)

    def mostrar_acerca_de(self):
        """Cambia la vista a la ventana 'Acerca de' dentro del QStackedWidget.

        Establece el `acerca_de_controller` como el widget actual visible en el `QStackedWidget`,
        mostrando la vista con información sobre la aplicación "Acerca de".
        """
        self.ui.stackedWidget.setCurrentWidget(self.acerca_de_controller)

    def mostrar_readme(self):
        """Cambia la vista a la ventana del README.

        Establece el `readme_controller` como el widget actual visible en el `QStackedWidget`,
        mostrando la documentación del proyecto cargada desde el archivo README.md.
        """
        self.ui.stackedWidget.setCurrentWidget(
            self.readme_controller
        )  # Función para mostrar el README
