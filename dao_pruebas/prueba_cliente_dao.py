from dao.clientes_dao import ClienteDao
from model.cliente import Cliente


def cliente_dao_findall(cliente_dao: ClienteDao):
    print("")
    print("--------listar Clientes activos------")
    print("")
    lista_clientes = cliente_dao.find_all_activos()
    if lista_clientes:
        for cliente in lista_clientes:
            print(type(cliente))
            print(cliente)


def cliente_dao_find_byId(cliente_dao: ClienteDao, id):
    print("--------Cliente por id--------")
    print("")
    cliente = cliente_dao.find_all_by_id(18)
    print(cliente)


def cliente_dao_update(cliente_dao: ClienteDao):
    print("--------Actualizar Cliente--------")
    print("")
    result = cliente_dao.update(
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


def cliente_dao_desactivate(cliente_dao: ClienteDao):
    print("--------Desactivar Cliente--------")
    print("")
    result = cliente_dao.deactivate(2)
    print(f"El cliente se desactivo: {result}")


def cliente_dao_create(cliente_dao: ClienteDao):
    print("--------Crear Cliente--------")
    print("")
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

    result = cliente_dao.create(nuevo_cliente)
    if result:
        print("Cliente creado correctamente.")
    else:
        print("No se pudo crear el cliente.")
