class TipoReservas:
    def __init__(self, tipo_reserva_id, nombre, requiere_jornadas, requiere_habitaciones):
        self.tipo_reserva_id = tipo_reserva_id
        self.nombre = nombre
        self.requiere_jornadas = requiere_jornadas
        self.requiere_habitaciones = requiere_habitaciones

    def __repr__(self):
        return f"Tipo Reservas(tipo_reserva_id={self.tipo_reserva_id}, nombre='{self.nombre}', requiere_jornadas='{self.requiere_jornadas}', requiere_habitaciones='{self.requiere_habitaciones}')"

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)
