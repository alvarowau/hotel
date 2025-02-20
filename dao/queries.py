user_dao_login = "SELECT COUNT(*) FROM users WHERE username = %s AND password = %s"


clientes_dao_find_all_actives = "SELECT * FROM clientes WHERE activo = True"
clientes_dao_find_by_id = "SELECT * FROM clientes WHERE id = %s AND activo = True"
clientes_dao_desctivate = "UPDATE clientes SET activo = NOT activo WHERE Id = %s"
cliente_dao_update = "UPDATE clientes SET Nombre = %s, Apellidos = %s, Fec_Nac = %s, Pais = %s, Telefono = %s, email = %s, Sexo = %s, Menores = %s, activo = %s WHERE Id = %s"
cliente_dao_create = """
INSERT INTO clientes (
    Nombre, Apellidos, Num_Identificacion, Fec_Nac, Pais, Telefono, email, Sexo, Menores, activo
) VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
)
"""


salones_dao_find_all = "SELECT * FROM salones"

tipo_cocina_dao_find_all = "SELECT * FROM tipos_cocina"
