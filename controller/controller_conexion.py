from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog

from bbdd.comprobar_conexion import ComprobadorMySQL
from iu.iu_conexion import Ui_conexion
from util.mostrar_mensajes import mostrar_error, mostrar_informacion


class ConexionController(QDialog):
    """Controlador de la configuración de la base de datos."""

    configuracion_finalizada = Signal(dict)  # Señal para enviar datos de conexión

    def __init__(self, datos_conexion):
        super().__init__()
        self.ui = Ui_conexion()
        self.ui.setupUi(self)
        self.datos_conexion = datos_conexion
        self._inicializar_ui()
        self._llenar_campos()

    def _inicializar_ui(self):
        self.ui.pushButton_conectar.setVisible(False)
        self.ui.pushButton_probar.clicked.connect(self._probar_conexion)

    def _llenar_campos(self):
        """Llena los campos de los QLineEdit con los datos de conexión."""
        self.ui.lineEdit_host.setText(self.datos_conexion["host"])
        self.ui.lineEdit_user.setText(self.datos_conexion["user"])
        self.ui.lineEdit_pass.setText(self.datos_conexion["password"])
        self.ui.lineEdit_db.setText(self.datos_conexion["database"])
        self.ui.lineEdit_port.setText(self.datos_conexion["port"])

    def obtener_datos(self):
        """Obtiene los datos ingresados por el usuario."""
        return {
            "host": self.ui.lineEdit_host.text().strip(),
            "user": self.ui.lineEdit_user.text().strip(),
            "password": self.ui.lineEdit_pass.text().strip(),
            "database": self.ui.lineEdit_db.text().strip(),
            "port": self.ui.lineEdit_port.text().strip(),
        }

    def validar_campos(self, datos):
        """Valida que los campos no estén vacíos."""
        return all(valor not in [None, ""] for valor in datos.values())

    def _probar_conexion(self):
        if self._comprobar_conexion():
            mostrar_informacion("La conexión ha sido efectuada")
            self.ui.pushButton_conectar.setVisible(True)
            self.ui.pushButton_probar.setVisible(False)
            self.ui.pushButton_conectar.clicked.connect(self.enviar_datos)
        else:
            mostrar_error("No se ha podido establecer la conexión")

    def enviar_datos(self):
        """Envía los datos de conexión al main."""
        # Utiliza self.datos_conexion en lugar de self.datos_conexion_true
        self.configuracion_finalizada.emit(self.datos_conexion_true)
        self.accept()

    def _comprobar_conexion(self):
        """Verifica la conexión a la base de datos."""
        comprobador = ComprobadorMySQL()
        dict_conexion = self.obtener_datos()
        respuesta = comprobador.comprobar_conexion(**dict_conexion)
        if respuesta:
            self.datos_conexion_true = dict_conexion
            return True
        else:
            return False
