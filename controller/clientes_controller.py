from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import (
    QHBoxLayout,
    QHeaderView,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)

from dao.clientes_dao import ClienteDao
from util.mostrar_mensajes import confirmar_eliminacion_usuario, mostrar_error


class ClientesController(QWidget):
    """Controlador de la vista de clientes."""

    def __init__(self, conexion):
        super().__init__()
        self.iniciar_tabla()
        self.conexion = conexion
        self.clientes_dao = ClienteDao(self.conexion)
        self.iniciar_interface()
        self.recargar_tabla()

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

        layout = QVBoxLayout(self)
        layout.addWidget(self.tableView)
        layout.addLayout(button_layout)
        self.setLayout(layout)

    def iniciar_tabla(self):
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

        header = self.tableView.horizontalHeader()
        for i in range(self.model.columnCount()):
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)

    def recargar_tabla(self):
        self.model.removeRows(0, self.model.rowCount())
        self.lista_clientes = self.clientes_dao.find_all_activos()
        if self.lista_clientes:
            for cliente in self.lista_clientes:
                fila = [
                    str(cliente.Nombre),
                    str(cliente.Apellidos),
                    str(cliente.Fec_Nac),
                    str(cliente.Pais),
                    str(cliente.Telefono),
                    str(cliente.email),
                ]
                elementos = [QStandardItem(dato) for dato in fila]

                id_cliente_item = QStandardItem(str(cliente.Id))
                id_cliente_item.setEditable(False)
                id_cliente_item.setData(True, Qt.ItemDataRole.UserRole)

                self.model.appendRow(elementos)

                if not hasattr(self, "id_items"):
                    self.id_items = {}
                self.id_items[self.model.rowCount() - 1] = id_cliente_item

    def agregar_cliente(self):
        print("Agregar cliente")

    def obtener_id_desde_index(self, index):
        row = index.row()
        id_cliente_item = self.id_items[row]
        return id_cliente_item.text()

    def modificar_cliente(self):
        try:
            index = self.tableView.selectionModel().currentIndex()
            if index.isValid():
                print(f"ID Cliente: {self.obtener_id_desde_index(index)}")
            else:
                mostrar_error("No se ha seleccionado ningún cliente")
        except Exception:
            mostrar_error("Ocurrió un error al intentar modificar el cliente")

    def eliminar_cliente(self):
        try:
            index = self.tableView.selectionModel().currentIndex()
            if index.isValid():
                id = self.obtener_id_desde_index(index)
                nombre_completo = self.clientes_dao.find_nombre_by_id(id)
                mensaje = (
                    f"¿Está seguro que desea eliminar al usuario {nombre_completo}?"
                )
                respuesta_ventana = confirmar_eliminacion_usuario(mensaje)
                if respuesta_ventana:
                    self.clientes_dao.deactivate(id)
                    self.recargar_tabla()
            else:
                mostrar_error("No se ha seleccionado ningún cliente")
        except Exception:
            mostrar_error("Ocurrió un error al intentar eliminar el cliente")

    def salir(self):
        print("Saliendo de la aplicación")
        self.close()
