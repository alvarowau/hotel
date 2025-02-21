class TiposCocina:
    """
    Representa un tipo de cocina en el sistema.

    Atributos:
        tipo_cocina_id (int): Identificador único del tipo de cocina.
        nombre (str): Nombre del tipo de cocina.
    """

    def __init__(self, tipo_cocina_id, nombre):
        """
        Inicializa una nueva instancia de la clase TiposCocina.

        Args:
            tipo_cocina_id (int): Identificador único del tipo de cocina.
            nombre (str): Nombre del tipo de cocina.
        """
        self._tipo_cocina_id = tipo_cocina_id
        self._nombre = nombre

    def __repr__(self):
        """
        Devuelve una representación en forma de cadena del tipo de cocina.

        Returns:
            str: Cadena que representa el tipo de cocina.
        """
        return f"Tipo Cocina(tipo_cocina_id={self._tipo_cocina_id}, nombre='{self._nombre}')"

    @classmethod
    def from_dict(cls, data_dict):
        """
        Crea una instancia de TiposCocina a partir de un diccionario de datos.

        Args:
            data_dict (dict): Diccionario con los datos del tipo de cocina.

        Returns:
            TiposCocina: Instancia de la clase TiposCocina.
        """
        return cls(**data_dict)

    # Getters y Setters

    @property
    def tipo_cocina_id(self):
        """Obtiene el identificador del tipo de cocina."""
        return self._tipo_cocina_id

    @tipo_cocina_id.setter
    def tipo_cocina_id(self, value):
        """Establece el identificador del tipo de cocina."""
        self._tipo_cocina_id = value

    @property
    def nombre(self):
        """Obtiene el nombre del tipo de cocina."""
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        """Establece el nombre del tipo de cocina."""
        self._nombre = value
