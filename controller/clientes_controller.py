from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import (
    QHeaderView,
    QTableView,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QHBoxLayout,
)
from dao.clientes_dao import ClienteDao


class ClientesController(QWidget):
    """Controlador de la vista de clientes."""

    def __init__(self, conexion):
        super().__init__()
        self.iniciar_tabla()
        self.conexion = conexion
        self.clientes_dao = ClienteDao(self.conexion)
        self.lista_clientes = (
            self.clientes_dao.find_all_activos()
        )  # Obtener los clientes de la base de datos
        self.iniciar_interface()
        self.llenar_datos()  # Llenar la tabla con los datos obtenidos

    def iniciar_interface(self):
        self.nueva_button = QPushButton("Nueva")
        self.modificar_button = QPushButton("Modificar")
        self.eliminar_button = QPushButton("Eliminar")
        self.salir_button = QPushButton("Salir")
        self.nueva_button.clicked.connect(self.agregar_cliente)
        self.modificar_button.clicked.connect(self.modificar_cliente)
        self.eliminar_button.clicked.connect(self.eliminar_cliente)
        self.salir_button.clicked.connect(self.salir)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.nueva_button)
        button_layout.addWidget(self.modificar_button)
        button_layout.addWidget(self.eliminar_button)
        button_layout.addWidget(self.salir_button)

        # Layout principal
        layout = QVBoxLayout(self)
        layout.addWidget(self.tableView)
        layout.addLayout(button_layout)
        self.setLayout(layout)

    def iniciar_tabla(self):
        """Inicializa la tabla y define sus columnas."""
        self.tableView = QTableView(self)
        self.model = QStandardItemModel()
        self.tableView.setModel(self.model)
        headers = [
            "Nombre",
            "Apellidos",
            "Fecha Nacimiento",
            "País",
            "Teléfono",
            "Email",
        ]
        self.model.setHorizontalHeaderLabels(headers)

        # Configurar el tamaño de las columnas para que se ajusten automáticamente
        header = self.tableView.horizontalHeader()
        for i in range(self.model.columnCount()):
            header.setSectionResizeMode(
                i, QHeaderView.ResizeMode.Stretch
            )  # Ajuste automático

    def llenar_datos(self):
        """Llena la tabla con los datos obtenidos de la base de datos."""
        if self.lista_clientes:
            for cliente in self.lista_clientes:
                # Asegúrate de que estás utilizando los nombres correctos de los atributos
                fila = [
                    str(cliente.Nombre),
                    str(cliente.Apellidos),
                    str(
                        cliente.Fec_Nac
                    ),  # Usar 'fecha_nacimiento' si ese es el nombre correcto
                    str(cliente.Pais),
                    str(cliente.Telefono),
                    str(cliente.email),
                ]
                # Agregar la fila a la tabla
                elementos = [QStandardItem(dato) for dato in fila]
                self.model.appendRow(elementos)

    # Funciones de los botones
    def agregar_cliente(self):
        print("Agregar cliente")
        # Aquí puedes abrir una ventana emergente o un formulario para agregar datos.

    def modificar_cliente(self):
        print("Modificar cliente")
        # Aquí puedes agregar lógica para modificar una fila seleccionada.

    def eliminar_cliente(self):
        print("Eliminar cliente")
        # Aquí puedes agregar lógica para eliminar la fila seleccionada.

    def salir(self):
        print("Saliendo de la aplicación")
        self.close()
