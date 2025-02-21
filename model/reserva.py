class Reserva:
    """
    Representa una reserva en el sistema.

    Atributos:
        reserva_id (int, opcional): Identificador único de la reserva.
        tipo_reserva_id (int, opcional): Tipo de reserva.
        salon_id (int, opcional): Identificador del salón asociado con la reserva.
        tipo_cocina_id (int, opcional): Tipo de cocina para la reserva.
        id_cliente (int, opcional): Identificador del cliente que realiza la reserva.
        fecha (str, opcional): Fecha de la reserva.
        ocupacion (int, opcional): Número de personas en la reserva.
        jornadas (int, opcional): Número de jornadas de la reserva.
        habitaciones (int, opcional): Número de habitaciones reservadas. Por defecto es 0.
    """

    def __init__(
        self,
        reserva_id=None,
        tipo_reserva_id=None,
        salon_id=None,
        tipo_cocina_id=None,
        id_cliente=None,
        fecha=None,
        ocupacion=None,
        jornadas=None,
        habitaciones=0,
    ):
        """
        Inicializa una nueva instancia de la clase Reserva.

        Args:
            reserva_id (int, opcional): Identificador único de la reserva.
            tipo_reserva_id (int, opcional): Tipo de reserva.
            salon_id (int, opcional): Identificador del salón asociado con la reserva.
            tipo_cocina_id (int, opcional): Tipo de cocina para la reserva.
            id_cliente (int, opcional): Identificador del cliente que realiza la reserva.
            fecha (str, opcional): Fecha de la reserva.
            ocupacion (int, opcional): Número de personas en la reserva.
            jornadas (int, opcional): Número de jornadas de la reserva.
            habitaciones (int, opcional): Número de habitaciones reservadas.
        """
        self._reserva_id = reserva_id
        self._tipo_reserva_id = tipo_reserva_id
        self._salon_id = salon_id
        self._tipo_cocina_id = tipo_cocina_id
        self._id_cliente = id_cliente
        self._fecha = fecha
        self._ocupacion = ocupacion
        self._jornadas = jornadas
        self._habitaciones = habitaciones

    def __str__(self):
        """
        Devuelve una representación en forma de cadena de la reserva.

        Returns:
            str: Cadena que representa la reserva.
        """
        return f"Reserva(reserva_id={self._reserva_id}, cliente_id={self._id_cliente}, fecha={self._fecha}, ocupacion={self._ocupacion}, jornadas={self._jornadas}, habitaciones={self._habitaciones})"

    @classmethod
    def from_dict(cls, data_dict):
        """
        Crea una instancia de Reserva a partir de un diccionario de datos.

        Args:
            data_dict (dict): Diccionario con los datos de la reserva.

        Returns:
            Reserva: Instancia de la clase Reserva.
        """
        return cls(**data_dict)

    # Getters y Setters

    @property
    def reserva_id(self):
        """Obtiene el identificador de la reserva."""
        return self._reserva_id

    @reserva_id.setter
    def reserva_id(self, value):
        """Establece el identificador de la reserva."""
        self._reserva_id = value

    @property
    def tipo_reserva_id(self):
        """Obtiene el tipo de reserva."""
        return self._tipo_reserva_id

    @tipo_reserva_id.setter
    def tipo_reserva_id(self, value):
        """Establece el tipo de reserva."""
        self._tipo_reserva_id = value

    @property
    def salon_id(self):
        """Obtiene el identificador del salón asociado con la reserva."""
        return self._salon_id

    @salon_id.setter
    def salon_id(self, value):
        """Establece el identificador del salón asociado con la reserva."""
        self._salon_id = value

    @property
    def tipo_cocina_id(self):
        """Obtiene el tipo de cocina para la reserva."""
        return self._tipo_cocina_id

    @tipo_cocina_id.setter
    def tipo_cocina_id(self, value):
        """Establece el tipo de cocina para la reserva."""
        self._tipo_cocina_id = value

    @property
    def id_cliente(self):
        """Obtiene el identificador del cliente que realiza la reserva."""
        return self._id_cliente

    @id_cliente.setter
    def id_cliente(self, value):
        """Establece el identificador del cliente que realiza la reserva."""
        self._id_cliente = value

    @property
    def fecha(self):
        """Obtiene la fecha de la reserva."""
        return self._fecha

    @fecha.setter
    def fecha(self, value):
        """Establece la fecha de la reserva."""
        self._fecha = value

    @property
    def ocupacion(self):
        """Obtiene el número de personas en la reserva."""
        return self._ocupacion

    @ocupacion.setter
    def ocupacion(self, value):
        """Establece el número de personas en la reserva."""
        self._ocupacion = value

    @property
    def jornadas(self):
        """Obtiene el número de jornadas de la reserva."""
        return self._jornadas

    @jornadas.setter
    def jornadas(self, value):
        """Establece el número de jornadas de la reserva."""
        self._jornadas = value

    @property
    def habitaciones(self):
        """Obtiene el número de habitaciones reservadas."""
        return self._habitaciones

    @habitaciones.setter
    def habitaciones(self, value):
        """Establece el número de habitaciones reservadas."""
        self._habitaciones = value
