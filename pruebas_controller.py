import sys

from PySide6.QtWidgets import QApplication

from bbdd.conexion_mysql import MySQLConnectionManager
from controller.main_controller import MainController


def devolver_conection():
    base_datos = MySQLConnectionManager(
        host="localhost", user="root", password="root", database="hotel", port="3308"
    )
    conexion = base_datos.connect()
    if conexion:
        return conexion
    else:
        return None


def main():
    conexion = devolver_conection()
    if conexion:
        app = QApplication(sys.argv)
        ventana_principal = MainController(conexion)
        ventana_principal.show()
        sys.exit(app.exec())
    else:
        print("no tenemos conexion")


if __name__ == "__main__":
    main()
