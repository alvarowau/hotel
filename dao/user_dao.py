from dao.queris import user_dao_login


class UserDao:
    def __init__(self, conexion):
        self.conexion = conexion

    def login(self, username: str, password: str) -> bool:
        """
        Verifica si el usuario y la contraseña son correctos.
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
