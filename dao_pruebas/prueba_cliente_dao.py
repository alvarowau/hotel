from dao.clientes_dao import ClienteDao
from model.cliente import Cliente


def cliente_dao_findall(cliente_dao: ClienteDao):
    """Muestra todos los clientes activos desde el DAO.

    Args:
        cliente_dao (ClienteDao): Objeto del DAO encargado de manejar las operaciones de cliente.
    """
    print("-------- Listar Clientes Activos --------")
    lista_clientes = cliente_dao.find_all_activos()
    if lista_clientes:
        for cliente in lista_clientes:
            print(cliente)
    else:
        print("No se encontraron clientes activos.")


def cliente_dao_find_byId(cliente_dao: ClienteDao, id):
    """Muestra un cliente específico por su ID desde el DAO.

    Args:
        cliente_dao (ClienteDao): Objeto del DAO encargado de manejar las operaciones de cliente.
        id (int): El ID del cliente que se busca.
    """
    print(f"-------- Cliente por ID {id} --------")
    cliente = cliente_dao.find_all_by_id(id)
    if cliente:
        print(cliente)
    else:
        print(f"No se encontró un cliente con ID {id}.")


def cliente_dao_update(cliente_dao: ClienteDao):
    """Actualiza la información de un cliente en el DAO.

    Args:
        cliente_dao (ClienteDao): Objeto del DAO encargado de manejar las operaciones de cliente.
    """
    print("-------- Actualizar Cliente --------")
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
    if result:
        print("El cliente con ID 18 se actualizó correctamente.")
    else:
        print("No se pudo actualizar el cliente.")


def cliente_dao_desactivate(cliente_dao: ClienteDao):
    """Desactiva un cliente en el DAO.

    Args:
        cliente_dao (ClienteDao): Objeto del DAO encargado de manejar las operaciones de cliente.
    """
    print("-------- Desactivar Cliente --------")
    result = cliente_dao.deactivate(2)
    if result:
        print("El cliente con ID 2 se desactivó correctamente.")
    else:
        print("No se pudo desactivar el cliente.")


def cliente_dao_create(cliente_dao: ClienteDao):
    """Crea un nuevo cliente en el DAO.

    Args:
        cliente_dao (ClienteDao): Objeto del DAO encargado de manejar las operaciones de cliente.
    """
    print("-------- Crear Cliente --------")
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
