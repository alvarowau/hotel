class Salon:
    def __init__(self, salon_id, nombre):
        self.salon_id = salon_id
        self.nombre = nombre

    def __repr__(self):
        return f"Salon(salon_id={self.salon_id}, nombre='{self.nombre}')"

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)
