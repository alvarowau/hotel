find_all_actives = "SELECT * FROM clientes WHERE activo = True"


find_nombre_by_id = "SELECT nombre, apellidos FROM clientes WHERE id = %s"

find_by_id = "SELECT * FROM clientes WHERE id = %s AND activo = True"


desctivate = "UPDATE clientes SET activo = NOT activo WHERE Id = %s"


exit_num_identificacion = "SELECT COUNT(*) FROM clientes WHERE Num_Identificacion = %s"


update = """
UPDATE clientes
SET Nombre = %s, Apellidos = %s, Fec_Nac = %s, Pais = %s,
    Telefono = %s, email = %s, Sexo = %s, Menores = %s, Num_Identificacion = %s
WHERE Id = %s;
"""


create = """
INSERT INTO clientes (
    Nombre, Apellidos, Num_Identificacion, Fec_Nac, Pais, Telefono, email, Sexo, Menores, activo
) VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
)
"""
