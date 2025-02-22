import sys

from PySide6.QtWidgets import QApplication

from bbdd.conexion_mysql import MySQLConnectionManager
from controller.main_controller import MainController


def devolver_conection():
    base_datos = MySQLConnectionManager(
        host="localhost", user="hotel", password="hotel", database="hotel"
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
        print("No se obtuvo conexion")


if __name__ == "__main__":
    main()
