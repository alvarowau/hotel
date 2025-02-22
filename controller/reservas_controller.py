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
from dao.reserva_dao import ReservaDao
from dao.salones_dao import SalonDao
from dao.tipo_cocina_dao import TipoCocinaDao
from dao.tipo_reserva_dao import TipoReservasDao
from util.mostrar_mensajes import confirmar_eliminacion_usuario, mostrar_error


class ReservasControler(QWidget):
    """Controlador de la vista de reservas."""

    def __init__(self, conexion):
        super().__init__()
        self.conexion = conexion
        if self.conexion:
            self.iniciar_daos()
            self.traer_listas()
            self.iniciar_tabla()
            self.recargar_tabla()
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
        self.nueva_button = QPushButton("Nueva")
        self.modificar_button = QPushButton("Modificar")
        self.eliminar_button = QPushButton("Eliminar")
        self.salir_button = QPushButton("Salir")

        self.nueva_button.clicked.connect(self.agregar_reserva)
        self.modificar_button.clicked.connect(self.modificar_reserva)
        self.eliminar_button.clicked.connect(self.eliminar_reserva)
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
            "Tipo reserva",
            "Salón",
            "Tipo cocina",
            "Cliente",
            "Fecha",
        ]
        self.model.setHorizontalHeaderLabels(headers)
        header = self.tableView.horizontalHeader()
        for i in range(self.model.columnCount()):
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)

    def recargar_tabla(self):
        """Recarga la tabla con los datos actualizados."""
        self.model.removeRows(0, self.model.rowCount())
        self.traer_reservas()

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
                id_reserva_item = QStandardItem(str(reserva.reserva_id))
                id_reserva_item.setEditable(False)
                id_reserva_item.setData(True, Qt.ItemDataRole.UserRole)

                self.model.appendRow(elementos)
                if not hasattr(self, "id_items"):
                    self.id_items = {}
                self.id_items[self.model.rowCount() - 1] = id_reserva_item

    def agregar_reserva(self):
        print("Agregar reserva")

    def obtener_id_desde_index(self, index):
        row = index.row()
        id_reserva_item = self.id_items[row]
        return id_reserva_item.text()

    def modificar_reserva(self):
        try:
            index = self.tableView.selectionModel().currentIndex()
            if index.isValid():
                # print(f"ID reserva: {self.obtener_id_desde_index(index)}")
                id_reserva = self.obtener_id_desde_index(index)
                self.reserva_dao.traer_details_delete(id_reserva)
            else:
                mostrar_error("No se ha seleccionado ninguna reserva")
        except Exception:
            mostrar_error("Ocurrió un error al intentar modificar reserva")

    def eliminar_reserva(self):
        try:
            index = self.tableView.selectionModel().currentIndex()
            if index.isValid():
                # print(f"ID reserva: {self.obtener_id_desde_index(index)}")
                id_reserva = self.obtener_id_desde_index(index)
                print(f"el id de la reserva {id_reserva}")
                resultado = self.reserva_dao.traer_details_delete(id_reserva)
                respuesta_ventana = confirmar_eliminacion_usuario(
                    f"Quiere eliminar la reserva {resultado}"
                )
                if respuesta_ventana:
                    print(f"Quiere eliminar el usuario {id_reserva}")
            else:
                print("entro en el else")
                mostrar_error("No se ha seleccionado ninguna reserva")
        except Exception:
            mostrar_error("Ocurrió un error al intentar modificar reserva")

    def salir(self):
        print("salir")
