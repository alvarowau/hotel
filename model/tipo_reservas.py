class TipoReservas:
    """
    Representa un tipo de reserva en el sistema.

    Atributos:
        tipo_reserva_id (int): Identificador único del tipo de reserva.
        nombre (str): Nombre del tipo de reserva.
        requiere_jornadas (bool): Indica si el tipo de reserva requiere jornadas.
        requiere_habitaciones (bool): Indica si el tipo de reserva requiere habitaciones.
    """

    def __init__(
        self, tipo_reserva_id, nombre, requiere_jornadas, requiere_habitaciones
    ):
        """
        Inicializa una nueva instancia de la clase TipoReservas.

        Args:
            tipo_reserva_id (int): Identificador único del tipo de reserva.
            nombre (str): Nombre del tipo de reserva.
            requiere_jornadas (bool): Indica si el tipo de reserva requiere jornadas.
            requiere_habitaciones (bool): Indica si el tipo de reserva requiere habitaciones.
        """
        self._tipo_reserva_id = tipo_reserva_id
        self._nombre = nombre
        self._requiere_jornadas = requiere_jornadas
        self._requiere_habitaciones = requiere_habitaciones

    def __repr__(self):
        """
        Devuelve una representación en forma de cadena del tipo de reserva.

        Returns:
            str: Cadena que representa el tipo de reserva.
        """
        return f"Tipo Reservas(tipo_reserva_id={self._tipo_reserva_id}, nombre='{self._nombre}', requiere_jornadas='{self._requiere_jornadas}', requiere_habitaciones='{self._requiere_habitaciones}')"

    @classmethod
    def from_dict(cls, data_dict):
        """
        Crea una instancia de TipoReservas a partir de un diccionario de datos.

        Args:
            data_dict (dict): Diccionario con los datos del tipo de reserva.

        Returns:
            TipoReservas: Instancia de la clase TipoReservas.
        """
        return cls(**data_dict)

    # Getters y Setters

    @property
    def tipo_reserva_id(self):
        """Obtiene el identificador del tipo de reserva."""
        return self._tipo_reserva_id

    @tipo_reserva_id.setter
    def tipo_reserva_id(self, value):
        """Establece el identificador del tipo de reserva."""
        self._tipo_reserva_id = value

    @property
    def nombre(self):
        """Obtiene el nombre del tipo de reserva."""
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        """Establece el nombre del tipo de reserva."""
        self._nombre = value

    @property
    def requiere_jornadas(self):
        """Indica si el tipo de reserva requiere jornadas."""
        return self._requiere_jornadas

    @requiere_jornadas.setter
    def requiere_jornadas(self, value):
        """Establece si el tipo de reserva requiere jornadas."""
        self._requiere_jornadas = value

    @property
    def requiere_habitaciones(self):
        """Indica si el tipo de reserva requiere habitaciones."""
        return self._requiere_habitaciones

    @requiere_habitaciones.setter
    def requiere_habitaciones(self, value):
        """Establece si el tipo de reserva requiere habitaciones."""
        self._requiere_habitaciones = value
