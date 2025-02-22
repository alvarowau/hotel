from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import (
    QHBoxLayout,
    QHeaderView,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)
from dao.reserva_dao import ReservaDao
from dao.salones_dao import SalonDao
from dao.tipo_cocina_dao import TipoCocinaDao
from dao.tipo_reserva_dao import TipoReservasDao
from dao.clientes_dao import ClienteDao


class ReservasControler(QWidget):
    """Controlador de la vista de reservas."""

    def __init__(self, conexion):
        super().__init__()
        self.conexion = conexion
        if self.conexion:
            self.iniciar_daos()
            self.traer_listas()  # Se debe llamar a traer_listas antes de acceder a las listas
            self.traer_reservas()
            self.iniciar_tabla()  # Llamar a iniciar_tabla antes de llenar los datos
            self.llenar_datos()
            self.iniciar_interface()
        else:
            print("No hay conexion")

    def iniciar_daos(self):
        self.reserva_dao = ReservaDao(self.conexion)
        self.salon_dao = SalonDao(self.conexion)
        self.tipo_cocina_dao = TipoCocinaDao(self.conexion)
        self.tipo_reserva_dao = TipoReservasDao(self.conexion)
        self.cliente_dao = ClienteDao(self.conexion)

    def traer_listas(self):
        self.lista_salones = self.salon_dao.find_all()
        self.lista_tipo_reservas = self.tipo_reserva_dao.find_all()
        self.lista_tipo_cocina = self.tipo_cocina_dao.find_all()

    def nombre_salon_by_id(self, id_salon):
        if self.lista_salones:
            for salon in self.lista_salones:
                if salon.salon_id == id_salon:
                    return salon.nombre

    def nombre_tipo_cocina_by_id(self, id_tipo_cocina):
        if self.lista_tipo_cocina:
            for cocina in self.lista_tipo_cocina:
                if cocina.tipo_cocina_id == id_tipo_cocina:
                    return cocina.nombre

    def nombre_tipo_reserva_by_id(self, tipo_reserva_id):
        if self.lista_tipo_reservas:
            for tipo_reserva in self.lista_tipo_reservas:
                if tipo_reserva.tipo_reserva_id == tipo_reserva_id:
                    return tipo_reserva.nombre

    def traer_reservas(self):
        self.lista_reservas = self.reserva_dao.find_all()

    def iniciar_interface(self):
        # Crear los botones
        self.nueva_button = QPushButton("Nueva")
        self.modificar_button = QPushButton("Modificar")
        self.eliminar_button = QPushButton("Eliminar")
        self.salir_button = QPushButton("Salir")

        # Conectar los botones a las funciones
        self.nueva_button.clicked.connect(self.agregar_reserva)
        self.modificar_button.clicked.connect(self.modificar_reserva)
        self.eliminar_button.clicked.connect(self.eliminar_reserva)
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

    def iniciar_tabla(self):
        self.tableView = QTableView(self)
        self.model = QStandardItemModel()
        self.tableView.setModel(self.model)

        headers = [
            "Tipo reserva",
            "Salon id",
            "tipo cocina",
            "cliente",
            "fecha",
        ]
        self.model.setHorizontalHeaderLabels(headers)
        header = self.tableView.horizontalHeader()
        for i in range(self.model.columnCount()):
            header.setSectionResizeMode(
                i, QHeaderView.ResizeMode.Stretch
            )  # Ajuste automático

    def llenar_datos(self):
        """Llena la tabla con datos de prueba."""
        if self.lista_reservas:
            for reserva in self.lista_reservas:
                fila = [
                    str(self.nombre_tipo_reserva_by_id(reserva.tipo_reserva_id)),
                    str(self.nombre_salon_by_id(reserva.salon_id)),
                    str(self.nombre_tipo_cocina_by_id(reserva.tipo_cocina_id)),
                    str(self.cliente_dao.find_nombre_by_id(reserva.id_cliente)),
                    str(reserva.fecha),
                ]
                elementos = [QStandardItem(dato) for dato in fila]
                self.model.appendRow(elementos)

    def agregar_reserva(self):
        print("Agregar reserva")
        # Aquí puedes abrir una ventana emergente o un formulario para agregar una nueva reserva.

    def modificar_reserva(self):
        print("Modificar reserva")
        # Aquí puedes agregar lógica para modificar una reserva existente.

    def eliminar_reserva(self):
        print("Eliminar reserva")
        # Aquí puedes agregar lógica para eliminar una reserva seleccionada.

    def salir(self):
        print("Saliendo de la aplicación")
        self.close()
