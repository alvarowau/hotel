from bbdd.conexion_mysql import MySQLConnectionManager
from dao.clientes_dao import ClienteDao
from dao.salones_dao import SalonDao
from dao_pruebas.prueba_cliente_dao import (
    cliente_dao_create,
    cliente_dao_desactivate,
    cliente_dao_find_byId,
    cliente_dao_findall,
    cliente_dao_update,
)
from dao_pruebas.prueba_salon_dao import salon_dao_findall


def inicio_pruebas():
    base_datos = MySQLConnectionManager(
        host="localhost", user="hotel", password="hotel", database="hotel"
    )
    conexion = base_datos.connect()
    # cliente_dao_pruebas(conexion)
    salones_dao_pruebas(conexion)


def cliente_dao_pruebas(conexion):
    cliente_dao = ClienteDao(conexion)
    cliente_dao_find_byId(cliente_dao, 2)
    cliente_dao_findall(cliente_dao)
    cliente_dao_desactivate(cliente_dao)
    cliente_dao_update(cliente_dao)
    cliente_dao_create(cliente_dao)


def salones_dao_pruebas(conexion):
    salon_dao = SalonDao(conexion)
    salon_dao_findall(salon_dao)


if __name__ == "__main__":
    inicio_pruebas()
