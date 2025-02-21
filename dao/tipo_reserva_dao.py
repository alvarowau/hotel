from dao.queries import tipo_reserva_dao_find_all
from model.tipo_reservas import TipoReservas

class TipoReservasDao:
    def __init__(self, conexion):
        self.conexion = conexion

    def find_all(self):
        if self.conexion:
            cursor = self.conexion.cursor(dictionary=True)
            try:
                cursor.execute(tipo_reserva_dao_find_all)
                result = cursor.fetchall()
                lista_tipo_reservas = list()
                for tipo in result:
                    lista_tipo_reservas.append(self.convertir_tipo_reservas(tipo))
                return lista_tipo_reservas
            finally:
                cursor.close()
        return None

    def convertir_tipo_reservas(self, tipo_reserva):
        return TipoReservas.from_dict(tipo_reserva)
