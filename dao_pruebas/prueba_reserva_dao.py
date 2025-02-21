from dao.reserva_dao import ReservaDao
from model.reserva import Reserva


def reserva_dao_findall(reserva_dao: ReservaDao):
    """Muestra una lista de todas las reservas desde el DAO.

    Args:
        reserva_dao (ReservaDao): Objeto del DAO encargado de manejar las operaciones de reserva.
    """
    print("------- Listado de Reservas -------")
    result = reserva_dao.find_all()
    if result:
        for reserva in result:
            print(reserva)


def reserva_dao_findById(reserva_dao: ReservaDao, id):
    """Muestra una reserva específica por su ID desde el DAO.

    Args:
        reserva_dao (ReservaDao): Objeto del DAO encargado de manejar las operaciones de reserva.
        id (int): El ID de la reserva que se busca.
    """
    print(f"-------- Reserva por ID {id} --------")
    result = reserva_dao.find_by_id(id)
    if result:
        print(result)
    else:
        print(f"No se encontró una reserva con ID {id}.")


def reserva_dao_update(reserva_dao: ReservaDao):
    """Actualiza una reserva en el DAO.

    Args:
        reserva_dao (ReservaDao): Objeto del DAO encargado de manejar las operaciones de reserva.
    """
    print("---- Edición de Reserva ----")
    reserva = reserva_dao.find_by_id(16)
    if reserva:
        reserva.id_cliente = 12
        result = reserva_dao.update(reserva)
        if result:
            print(f"La reserva se actualizó correctamente: {result}")
        else:
            print("No se pudo actualizar la reserva.")
    else:
        print("No se encontró la reserva con ID 16.")


def reserva_dao_create(reserva_dao: ReservaDao):
    """Crea una nueva reserva en el DAO.

    Args:
        reserva_dao (ReservaDao): Objeto del DAO encargado de manejar las operaciones de reserva.
    """
    print("----- Creación de Reserva -----")
    reserva = Reserva(
        tipo_reserva_id=2,
        salon_id=2,
        tipo_cocina_id=1,
        id_cliente=5,
        fecha="2025-02-22",
        ocupacion=4,
        jornadas=2,
        habitaciones=1,
    )
    result = reserva_dao.create(reserva)
    if result:
        print("La reserva se creó correctamente.")
    else:
        print("La reserva NO se pudo crear.")
