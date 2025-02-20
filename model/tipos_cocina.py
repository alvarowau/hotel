class TiposCocina:
    def __init__(self, tipo_cocina_id, nombre):
        self.tipo_cocina_id = tipo_cocina_id
        self.nombre = nombre

    def __repr__(self):
        return (
            f"Tipo Cocina(tipo_cocina_id={self.tipo_cocina_id}, nombre='{self.nombre}')"
        )

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)
