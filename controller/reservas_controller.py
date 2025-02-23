from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QHeaderView, QTableView, QWidget

from iu.iu_reservas import Ui_Reservas
from iu.estilo_tabla import estilo_tabla


class ReservasController(QWidget):
    """Controlador para la vista de reservas."""

    def __init__(self, conexion):
        super().__init__()
        self.conexion = conexion
        self.ui = Ui_Reservas()
        self.ui.setupUi(self)
        self.model = QStandardItemModel()
        self.reserva_seleccionada = None
        self.init_ui()

    def init_ui(self):
        """Inicializa la interfaz de usuario y conecta los eventos"""
        self.ui.nuevo_pushButton.clicked.connect(self.nueva_reserva)
        self.ui.saber_pushButton.clicked.connect(self.saber_mas)
        self.iniciar_tabla()

    def nueva_reserva(self):
        """Lógica para agregar una nueva reserva."""
        print("Nueva reserva")  # Aquí iría la lógica real para agregar una reserva
        # Puedes abrir un modal para crear una nueva reserva como en el otro ejemplo
        # self.open_modal(True)

    def saber_mas(self):
        """Lógica para mostrar más información sobre la reserva seleccionada."""
        if self.reserva_seleccionada:
            print(f"Más información de la reserva: {self.reserva_seleccionada}")
        else:
            print("Selecciona una reserva", "warning")

    def iniciar_tabla(self):
        """Configura la tabla inicialmente sin datos"""
        self.tableView = self.ui.reservas_tableView

        # Definir los encabezados de la tabla
        headers = [
            "ID",
            "Tipo reserva",
            "Salón",
            "Tipo cocina",
            "Cliente",
            "Fecha",
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
        reservas = [
            {
                "id_reserva": 1,
                "tipo_reserva": "Individual",
                "salon": "A",
                "tipo_cocina": "Buffet",
                "cliente": "Juan Pérez",
                "fecha": "2025-03-01",
            },
            {
                "id_reserva": 2,
                "tipo_reserva": "Grupo",
                "salon": "B",
                "tipo_cocina": "Menú",
                "cliente": "Ana Gómez",
                "fecha": "2025-03-02",
            },
            {
                "id_reserva": 3,
                "tipo_reserva": "VIP",
                "salon": "C",
                "tipo_cocina": "A la carta",
                "cliente": "Carlos López",
                "fecha": "2025-03-05",
            },
            {
                "id_reserva": 4,
                "tipo_reserva": "Individual",
                "salon": "A",
                "tipo_cocina": "Buffet",
                "cliente": "Maria Martínez",
                "fecha": "2025-03-07",
            },
            {
                "id_reserva": 5,
                "tipo_reserva": "Grupo",
                "salon": "B",
                "tipo_cocina": "Menú",
                "cliente": "Pedro Rodríguez",
                "fecha": "2025-03-10",
            },
        ]

        # Insertar los datos en el modelo
        for reserva in reservas:
            row = []
            # Insertar los datos en la fila de la tabla
            row.append(QStandardItem(str(reserva["id_reserva"])))  # ID
            row.append(QStandardItem(reserva["tipo_reserva"]))  # Tipo reserva
            row.append(QStandardItem(reserva["salon"]))  # Salón
            row.append(QStandardItem(reserva["tipo_cocina"]))  # Tipo cocina
            row.append(QStandardItem(reserva["cliente"]))  # Cliente
            row.append(QStandardItem(reserva["fecha"]))  # Fecha

            # Agregar la fila al modelo
            self.model.appendRow(row)

        # Ocultar la columna de ID (índice 0)
        self.tableView.setColumnHidden(0, True)
