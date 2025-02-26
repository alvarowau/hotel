import mysql.connector


class ComprobadorMySQL:
    """
    Clase para comprobar la conexión a un servidor MySQL.

    Ofrece métodos para verificar si se puede establecer
    una conexión con los parámetros proporcionados a una base de datos MySQL.
    """

    def comprobar_conexion(self, host, user, password, database, port):
        """
        Comprueba si se puede establecer una conexión a la base de datos MySQL.

        Intenta conectar a la base de datos MySQL utilizando los parámetros
        proporcionados. Devuelve `True` si la conexión se establece
        correctamente, y `False` en caso contrario.

        Args:
            host (str): La dirección del servidor MySQL (hostname o IP).
            user (str): El nombre de usuario para la conexión MySQL.
            password (str): La contraseña del usuario de MySQL.
            database (str): El nombre de la base de datos a la que conectar.
            port (int): El puerto del servidor MySQL.

        Returns:
            bool: `True` si la conexión fue exitosa, `False` en caso de error.
        """
        try:
            connection = mysql.connector.connect(
                host=host, user=user, password=password, database=database, port=port
            )
            if connection.is_connected():
                connection.close()
                return True
        except mysql.connector.Error:
            return False
        return False  # Esta línea sigue siendo redundante, ya que el 'except' ya retorna False.
