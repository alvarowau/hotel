from typing import Optional


class User:
    """
    Representación de un usuario del sistema.

    Esta clase define la estructura de un usuario con sus atributos principales:
    identificador de usuario, nombre de usuario y contraseña. Proporciona métodos
    para inicializar un usuario, representarlo en formato de cadena y crear
    instancias de `User` a partir de un diccionario.

    Attributes:
        user_id (Optional[int]): Identificador único del usuario. Puede ser None si el
                                  usuario no ha sido persistido aún en la base de datos.
        username (str): Nombre de usuario utilizado para el login.
        password (str): Contraseña del usuario (se debe manejar de forma segura en la
                        aplicación real, p.ej., utilizando hash).
    """

    def __init__(self, username: str, password: str, user_id: Optional[int] = None):
        """
        Inicializa una instancia de la clase User.

        Args:
            username (str): Nombre de usuario.
            password (str): Contraseña del usuario.
            user_id (Optional[int], optional): Identificador del usuario. Defaults to None.
        """
        self.user_id: Optional[int] = user_id
        self.username: str = username
        self.password: str = password

    def __repr__(self):
        """
        Representación en cadena del objeto User.

        Proporciona una representación legible en formato de cadena del objeto `User`,
        útil para debugging y logs.

        Returns:
            str: Cadena representando el objeto User, incluyendo su ID de usuario y nombre de usuario.
        """
        return f"User(user_id={self.user_id}, username='{self.username}')"

    @classmethod
    def from_dict(cls, data_dict):
        """
        Crea una instancia de User a partir de un diccionario.

        Permite instanciar un objeto `User` directamente desde un diccionario, asumiendo que
        las claves del diccionario coinciden con los nombres de los atributos de la clase `User`.

        Args:
            data_dict (dict): Diccionario que contiene los datos del usuario. Debe tener las claves:
                               'username', 'password', y opcionalmente 'user_id'.

        Returns:
            User: Una nueva instancia de la clase `User` creada con los datos del diccionario.
        """
        return cls(**data_dict)
