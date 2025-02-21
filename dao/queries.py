# Consultas relacionadas con usuarios
user_dao_login = "SELECT COUNT(*) FROM users WHERE username = %s AND password = %s"
"""
Consulta SQL para verificar las credenciales de un usuario.

Returns:
    int: Número de coincidencias encontradas (0 si no hay coincidencias, 1 si las credenciales son válidas).
"""

# Consultas relacionadas con clientes
clientes_dao_find_all_actives = "SELECT * FROM clientes WHERE activo = True"
"""
Consulta SQL para obtener todos los clientes activos.

Returns:
    list[dict]: Lista de diccionarios con los datos de los clientes activos.
"""

clientes_dao_find_by_id = "SELECT * FROM clientes WHERE id = %s AND activo = True"
"""
Consulta SQL para buscar un cliente por su ID, siempre que esté activo.

Args:
    id (int): El ID del cliente a buscar.

Returns:
    dict: Un diccionario con los datos del cliente encontrado.
"""

clientes_dao_desctivate = "UPDATE clientes SET activo = NOT activo WHERE Id = %s"
"""
Consulta SQL para desactivar o reactivar un cliente por su ID.

Args:
    id (int): El ID del cliente a desactivar o reactivar.

Returns:
    bool: True si la operación fue exitosa, False en caso contrario.
"""

cliente_dao_update = """
UPDATE clientes
SET Nombre = %s, Apellidos = %s, Fec_Nac = %s, Pais = %s,
    Telefono = %s, email = %s, Sexo = %s, Menores = %s, activo = %s
WHERE Id = %s;
"""
"""
Consulta SQL para actualizar los datos de un cliente.

Args:
    Nombre (str): Nombre del cliente.
    Apellidos (str): Apellidos del cliente.
    Fec_Nac (str): Fecha de nacimiento del cliente.
    Pais (str): País del cliente.
    Telefono (str): Teléfono del cliente.
    email (str): Correo electrónico del cliente.
    Sexo (str): Sexo del cliente.
    Menores (int): Número de menores a cargo del cliente.
    activo (bool): Estado de activación del cliente.
    Id (int): ID del cliente a actualizar.

Returns:
    bool: True si la actualización fue exitosa, False en caso contrario.
"""

cliente_dao_create = """
INSERT INTO clientes (
    Nombre, Apellidos, Num_Identificacion, Fec_Nac, Pais, Telefono, email, Sexo, Menores, activo
) VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
)
"""
"""
Consulta SQL para crear un nuevo cliente.

Args:
    Nombre (str): Nombre del cliente.
    Apellidos (str): Apellidos del cliente.
    Num_Identificacion (str): Número de identificación del cliente.
    Fec_Nac (str): Fecha de nacimiento del cliente.
    Pais (str): País del cliente.
    Telefono (str): Teléfono del cliente.
    email (str): Correo electrónico del cliente.
    Sexo (str): Sexo del cliente.
    Menores (int): Número de menores a cargo del cliente.
    activo (bool): Estado de activación del cliente.

Returns:
    bool: True si la creación fue exitosa, False en caso contrario.
"""

# Consultas relacionadas con reservas
reserva_dao_create = """
INSERT INTO reservas (tipo_reserva_id, salon_id, tipo_cocina_id, id_cliente, fecha, ocupacion, jornadas, habitaciones)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""
"""
Consulta SQL para crear una nueva reserva.

Args:
    tipo_reserva_id (int): ID del tipo de reserva.
    salon_id (int): ID del salón.
    tipo_cocina_id (int): ID del tipo de cocina.
    id_cliente (int): ID del cliente.
    fecha (str): Fecha de la reserva.
    ocupacion (int): Número de personas en la reserva.
    jornadas (int): Número de jornadas.
    habitaciones (int): Número de habitaciones.

Returns:
    bool: True si la creación fue exitosa, False en caso contrario.
"""

tipo_reserva_dao_find_all = "SELECT * FROM tipos_reservas"
"""
Consulta SQL para obtener todos los tipos de reservas.

Returns:
    list[dict]: Lista de diccionarios con los datos de los tipos de reservas.
"""

salones_dao_find_all = "SELECT * FROM salones"
"""
Consulta SQL para obtener todos los salones.

Returns:
    list[dict]: Lista de diccionarios con los datos de los salones.
"""

tipo_cocina_dao_find_all = "SELECT * FROM tipos_cocina"
"""
Consulta SQL para obtener todos los tipos de cocina.

Returns:
    list[dict]: Lista de diccionarios con los datos de los tipos de cocina.
"""

reservas_dao_find_all = "SELECT * FROM reservas"
"""
Consulta SQL para obtener todas las reservas.

Returns:
    list[dict]: Lista de diccionarios con los datos de las reservas.
"""

reservas_dao_find_byId = "SELECT * FROM reservas WHERE reserva_id = %s"
"""
Consulta SQL para buscar una reserva por su ID.

Args:
    reserva_id (int): El ID de la reserva a buscar.

Returns:
    dict: Un diccionario con los datos de la reserva encontrada.
"""

reserva_dao_update = """
UPDATE reservas
SET tipo_reserva_id = %s, salon_id = %s, tipo_cocina_id = %s, id_cliente = %s,
    fecha = %s, ocupacion = %s, jornadas = %s, habitaciones = %s
WHERE reserva_id = %s
"""
"""
Consulta SQL para actualizar una reserva existente.

Args:
    tipo_reserva_id (int): ID del tipo de reserva.
    salon_id (int): ID del salón.
    tipo_cocina_id (int): ID del tipo de cocina.
    id_cliente (int): ID del cliente.
    fecha (str): Fecha de la reserva.
    ocupacion (int): Número de personas en la reserva.
    jornadas (int): Número de jornadas.
    habitaciones (int): Número de habitaciones.
    reserva_id (int): ID de la reserva a actualizar.

Returns:
    bool: True si la actualización fue exitosa, False en caso contrario.
"""
