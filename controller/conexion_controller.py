from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Signal
from util.mostrar_mensajes import mostrar_error, mostrar_advertencia
from iu.iu_conexion import Ui_conexion
from bbdd.conexion_mysql import MySQLConnectionManager


class ConexionController(QWidget, Ui_conexion):
    """Controlador de la configuración de la base de datos."""

    configuracion_finalizada = Signal(dict)

    def __init__(self, datos_conexion):
        super().__init__()
        self.datos_conexion = datos_conexion
        self.setupUi(self)
        self.conectado = False  # Flag para evitar conexiones múltiples
        self.initUI()

    def initUI(self):
        """Inicializa eventos y configuraciones."""
        self.pushButton_probar.clicked.connect(self.probar_conexion)
        self.pushButton_conectar.setVisible(False)
        self.iniciar_campos()
        self.label_img.setPixmap(QPixmap("iu/imagenes/no_conexion.jpg"))

    def iniciar_campos(self):
        """Inicializa los campos con los datos de conexión previos."""
        self.lineEdit_host.setText(self.datos_conexion["host"])
        self.lineEdit_user.setText(self.datos_conexion["user"])
        self.lineEdit_pass.setText(self.datos_conexion["password"])
        self.lineEdit_db.setText(self.datos_conexion["database"])
        self.lineEdit_port.setText(self.datos_conexion["port"])

    def obtener_datos(self):
        """Obtiene los datos ingresados por el usuario."""
        return {
            "host": self.lineEdit_host.text().strip(),
            "user": self.lineEdit_user.text().strip(),
            "password": self.lineEdit_pass.text().strip(),
            "database": self.lineEdit_db.text().strip(),
            "port": self.lineEdit_port.text().strip(),
        }

    def validar_campos(self, datos):
        """Valida que los campos no estén vacíos."""
        return all(valor not in [None, ""] for valor in datos.values())

    def probar_conexion(self):
        """Prueba la conexión con la base de datos."""
        datos = self.obtener_datos()
        if self.validar_campos(datos):
            self.datos_conexion = datos
            bbdd = MySQLConnectionManager(**self.datos_conexion)
            conexion = bbdd.connect()
            if conexion:
                conexion.close()
                mostrar_advertencia("La conexión se ha establecido")
                self.pushButton_conectar.setVisible(True)
                if not self.conectado:
                    self.pushButton_conectar.clicked.connect(self.conectar)
                    self.conectado = True
            else:
                mostrar_error(
                    "No se ha podido establecer conexión con la base de datos"
                )
        else:
            mostrar_error("Todos los campos deben estar completos")

    def conectar(self):
        """Guarda los datos de conexión y notifica que la configuración ha finalizado."""
        print("Método conectar() llamado")
        self.configuracion_finalizada.emit(self.datos_conexion)
        self.close()

    def closeEvent(self, event):
        """Manejo adecuado del cierre de la ventana."""
        print("Evento closeEvent()")
        super().closeEvent(event)
