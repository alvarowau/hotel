from dao.queries import (
    clientes_dao_find_all_actives,
    clientes_dao_find_by_id,
    clientes_dao_desctivate,
    cliente_dao_create,
    cliente_dao_update,
)
from model.cliente import Cliente


class ClienteDao:
    """
    Clase que maneja las operaciones de acceso a datos (DAO) para la entidad Cliente.

    Esta clase proporciona métodos para interactuar con la base de datos, como la búsqueda,
    creación, actualización y desactivación de clientes.

    Atributos:
        conexion: Objeto de conexión a la base de datos.

    Métodos:
        find_all_activos(): Obtiene todos los clientes activos.
        find_all_by_id(id): Busca un cliente por su ID.
        update(id, nombre, apellidos, fec_nac, pais, telefono, email, sexo, menores, activo): Actualiza un cliente.
        deactivate(id): Desactiva un cliente por su ID.
        create(cliente): Crea un nuevo cliente.
        convertir_cliente(cliente): Convierte un diccionario en un objeto Cliente.
    """

    def __init__(self, conexion):
        """
        Inicializa una instancia de ClienteDao.

        Args:
            conexion: Objeto de conexión a la base de datos.
        """
        self.conexion = conexion

    def find_all_activos(self):
        """
        Obtiene todos los clientes activos de la base de datos.

        Returns:
            list[Cliente]: Una lista de objetos Cliente que representan a los clientes activos.
            None: Si no hay conexión a la base de datos.
        """
        if self.conexion:
            cursor = self.conexion.cursor(dictionary=True)
            try:
                cursor.execute(clientes_dao_find_all_actives)
                result = cursor.fetchall()
                lista_cliente = list()
                for clie in result:
                    lista_cliente.append(self.convertir_cliente(clie))
                return lista_cliente
            finally:
                cursor.close()
        return None

    def find_all_by_id(self, id):
        """
        Busca un cliente por su ID en la base de datos.

        Args:
            id (int): El ID del cliente a buscar.

        Returns:
            Cliente: Un objeto Cliente que representa al cliente encontrado.
            None: Si no se encuentra el cliente o no hay conexión a la base de datos.
        """
        if self.conexion:
            cursor = self.conexion.cursor(dictionary=True)
            try:
                cursor.execute(clientes_dao_find_by_id, (id,))
                result = cursor.fetchone()
                return self.convertir_cliente(result)
            finally:
                cursor.close()
        return None

    def update(
        self,
        id: int,
        nombre: str,
        apellidos: str,
        fec_nac: str,
        pais: str,
        telefono: str,
        email: str,
        sexo: str,
        menores: int,
        activo: bool,
    ) -> bool:
        """
        Actualiza los datos de un cliente en la base de datos.

        Args:
            id (int): El ID del cliente a actualizar.
            nombre (str): El nuevo nombre del cliente.
            apellidos (str): Los nuevos apellidos del cliente.
            fec_nac (str): La nueva fecha de nacimiento del cliente.
            pais (str): El nuevo país del cliente.
            telefono (str): El nuevo teléfono del cliente.
            email (str): El nuevo email del cliente.
            sexo (str): El nuevo sexo del cliente.
            menores (int): El nuevo número de menores a cargo del cliente.
            activo (bool): El nuevo estado de activación del cliente.

        Returns:
            bool: True si la actualización fue exitosa, False en caso contrario.
        """
        if self.conexion:
            cursor = self.conexion.cursor(dictionary=True)
            try:
                cursor.execute(
                    cliente_dao_update,
                    (
                        nombre,
                        apellidos,
                        fec_nac,
                        pais,
                        telefono,
                        email,
                        sexo,
                        menores,
                        activo,
                        id,
                    ),
                )
                self.conexion.commit()
                return cursor.rowcount > 0
            finally:
                cursor.close()
        return False

    def deactivate(self, id: int) -> bool:
        """
        Desactiva un cliente en la base de datos por su ID.

        Args:
            id (int): El ID del cliente a desactivar.

        Returns:
            bool: True si la desactivación fue exitosa, False en caso contrario.
        """
        if self.conexion:
            cursor = self.conexion.cursor(dictionary=True)
            try:
                cursor.execute(clientes_dao_desctivate, (id,))
                self.conexion.commit()
                return cursor.rowcount > 0
            finally:
                cursor.close()
        return False

    def create(self, cliente: Cliente) -> bool:
        """
        Crea un nuevo cliente en la base de datos.

        Args:
            cliente (Cliente): Un objeto Cliente con los datos del nuevo cliente.

        Returns:
            bool: True si la creación fue exitosa, False en caso contrario.
        """
        if self.conexion:
            cursor = self.conexion.cursor(dictionary=True)
            try:
                cursor.execute(
                    cliente_dao_create,
                    (
                        cliente.Nombre,
                        cliente.Apellidos,
                        cliente.Num_Identificacion,
                        cliente.Fec_Nac,
                        cliente.Pais,
                        cliente.Telefono,
                        cliente.email,
                        cliente.Sexo,
                        cliente.Menores,
                        cliente.activo,
                    ),
                )
                self.conexion.commit()
                return cursor.rowcount > 0  # True si se insertó correctamente
            finally:
                cursor.close()
        return False

    def convertir_cliente(self, cliente):
        """
        Convierte un diccionario en un objeto Cliente.

        Args:
            cliente (dict): Un diccionario con los datos del cliente.

        Returns:
            Cliente: Un objeto Cliente creado a partir del diccionario.
        """
        return Cliente.from_dict(cliente)
