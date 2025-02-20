class Reserva:
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
        Constructor de la clase Reserva.

        Args:
            reserva_id (int, opcional): Identificador único de la reserva (clave primaria).
            tipo_reserva_id (int, requerido): Identificador del tipo de reserva.
            salon_id (int, requerido): Identificador del salón.
            tipo_cocina_id (int, requerido): Identificador del tipo de cocina.
            id_cliente (int, requerido): Identificador del cliente que hace la reserva.
            fecha (date, requerido): Fecha de la reserva.
            ocupacion (int, requerido): Número de personas en la reserva.
            jornadas (int, requerido): Número de jornadas de la reserva.
            habitaciones (int, opcional): Número de habitaciones reservadas (por defecto 0).
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
        Representación en cadena del objeto Reserva.
        """
        return f"Reserva(reserva_id={self._reserva_id}, cliente_id={self._id_cliente}, fecha={self._fecha}, ocupacion={self._ocupacion}, jornadas={self._jornadas}, habitaciones={self._habitaciones})"

    @classmethod
    def from_dict(cls, data_dict):
        """
        Método de clase para crear un objeto Reserva a partir de un diccionario.

        Args:
            data_dict (dict): Diccionario con los datos de la reserva.

        Returns:
            Reserva: Un nuevo objeto Reserva instanciado con los datos del diccionario.
        """
        return cls(**data_dict)

    # GETTERS y SETTERS
    @property
    def reserva_id(self):
        return self._reserva_id

    @reserva_id.setter
    def reserva_id(self, value):
        self._reserva_id = value

    @property
    def tipo_reserva_id(self):
        return self._tipo_reserva_id

    @tipo_reserva_id.setter
    def tipo_reserva_id(self, value):
        self._tipo_reserva_id = value

    @property
    def salon_id(self):
        return self._salon_id

    @salon_id.setter
    def salon_id(self, value):
        self._salon_id = value

    @property
    def tipo_cocina_id(self):
        return self._tipo_cocina_id

    @tipo_cocina_id.setter
    def tipo_cocina_id(self, value):
        self._tipo_cocina_id = value

    @property
    def id_cliente(self):
        return self._id_cliente

    @id_cliente.setter
    def id_cliente(self, value):
        self._id_cliente = value

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, value):
        self._fecha = value

    @property
    def ocupacion(self):
        return self._ocupacion

    @ocupacion.setter
    def ocupacion(self, value):
        self._ocupacion = value

    @property
    def jornadas(self):
        return self._jornadas

    @jornadas.setter
    def jornadas(self, value):
        self._jornadas = value

    @property
    def habitaciones(self):
        return self._habitaciones

    @habitaciones.setter
    def habitaciones(self, value):
        self._habitaciones = value
