class Salon:
    """
    Representa un salón en el sistema.

    Atributos:
        salon_id (int): Identificador único del salón.
        nombre (str): Nombre del salón.
    """

    def __init__(self, salon_id, nombre):
        """
        Inicializa una nueva instancia de la clase Salon.

        Args:
            salon_id (int): Identificador único del salón.
            nombre (str): Nombre del salón.
        """
        self._salon_id = salon_id
        self._nombre = nombre

    def __repr__(self):
        """
        Devuelve una representación en forma de cadena del salón.

        Returns:
            str: Cadena que representa el salón.
        """
        return f"Salon(salon_id={self._salon_id}, nombre='{self._nombre}')"

    @classmethod
    def from_dict(cls, data_dict):
        """
        Crea una instancia de Salon a partir de un diccionario de datos.

        Args:
            data_dict (dict): Diccionario con los datos del salón.

        Returns:
            Salon: Instancia de la clase Salon.
        """
        return cls(**data_dict)

    # Getters y Setters

    @property
    def salon_id(self):
        """Obtiene el identificador del salón."""
        return self._salon_id

    @salon_id.setter
    def salon_id(self, value):
        """Establece el identificador del salón."""
        self._salon_id = value

    @property
    def nombre(self):
        """Obtiene el nombre del salón."""
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        """Establece el nombre del salón."""
        self._nombre = value
