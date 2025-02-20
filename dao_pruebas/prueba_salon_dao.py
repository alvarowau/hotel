from dao.salones_dao import SalonDao


def salon_dao_findall(salon_dao: SalonDao):
    print("---------Listar salones---------")
    result = salon_dao.find_all()
    if result:
        for salon in result:
            print(salon)
    else:
        print("no hay salones")
