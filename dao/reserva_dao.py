from dao.queries import reservas_dao_find_all, reservas_dao_find_byId
from model.reserva import Reserva

class ReservaDao:
    def __init__(self, conexion):
        self.conexion = conexion

    def find_all(self):
        if self.conexion:
            cursor = self.conexion.cursor(dictionary=True)
            try:
                cursor.execute(reservas_dao_find_all)
                result = cursor.fetchall()
                lista_reserva = list()
                for res in result:
                    lista_reserva.append(
                        self.convertir_reserva(res)
                    )
                return lista_reserva
            finally:
                cursor.close()
        return None

    def find_by_id(self, id):
        if self.conexion:
            cursor = self.conexion.cursor(dictionary=True)
            try:
                cursor.execute(reservas_dao_find_byId, (id,))
                result = cursor.fetchone()
                return self.convertir_reserva(result)
            finally:
                cursor.close()
        return None

    def convertir_reserva(self, reserva):
        return Reserva.from_dict(reserva)
