import sys
from PySide6.QtWidgets import QApplication
from controller.controller_login import LoginController
from controller.main_controller import MainController
from bbdd.conexion_mysql import MySQLConnectionManager


def inicio_aplicacion():
    """Inicia la aplicación estableciendo la conexión con la base de datos.

    Conecta a la base de datos MySQL y, si la conexión es exitosa, inicia la interfaz gráfica
    llamando a `inciar_grafica`. Si la conexión falla, imprime un mensaje de error en la consola.

    """
    base_datos = MySQLConnectionManager(
        host="localhost", user="hotel", password="hotel", database="hotel"
    )
    conexion = base_datos.connect()
    if conexion:
        inciar_grafica(conexion)
    else:
        print("No se ha conectado")


def inciar_grafica(conexion):
    """Inicia la interfaz gráfica y muestra la ventana de login.

    Crea una instancia de `QApplication` y configura los controladores para las vistas de login
    y la ventana principal. Conecta la señal de login exitoso para mostrar la ventana principal
    y cerrar la ventana de login.

    Args:
        conexion (MySQLConnectionManager): Objeto de conexión a la base de datos.
    """
    app = QApplication(sys.argv)

    # Crear el controlador de login
    login_controller = LoginController(conexion=conexion)

    # Crear el controlador de la ventana principal
    main_controller = MainController(conexion=conexion)

    # Conectar la señal de login exitoso para abrir la ventana principal
    login_controller.login_exitoso.connect(
        lambda: abrir_ventana_principal(main_controller, login_controller)
    )

    # Mostrar la ventana de login
    login_controller.show()

    sys.exit(app.exec())


def abrir_ventana_principal(main_controller, login_controller):
    """Abre la ventana principal y cierra la ventana de login.

    Esta función se llama cuando el login es exitoso. Muestra la ventana principal y
    cierra la ventana de login.

    Args:
        main_controller (MainController): Controlador de la ventana principal.
        login_controller (LoginController): Controlador de la ventana de login.
    """
    main_controller.show()  # Mostrar la ventana principal
    login_controller.close()  # Cerrar la ventana de login


if __name__ == "__main__":
    inicio_aplicacion()
