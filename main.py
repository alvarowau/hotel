import sys
from PySide6.QtWidgets import QApplication
from controller.controller_login import LoginController
from bbdd.conexion_mysql import MySQLConnectionManager


def inicio_aplicacion():
    base_datos = MySQLConnectionManager(host="localhost",
                                        user="hotel",
                                        password="hotel",
                                        database="hotel")
    conexion = base_datos.connect()
    if conexion:
        inciar_grafica(conexion)
    else:
        print("No se ha conectado")


def inciar_grafica(conexion):
    app = QApplication(sys.argv)
    login_controller = LoginController(conexion=conexion)
    login_controller.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    inicio_aplicacion()
