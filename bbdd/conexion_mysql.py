from typing import Any, Optional

import mysql.connector


class MySQLConnectionManager:
    """
    Maneja la conexión a una base de datos MySQL.

    Esta clase facilita la gestión de conexiones a una base de datos MySQL,
    permitiendo establecer, reutilizar y cerrar conexiones de manera
    segura y eficiente.
    """

    def __init__(
        self, host: str, user: str, password: str, database: str, port: str = "3306"
    ):
        """
        Inicializa el administrador de conexiones MySQL.

        Crea una instancia de `MySQLConnectionManager` con los parámetros
        necesarios para establecer la conexión a la base de datos.  La conexión
        no se establece inmediatamente, sino hasta que se llama al método `connect()`.

        Args:
            host (str):  Dirección del servidor MySQL (hostname o IP).
            user (str):  Nombre de usuario para la conexión MySQL.
            password (str): Contraseña del usuario de MySQL.
            database (str): Nombre de la base de datos a la que conectar.
            port (str, optional): Puerto del servidor MySQL. Por defecto '3306'.
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.connection: Optional[Any] = None

    def connect(self) -> Any:
        """
        Establece y devuelve una conexión a la base de datos MySQL.

        Verifica si ya existe una conexión activa. Si no existe o la conexión
        actual no está activa, establece una nueva conexión utilizando los
        parámetros proporcionados en el constructor.

        Returns:
            Any:  Objeto de conexión de `mysql.connector`.  Retorna la conexión
                  existente si ya estaba activa, o una nueva conexión si fue necesario
                  establecerla. En caso de error al conectar, puede retornar `None` o
                  lanzar una excepción (dependiendo del manejo de errores que se implemente
                  adicionalmente en el método, aunque en este ejemplo no se manejan
                  excepciones explícitamente en la conexión).
        """
        if self.connection is None or not self.connection.is_connected():
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port,
            )
        return self.connection

    def close(self):
        """
        Cierra la conexión a la base de datos si está abierta.

        Verifica si existe una conexión activa y la cierra de manera segura.
        Además, establece el atributo `connection` a `None` para indicar que
        ya no hay una conexión activa.
        """
        if self.connection and self.connection.is_connected():
            self.connection.close()
            self.connection = None
