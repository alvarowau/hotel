from PySide6.QtWidgets import QApplication, QWidget

from iu.iu_reservas import Ui_RESERVAS


class ReservasControler(QWidget):
    """Controlador de la vista de reservas."""

    def __init__(self):
        super().__init__()
        self.ui = Ui_RESERVAS()
        self.ui.setupUi(self)

        # conectar botones
        self.ui.eliminar_button.clicked.connect(self.eliminar_reserva)
        self.ui.modificar_button.clicked.connect(self.modificar_reserva)
        self.ui.nueva_button.clicked.connect(self.nueva_reserva)
        self.ui.salir_button.clicked.connect(self.salir)

    def eliminar_reserva(self):
        print("Estas eliminando una reserva")

    def modificar_reserva(self):
        print("Estas modificando una reserva")

    def nueva_reserva(self):
        print("Estas creando una nueva reserva")

    def salir(self):
        print("Saliendo de la aplicación")
        QApplication.quit()
