from typing import Any, Optional

import mysql.connector


class MySQLConnectionManager:
    """
    Maneja la conexión a una base de datos MySQL.
    """

    def __init__(
        self, host: str, user: str, password: str, database: str, port: int = 3306
    ):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.connection: Optional[Any] = None  # Se permite cualquier tipo de conexión

    def connect(self) -> Any:
        """
        Establece y devuelve una conexión a la base de datos MySQL.
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
        """
        if self.connection and self.connection.is_connected():
            self.connection.close()
            self.connection = None
