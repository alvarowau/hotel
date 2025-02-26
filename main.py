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
    "port": "3308",
}

app = None


def recibir_datos_conexion(datos):
    """Recoge los datos de conexión enviados desde el controlador.

    Esta función se encarga de recibir los datos de conexión a la base de datos
    desde el `ConexionController` cuando la configuración es finalizada por el usuario.
    Actualiza la variable global `datos_conexion` con los nuevos datos y, como paso
    inmediato, inicia el proceso de login llamando a la función `iniciar_login()`.

    Args:
        datos (dict): Diccionario que contiene los datos de conexión a la base de datos,
                      incluyendo host, user, password, database y port.
    """
    global datos_conexion
    datos_conexion = datos  # Actualiza los datos de conexión
    print("Datos recibidos:", datos_conexion)
    iniciar_login()  # Iniciar login tras recibir datos de conexión


def comprobar_conexion():
    """Comprueba la conexión a la base de datos y, si falla, abre la ventana de configuración.

    Utiliza la clase `ComprobadorMySQL` para verificar si es posible establecer una conexión
    con los datos de conexión actualmente definidos en la variable global `datos_conexion`.
    Si la conexión falla, inicializa la aplicación Qt si aún no se ha hecho, crea una instancia
    de `ConexionController` para permitir al usuario configurar la conexión, conecta la señal
    `configuracion_finalizada` de `ConexionController` a la función `recibir_datos_conexion`
    para que los datos configurados se recojan al cerrar la ventana de configuración, y ejecuta
    el controlador de conexión de forma modal.

    Returns:
        bool: `True` si la conexión a la base de datos es exitosa, `False` si falla o si se abre
              la ventana de configuración.
    """
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
    """Inicia la aplicación, verificando primero la conexión a la base de datos.

    Esta función es el punto de inicio del flujo de la aplicación. Primero, llama a `comprobar_conexion()`
    para asegurarse de que la conexión a la base de datos esté configurada y sea funcional.
    Si `comprobar_conexion()` retorna `True`, indicando una conexión exitosa o ya configurada,
    entonces procede a iniciar la ventana de login llamando a `iniciar_login()`.
    Si `comprobar_conexion()` retorna `False`, significa que la conexión falló o que se ha abierto
    la ventana de configuración para que el usuario la establezca; en este caso, la aplicación esperará
    a que la configuración se complete para intentar iniciar sesión posteriormente (a través de `recibir_datos_conexion`).
    """
    if comprobar_conexion():
        iniciar_login()
    else:
        iniciar()


def iniciar_login():
    """Inicia la ventana de login y el proceso de autenticación del usuario.

    Esta función se encarga de inicializar la ventana de login de la aplicación.
    Primero, se asegura de que exista una única instancia de `QApplication`. Luego, utiliza
    `MySQLConnectionManager` para intentar establecer una conexión a la base de datos utilizando
    los datos de conexión definidos en `datos_conexion`.

    Si la conexión a la base de datos se establece con éxito:
        - Crea instancias de `LoginController` y `MainController`, pasando la conexión de base de datos a ambos.
        - Conecta la señal `login_exitoso` del `LoginController` a una función lambda que se encargará
          de abrir la ventana principal (`MainController`) y cerrar la ventana de login una vez que el login
          sea exitoso.
        - Muestra la ventana de login.
        - Ejecuta el bucle de eventos de la aplicación (`app.exec()`) para iniciar la interfaz gráfica y
          esperar la interacción del usuario.

    Si la conexión a la base de datos falla:
        - Imprime un mensaje en la consola indicando que no se pudo conectar a la base de datos y que se iniciará
          la configuración (aunque en el flujo actual, la configuración ya debería haberse intentado en `comprobar_conexion`).

    Nota:
        `app.exec()` se llama solo una vez para iniciar el bucle de eventos de la aplicación. No se debe usar `sys.exit(app.exec())` aquí, ya que
        `app.exec()` gestiona el bucle de eventos hasta que la aplicación se cierre explícitamente.
    """
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
    """Abre la ventana principal de la aplicación y cierra la ventana de inicio de sesión.

    Una vez que el login del usuario ha sido exitoso, esta función se encarga de mostrar la ventana principal
    de la aplicación, gestionada por `MainController`, y de cerrar la ventana de inicio de sesión, gestionada
    por `LoginController`, limpiando así la interfaz y presentando al usuario la aplicación principal.

    Args:
        main_controller (MainController): Instancia del controlador de la ventana principal de la aplicación.
        login_controller (LoginController): Instancia del controlador de la ventana de inicio de sesión.
    """
    main_controller.show()
    login_controller.close()


def iniciar():
    """Función principal para iniciar la aplicación.

    Esta función actúa como punto de entrada principal para iniciar la aplicación. Simplemente llama a
    `iniciar_aplicacion()` para comenzar el proceso de inicialización, que incluye la verificación de la
    conexión a la base de datos y el inicio de la interfaz de usuario, ya sea con la ventana de configuración
    o directamente con la ventana de login, dependiendo del estado de la conexión.
    """
    iniciar_aplicacion()


if __name__ == "__main__":
    iniciar()
