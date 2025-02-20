from dao.tipo_cocina_dao import TipoCocinaDao


def tipo_cocina_dao_findall(tipo_cocina_dao: TipoCocinaDao):
    print("----Listar tipo Cocina-----")
    print("")
    result = tipo_cocina_dao.find_all()
    if result:
        for cocina in result:
            print(cocina)
    else:
        print("No se han recivido cocinas")
