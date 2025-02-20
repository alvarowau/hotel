from dao.reserva_dao import ReservaDao


def reserva_dao_findall(reserva_dao: ReservaDao):
    print("")
    print("-------Listar reserva-------")
    result = reserva_dao.find_all()
    if result:
        for reserva in result:
            print(reserva)


def reserva_dao_findById(reserva_dao: ReservaDao, id):
    print("")
    print(f"--------Reserva por id {id}--------")
    result = reserva_dao.find_by_id(id)
    print(result)


def reserva_dao_update(reserva_dao :ReservaDao):
    print("")
    print("----Edicicion de reserva-----")
    reserva = reserva_dao.find_by_id(16)
    if reserva:
        reserva.id_cliente = 12
        result = reserva_dao.update(reserva)
        print(f"la reserva se actualizo correctamente: {result}")
    else:
        print("No se encontro reserva")
