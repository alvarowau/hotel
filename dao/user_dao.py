from dao.queries import user_dao_login


class UserDao:
    """
    Clase que maneja las operaciones relacionadas con los usuarios en la base de datos.
    """

    def __init__(self, conexion):
        """
        Inicializa el DAO con una conexión a la base de datos.

        :param conexion: Objeto de conexión a la base de datos.
        """
        self.conexion = conexion

    def login(self, username: str, password: str) -> bool:
        """
        Verifica si el usuario y la contraseña proporcionados son válidos.

        Ejecuta una consulta en la base de datos para comprobar la existencia del usuario
        con las credenciales dadas.

        :param username: Nombre de usuario a verificar.
        :param password: Contraseña del usuario.
        :return: True si las credenciales son válidas, False en caso contrario.
        """
        if self.conexion:
            cursor = self.conexion.cursor()
            try:
                cursor.execute(user_dao_login, (username, password))
                result = cursor.fetchone()
                return 0 < result[0] < 2 if result else False
            finally:
                cursor.close()
        return False
