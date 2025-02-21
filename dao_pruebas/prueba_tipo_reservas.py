from dao.tipo_reserva_dao import TipoReservasDao


def tipo_reservas_dao_find_all(tipo_reservas_dao: TipoReservasDao):
    """Muestra una lista de todos los tipos de reserva desde el DAO.

    Args:
        tipo_reservas_dao (TipoReservasDao): Objeto del DAO encargado de manejar las operaciones de tipo de reserva.
    """
    print("------- Listado de Tipos de Reserva -------")
    print("")
    result = tipo_reservas_dao.find_all()
    if result:
        for tipo in result:
            print(tipo)
    else:
        print("No se han recibido tipos de reserva.")
