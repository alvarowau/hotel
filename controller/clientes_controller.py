from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QHeaderView, QTableView, QWidget, QMessageBox

from iu.iu_clientes import Ui_Clientes
from iu.estilo_tabla import estilo_tabla
from dao.clientes_dao import ClienteDao


class ClientesController(QWidget):
    """Controlador para la vista de clientes."""

    def __init__(self, conexion):
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
        self.cliente_dao = ClienteDao(self.conexion)

    def init_ui(self):
        """Inicializa la interfaz de usuario y conecta los eventos"""
        self.ui.nuevo_pushButton.clicked.connect(self.nuevo_cliente)
        self.ui.saber_pushButton.clicked.connect(self.saber_mas)
        self.iniciar_tabla()

    def nuevo_cliente(self):
        """Lógica para agregar un nuevo cliente."""
        print("Nuevo cliente")  # Aquí iría la lógica real para agregar un cliente

    def saber_mas(self):
        """Lógica para mostrar más información sobre el cliente seleccionado."""
        # Obtener el índice de la fila seleccionada
        index = self.ui.clientes_tableView.selectedIndexes()
        if index:
            # El índice seleccionado siempre estará en la primera columna (ID)
            id_cliente = self.model.item(index[0].row(), 0).text()
            print(f"el id del cliente es {id_cliente}")

        else:
            print("Selecciona un cliente para ver más información.")

    def iniciar_tabla(self):
        """Configura la tabla inicialmente sin datos"""
        self.tableView = self.ui.clientes_tableView
        headers = [
            "ID",
            "Nombre Completo",  # Cambiar encabezado a "Nombre Completo"
            "Fecha Nacimiento",
            "País",
            "Teléfono",
            "Email",
        ]

        # Asignar los encabezados al modelo de la tabla
        self.model.setHorizontalHeaderLabels(headers)

        # Configurar la vista de la tabla
        self.tableView.setModel(self.model)

        # Cambiar el modo de redimensionamiento de las columnas
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Eliminar los números de las filas (índices de las filas)
        self.tableView.verticalHeader().setVisible(False)

        # Aplicar estilo Material Design oscuro a la tabla
        self.tableView.setStyleSheet(estilo_tabla)

        # Llamar a recargar_tabla para insertar datos harcodeados
        self.recargar_tabla()

    def recargar_tabla(self):
        """Recarga la tabla con datos harcodeados para hacer pruebas."""
        # Limpiar la tabla antes de agregar nuevos datos
        self.model.removeRows(0, self.model.rowCount())

        # Datos harcodeados para insertar en la tabla
        clientes = self.cliente_dao.find_all_activos()

        if clientes:
            # Insertar los datos en el modelo
            for cliente in clientes:
                row = []
                # Combinar nombre y apellido en una sola columna
                #nombre_completo = f"{cliente.nombre} {cliente.apellido}"  #

                # Insertar los datos en la fila de la tabla
                row.append(QStandardItem(str(cliente.Id)))  # ID
                row.append(
                    QStandardItem(str(f"{cliente.Nombre} {cliente.Apellidos}"))
                )  # Nombre Completo
                row.append(QStandardItem(str(cliente.Fec_Nac)))  # Fecha Nacimiento
                row.append(QStandardItem(str(cliente.Pais)))  # País
                row.append(QStandardItem(str(cliente.Telefono)))  # Teléfono
                row.append(QStandardItem(str(cliente.email)))  # Email

                # Agregar la fila al modelo
                self.model.appendRow(row)

            # Ocultar la columna de ID (índice 0)
            self.tableView.setColumnHidden(0, True)
