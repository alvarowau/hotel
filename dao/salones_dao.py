from dao.queris import salones_dao_find_all
from model.salon import Salon


class SalonDao:
    def __init__(self, conexion):
        self.conexion = conexion

    def find_all(self):
        if self.conexion:
            cursor = self.conexion.cursor(dictionary=True)
            try:
                cursor.execute(salones_dao_find_all)
                result = cursor.fetchall()
                lista_salones = list()
                for sal in result:
                    lista_salones.append(self.convertir_salon(sal))
                return lista_salones
            finally:
                cursor.close()
        return None

    def convertir_salon(self, salon):
        return Salon.from_dict(salon)
