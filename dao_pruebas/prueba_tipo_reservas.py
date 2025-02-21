from dao.tipo_reserva_dao import TipoReservasDao

def tipo_reservas_dao_find_all(tipo_reservas_dao :TipoReservasDao):
    print("-------Listar tipo reservas-------")
    print("")
    result = tipo_reservas_dao.find_all()
    if result:
        for tipo in result:
            print(tipo)
    else:
        print("no se ha recivodo tipos de reservas")
