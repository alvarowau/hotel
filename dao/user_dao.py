from dao.queries import user_dao_login


class UserDao:
    """
    Clase que maneja las operaciones de acceso a datos (DAO) para la entidad User.

    Esta clase proporciona métodos para interactuar con la base de datos, como la autenticación
    de usuarios (login).

    Atributos:
        conexion: Objeto de conexión a la base de datos.

    Métodos:
        login(username, password): Verifica las credenciales de un usuario.
    """

    def __init__(self, conexion):
        """
        Inicializa una instancia de UserDao.

        Args:
            conexion: Objeto de conexión a la base de datos.
        """
        self.conexion = conexion

    def login(self, username: str, password: str) -> bool:
        """
        Verifica las credenciales de un usuario en la base de datos.

        Args:
            username (str): El nombre de usuario.
            password (str): La contraseña del usuario.

        Returns:
            bool: True si las credenciales son válidas, False en caso contrario.
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
