from dao.queris import clientes_dao_find_all_actives, clientes_dao_find_by_id, clientes_dao_desctivate,cliente_dao_create
from model.clientes import Cliente


class ClienteDao:
    def __init__(self, conexion):
        self.conexion = conexion

    def find_all_activos(self):
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
        if self.conexion:
            cursor = self.conexion.cursor(dictionary=True)
            try:
                cursor.execute(clientes_dao_find_by_id,(id,))
                result = cursor.fetchone()
                return self.convertir_cliente(result)
            finally:
                cursor.close()
        return None

    def actualizar_cliente(self, id: int, nombre: str, apellidos: str, fec_nac: str, pais: str,
                       telefono: str, email: str, sexo: str, menores: int, activo: bool) -> bool:
        """
        Actualiza los datos de un cliente en la base de datos.
        Devuelve True si la actualización fue exitosa, False en caso contrario.
        """
        query = """
            UPDATE clientes
            SET Nombre = %s, Apellidos = %s, Fec_Nac = %s, Pais = %s,
                Telefono = %s, email = %s, Sexo = %s, Menores = %s, activo = %s
            WHERE Id = %s;
        """

        if self.conexion:
            cursor = self.conexion.cursor(dictionary=True)
            try:
                cursor.execute(query, (nombre, apellidos, fec_nac, pais, telefono, email, sexo, menores, activo, id))
                self.conexion.commit()
                return cursor.rowcount > 0  
            finally:
                cursor.close()
        return False

    def desactive_clientes(self, id: int) -> bool:
        """
        Desactiva o activa un cliente alternando el estado del campo 'activo'.
        Devuelve True si la actualización fue exitosa, False en caso contrario.
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

    def crear_cliente(self, cliente: Cliente) -> bool:
        """
        Inserta un nuevo cliente en la base de datos.

        Args:
            cliente (Cliente): Objeto Cliente con la información a registrar.

        Returns:
            bool: True si la inserción fue exitosa, False en caso contrario.
        """
        if self.conexion:
            cursor = self.conexion.cursor(dictionary=True)
            try:
                cursor.execute(cliente_dao_create, (
                    cliente.Nombre, cliente.Apellidos, cliente.Num_Identificacion,
                    cliente.Fec_Nac, cliente.Pais, cliente.Telefono, cliente.email,
                    cliente.Sexo, cliente.Menores, cliente.activo
                ))
                self.conexion.commit()
                return cursor.rowcount > 0  # True si se insertó correctamente
            finally:
                cursor.close()
        return False

    def convertir_cliente(self, cliente):
        return Cliente.from_dict(cliente)
