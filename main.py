import sys

from PySide6.QtWidgets import QApplication

from bbdd.comprobar_conexion import ComprobadorMySQL
from bbdd.conexion_mysql import MySQLConnectionManager
from controller.controller_conexion import ConexionController
from controller.controller_login import LoginController
from controller.controller_main import MainController

datos_conexion = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "hotel",
    "port": "3307",
}

app = None


def recibir_datos_conexion(datos):
    """Recoge los datos de conexión enviados desde el controlador."""
    global datos_conexion
    datos_conexion = datos  # Actualiza los datos de conexión
    print(
        "Datos recibidos:", datos_conexion
    )  # Aquí puedes hacer lo que necesites con los datos


def comprobar_conexion():
    """Comprueba la conexión y, si falla, abre la ventana de configuración."""
    global app

    compro = ComprobadorMySQL()
    if compro.comprobar_conexion(**datos_conexion):
        return True
    else:
        if not app:
            app = QApplication(sys.argv)

        conexion_controller = ConexionController(datos_conexion)
        conexion_controller.configuracion_finalizada.connect(
            recibir_datos_conexion
        )  # Conecta la señal
        conexion_controller.exec()

        return False


def iniciar_aplicacion():
    """Inicia la aplicación con la ventana de configuración primero."""
    ##
    if comprobar_conexion():
        iniciar_login()
    else:
        iniciar()


# en iniciar_login
def iniciar_login():
    """Este método inicia la ventana de login cuando se llame explícitamente."""
    global app
    if app is None:
        app = QApplication(
            []
        )  # Se asegura de que solo haya una instancia de QApplication
    base_datos = MySQLConnectionManager(**datos_conexion)
    try:
        conexion = base_datos.connect()
    except Exception:
        conexion = None
    if conexion:
        login_controller = LoginController(conexion=conexion)
        main_controller = MainController(conexion=conexion)
        login_controller.login_exitoso.connect(
            lambda: abrir_ventana_principal(main_controller, login_controller)
        )
        login_controller.show()
        app.exec()  # Solo se llama una vez, no sys.exit()
    else:
        print("No se pudo conectar a la base de datos. Iniciando configuración.")


def abrir_ventana_principal(main_controller, login_controller):
    """Abre la ventana principal y cierra la ventana de inicio de sesión."""
    main_controller.show()
    login_controller.close()


def iniciar():
    """Inicia la aplicación."""
    iniciar_aplicacion()


if __name__ == "__main__":
    iniciar()
