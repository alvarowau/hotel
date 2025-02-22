from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import (
    QHBoxLayout,
    QHeaderView,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)

# Datos de prueba
datos = [
    ["Juan Pérez", "París", "2025-03-01", "España"],
    ["María López", "Londres", "2025-03-02", "México"],
    ["Carlos Gómez", "Nueva York", "2025-03-03", "Argentina"],
    ["Ana Sánchez", "Roma", "2025-03-04", "Chile"],
]


class ReservasControler(QWidget):
    """Controlador de la vista de reservas."""

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
            "Destino",
            "Fecha reserva",
            "País reserva",
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
        for fila in datos:
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
