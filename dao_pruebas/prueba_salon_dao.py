from dao.salones_dao import SalonDao


def salon_dao_findall(salon_dao: SalonDao):
    """Muestra una lista de todos los salones desde el DAO.

    Args:
        salon_dao (SalonDao): Objeto del DAO encargado de manejar las operaciones de salón.
    """
    print("--------- Listado de Salones ---------")
    result = salon_dao.find_all()
    if result:
        for salon in result:
            print(salon)
    else:
        print("No se han recibido salones.")
