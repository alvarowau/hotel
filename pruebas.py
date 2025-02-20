from bbdd.conexion_mysql import MySQLConnectionManager
from dao.clientes_dao import ClienteDao
from model.clientes import Cliente


def inicio_pruebas():
    base_datos = MySQLConnectionManager(
        host="localhost", user="hotel", password="hotel", database="hotel"
    )
    conexion = base_datos.connect()
    cliente_dao_pruebas(conexion)


def cliente_dao_pruebas(conexion):
    cliente_dao = ClienteDao(conexion)
    __cliente_dao_create(cliente_dao)
    __cliente_dao_findall(cliente_dao)
    """print("--------Cliente por id--------")
    print("")
    __cliente_dao_find_byId(cliente_dao)
    print("")
    print("--------Desactivar cliente------")
    print("")
    __cliente_dao_desactivate(cliente_dao)
    print("")
    print("--------listar Clientes activos------")
    print("")
    __cliente_dao_findall(cliente_dao)
    print("--------Cliente por id antes de modificar--------")
    print("")
    __cliente_dao_find_byId(cliente_dao)
    print("--------Modificar cliente--------")
    print("")
    __cliente_dao_update(cliente_dao)
    print("--------Cliente por id despues de modificar--------")
    print("")
    __cliente_dao_find_byId(cliente_dao)"""


def __cliente_dao_findall(cliente_dao: ClienteDao):
    lista_clientes = cliente_dao.find_all_activos()
    if lista_clientes:
        for cliente in lista_clientes:
            print(type(cliente))
            print(cliente)


def __cliente_dao_find_byId(cliente_dao: ClienteDao):
    cliente = cliente_dao.find_all_by_id(18)
    print(cliente)

def __cliente_dao_update(cliente_dao: ClienteDao):
    result = cliente_dao.actualizar_cliente(
        id=18,
        nombre="Juan",
        apellidos="Pérez",
        fec_nac="1990-05-15",
        pais="México",
        telefono="555-1234",
        email="juan.perez@example.com",
        sexo="M",
        menores=2,
        activo=True,
    )

    print(f"El resultado de la modificacion es: {result}")


def __cliente_dao_desactivate(cliente_dao: ClienteDao):
    result = cliente_dao.desactive_clientes(2)
    print(f"El cliente se desactivo: {result}")

def __cliente_dao_create(cliente_dao:ClienteDao):
    nuevo_cliente = Cliente(
        Nombre="Carlos",
        Apellidos="Ramírez",
        Num_Identificacion="12345678X",
        Fec_Nac="1985-09-20",
        Pais="España",
        Telefono="666-7890",
        email="carlos.ramirez@example.com",
        Sexo="M",
        Menores=1,
        activo=True,
    )

    result = cliente_dao.crear_cliente(nuevo_cliente)
    if result:
        print("Cliente creado correctamente.")
    else:
        print("No se pudo crear el cliente.")


if __name__ == "__main__":
    inicio_pruebas()
