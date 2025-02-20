from typing import Optional


class User:
    """
    Representa a un usuario con un identificador opcional, nombre de usuario y contraseña.
    """

    def __init__(self, username: str, password: str, user_id: Optional[int] = None):
        self.user_id: Optional[int] = user_id
        self.username: str = username
        self.password: str = password

    def __repr__(self):
        return f"User(user_id={self.user_id}, username='{self.username}')"
