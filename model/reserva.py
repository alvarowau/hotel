class Reserva:
    def __init__(
        self,
        reserva_id=None,
        tipo_reserva_id=None,
        salon_id=None,
        tipo_cocina_id=None,
        id_Cliente=None,
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
            id_Cliente (int, requerido): Identificador del cliente que hace la reserva.
            fecha (date, requerido): Fecha de la reserva.
            ocupacion (int, requerido): Número de personas en la reserva.
            jornadas (int, requerido): Número de jornadas de la reserva.
            habitaciones (int, opcional): Número de habitaciones reservadas (por defecto 0).
        """
        self.reserva_id = reserva_id
        self.tipo_reserva_id = tipo_reserva_id
        self.salon_id = salon_id
        self.tipo_cocina_id = tipo_cocina_id
        self.id_Cliente = id_Cliente
        self.fecha = fecha
        self.ocupacion = ocupacion
        self.jornadas = jornadas
        self.habitaciones = habitaciones

    def __str__(self):
        """
        Método para representar el objeto Reserva como una cadena (string).
        Útil para debuggear o imprimir información de la reserva.
        """
        return f"Reserva(reserva_id={self.reserva_id}, cliente_id={self.id_Cliente}, fecha={self.fecha}, ocupacion={self.ocupacion}, jornadas={self.jornadas}, habitaciones={self.habitaciones})"

    @classmethod
    def from_dict(cls, data_dict):
        """
        Método de clase para crear un objeto Reserva a partir de un diccionario.

        Args:
            data_dict (dict): Diccionario que contiene los datos de la reserva.
                              Las claves del diccionario deberían corresponder
                              a los atributos de la clase Reserva (reserva_id, tipo_reserva_id, etc.).

        Returns:
            Reserva: Un nuevo objeto Reserva instanciado con los datos del diccionario.
        """
        return cls(**data_dict)
