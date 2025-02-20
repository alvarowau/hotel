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
