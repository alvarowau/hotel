from PySide6.QtWidgets import QApplication
from controller.controller_conexion import ConexionController

datos_conexion = {
    "host": "localhost",
    "user": "hotel",
    "password": "hotel",
    "database": "hotel",
    "port": "3307",
}
def main():
    """Punto de entrada de la aplicación."""
    app = QApplication([])
    ventana = ConexionController(datos_conexion)
    ventana.show()
    app.exec()


if __name__ == "__main__":
    main()
