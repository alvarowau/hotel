from dao.queries import tipo_cocina_dao_find_all
from model.tipos_cocina import TiposCocina


class TipoCocinaDao:
    def __init__(self, conexion):
        self.conexion = conexion

    def find_all(self):
        if self.conexion:
            cursor = self.conexion.cursor(dictionary=True)
            try:
                cursor.execute(tipo_cocina_dao_find_all)
                result = cursor.fetchall()
                tipos_cocina = list()
                for cocina in result:
                    tipos_cocina.append(
                        self.convertir_tipo_cocina(cocina)
                    )
                return tipos_cocina
            finally:
                cursor.close()
        else:
            return None

    def convertir_tipo_cocina(self, cocina):
        return TiposCocina.from_dict(cocina)
