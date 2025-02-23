import sys
from PySide6.QtWidgets import QApplication
from bbdd.conexion_mysql import MySQLConnectionManager
from bbdd.comprobar_conexion import ComprobadorMySQL
from controller.conexion_controller import ConexionController
from controller.controller_login import LoginController
from controller.main_controller import MainController

datos_conexion = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "hotel",
    "port": "3307",
}

app = None


def iniciar_aplicacion():
    """Inicia la aplicación con la ventana de configuración primero."""
    iniciar_configuracion()


def iniciar_configuracion():
    """Muestra la ventana de configuración."""
    global app
    if app is None:
        app = QApplication(
            []
        )  # Se asegura de que solo haya una instancia de QApplication
    ventana = ConexionController(datos_conexion)
    ventana.configuracion_finalizada.connect(actualizar_datos_y_reiniciar)
    ventana.show()
    if QApplication.instance() is None:
        app.exec()


def actualizar_datos_y_reiniciar(nuevos_datos):
    """Actualiza los datos de conexión."""
    global datos_conexion
    datos_conexion = nuevos_datos
    print("Datos actualizados.")
    # Aquí no iniciamos el login de forma inmediata, solo configuramos los datos


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
        if QApplication.instance() is None:
            sys.exit(app.exec())
    else:
        print("No se pudo conectar a la base de datos. Iniciando configuración.")
        iniciar_configuracion()


def abrir_ventana_principal(main_controller, login_controller):
    """Abre la ventana principal y cierra la ventana de inicio de sesión."""
    main_controller.show()
    login_controller.close()


def iniciar():
    """Inicia la aplicación."""
    iniciar_aplicacion()


if __name__ == "__main__":
    iniciar()
