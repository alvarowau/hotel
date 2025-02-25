from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QHeaderView, QWidget

from controller.controller_clientes_edit import ControladorClientesEdit
from dao.clientes_dao import ClienteDao
from iu.estilo_tabla import estilo_tabla
from iu.iu_clientes import Ui_Clientes
from util.mostrar_mensajes import mostrar_informacion


class ClientesController(QWidget):
    """Controlador para la vista de clientes."""

    def __init__(self, conexion):
        """Inicializa el controlador de clientes.

        Args:
            conexion: Objeto de conexión a la base de datos.
        """
        super().__init__()
        if conexion:
            self.ui = Ui_Clientes()
            self.conexion = conexion
            self.iniciar_daos()
            self.ui.setupUi(self)
            self.model = QStandardItemModel()
            self.cliente_seleccionado = None
            self.init_ui()
        else:
            print("no hay conexion")

    def iniciar_daos(self):
        """Inicializa los objetos de acceso a datos (DAOs)."""
        self.cliente_dao = ClienteDao(self.conexion)

    def init_ui(self):
        """Inicializa la interfaz de usuario y conecta los eventos."""
        self.ui.nuevo_pushButton.setText("Nuevo cliente")
        self.ui.nuevo_pushButton.clicked.connect(self.nuevo_cliente)
        self.ui.saber_pushButton.clicked.connect(self.saber_mas)
        self.iniciar_tabla()

    def nuevo_cliente(self):
        """Abre el modal para crear un nuevo cliente."""
        self.abrir_cliente_modal()

    def saber_mas(self):
        """Muestra información detallada del cliente seleccionado."""
        index = self.ui.clientes_tableView.selectedIndexes()
        if index:
            id_cliente = self.model.item(index[0].row(), 0).text()
            self.abrir_cliente_modal(id_cliente)
        else:
            mostrar_informacion("Selecciona un cliente para ver más información.")

    def abrir_cliente_modal(self, id_cliente=None):
        """Abre la ventana modal para edición/creación de cliente.

        Args:
            id_cliente (str, optional): ID del cliente para editar. Defaults to None (creación nuevo cliente).
        """
        ventana_edicion = ControladorClientesEdit(self.conexion, id_cliente)
        ventana_edicion.exec_()
        self.recargar_tabla()

    def iniciar_tabla(self):
        """Configura e inicializa la tabla de clientes."""
        self.tableView = self.ui.clientes_tableView
        headers = [
            "ID",
            "Nombre Completo",
            "Fecha Nacimiento",
            "País",
            "Teléfono",
            "Email",
        ]

        self.model.setHorizontalHeaderLabels(headers)
        self.tableView.setModel(self.model)

        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.tableView.verticalHeader().setVisible(False)
        self.tableView.setStyleSheet(estilo_tabla)

        self.recargar_tabla()

    def recargar_tabla(self):
        """Recarga los datos de la tabla de clientes desde la base de datos."""
        self.model.removeRows(0, self.model.rowCount())
        clientes = self.cliente_dao.find_all_activos()

        if clientes:
            for cliente in clientes:
                row = []
                row.append(QStandardItem(str(cliente.Id)))
                row.append(QStandardItem(str(f"{cliente.Nombre} {cliente.Apellidos}")))
                row.append(QStandardItem(str(cliente.Fec_Nac)))
                row.append(QStandardItem(str(cliente.Pais)))
                row.append(QStandardItem(str(cliente.Telefono)))
                row.append(QStandardItem(str(cliente.email)))
                self.model.appendRow(row)

            self.tableView.setColumnHidden(0, True)
