from dao.tipo_cocina_dao import TipoCocinaDao


def tipo_cocina_dao_findall(tipo_cocina_dao: TipoCocinaDao):
    """Muestra una lista de todos los tipos de cocina desde el DAO.

    Args:
        tipo_cocina_dao (TipoCocinaDao): Objeto del DAO encargado de manejar las operaciones de tipo de cocina.
    """
    print("---- Listado de Tipos de Cocina ----")
    print("")
    result = tipo_cocina_dao.find_all()
    if result:
        for cocina in result:
            print(cocina)
    else:
        print("No se han recibido tipos de cocina.")
