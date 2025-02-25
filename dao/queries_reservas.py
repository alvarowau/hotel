
create = """
INSERT INTO reservas (tipo_reserva_id, salon_id, tipo_cocina_id, id_cliente, fecha, ocupacion, jornadas, habitaciones)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""
find_all = "SELECT * FROM reservas"

find_byId = "SELECT * FROM reservas WHERE reserva_id = %s"

find_all_by_id_salones = "SELECT * FROM reservas WHERE salon_id = %s"

update = """
UPDATE reservas
SET tipo_reserva_id = %s, salon_id = %s, tipo_cocina_id = %s, id_cliente = %s,
    fecha = %s, ocupacion = %s, jornadas = %s, habitaciones = %s
WHERE reserva_id = %s
"""
details_delete = """
SELECT c.Nombre, c.Apellidos, r.fecha
FROM reservas r
JOIN clientes c ON r.id_cliente = c.id
WHERE r.reserva_id = %s;

"""

is_date_dispon = """
SELECT COUNT(*)
FROM reservas
WHERE salon_id = %s AND fecha = %s;
"""

delete = "DELETE FROM reservas WHERE reserva_id = %s"
