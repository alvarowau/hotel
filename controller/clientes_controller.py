from PySide6.QtWidgets import QWidget

from iu.iu_clientes import Ui_clientes


class ClientesController(QWidget):
    """Controlador de la vista de clientes."""

    def __init__(self):
        super().__init__()
        self.ui = Ui_clientes()
        self.ui.setupUi(self)

        # Conectar botones
        self.ui.nueva_button.clicked.connect(self.agregar_cliente)
        self.ui.modificar_button.clicked.connect(self.modificar_cliente)
        self.ui.eliminar_button.clicked.connect(self.eliminar_cliente)
        self.ui.eliminar_button.clicked.connect(self.salir)

    def agregar_cliente(self):
        """Lógica para agregar un cliente."""
        print("Agregar cliente")

    def modificar_cliente(self):
        """Lógica para modificar un cliente."""
        print("Modificar cliente")

    def eliminar_cliente(self):
        """Lógica para eliminar un cliente."""
        print("Eliminar cliente")

    def salir(self):
        print("Saliendo de la aplicación")
        self.close()
