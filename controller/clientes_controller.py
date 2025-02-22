from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import (
    QHeaderView,
    QTableView,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QHBoxLayout,
)


class ClientesController(QWidget):
    """Controlador de la vista de clientes."""

    def __init__(self, conexion):
        super().__init__()

        # Crear la tabla
        self.tableView = QTableView(self)
        self.conexion = conexion

        # Crear el modelo de datos
        self.model = QStandardItemModel()
        self.tableView.setModel(self.model)

        # Definir encabezados de columna
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

        # Llenar con datos de prueba (harcodeados)
        self.llenar_datos()

        # Crear los botones
        self.nueva_button = QPushButton("Nueva")
        self.modificar_button = QPushButton("Modificar")
        self.eliminar_button = QPushButton("Eliminar")
        self.salir_button = QPushButton("Salir")

        # Conectar los botones a las funciones
        self.nueva_button.clicked.connect(self.agregar_cliente)
        self.modificar_button.clicked.connect(self.modificar_cliente)
        self.eliminar_button.clicked.connect(self.eliminar_cliente)
        self.salir_button.clicked.connect(self.salir)

        # Layout para los botones
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.nueva_button)
        button_layout.addWidget(self.modificar_button)
        button_layout.addWidget(self.eliminar_button)
        button_layout.addWidget(self.salir_button)

        # Layout principal
        layout = QVBoxLayout(self)
        layout.addWidget(self.tableView)  # Agregar la tabla
        layout.addLayout(button_layout)  # Agregar los botones
        self.setLayout(layout)

    def llenar_datos(self):
        """Llena la tabla con datos de prueba."""
        datos = [
            ["Juan", "Pérez", "1990-05-12", "España", "600123456", "juan@example.com"],
            [
                "María",
                "López",
                "1985-10-23",
                "México",
                "555678901",
                "maria@example.com",
            ],
            [
                "Carlos",
                "Martínez",
                "1992-03-17",
                "Argentina",
                "911234567",
                "carlos@example.com",
            ],
            ["Ana", "González", "1988-07-08", "Chile", "987654321", "ana@example.com"],
        ]

        for fila in datos:
            elementos = [QStandardItem(dato) for dato in fila]
            self.model.appendRow(elementos)

    # Funciones de los botones
    def agregar_cliente(self):
        print("Agregar cliente")

    def modificar_cliente(self):
        print("Modificar cliente")

    def eliminar_cliente(self):
        print("Eliminar cliente")

    def salir(self):
        print("Saliendo de la aplicación")
        self.close()
