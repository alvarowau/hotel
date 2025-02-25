from dao.queries_reservas import (
    create,
    delete,
    details_delete,
    find_all,
    find_all_by_id_salones,
    find_byId,
    is_date_dispon,
    update,
)
from model.reserva import Reserva


class ReservaDao:
    """
    Clase que maneja las operaciones de acceso a datos (DAO) para la entidad Reserva.

    Esta clase proporciona métodos para interactuar con la base de datos, como la búsqueda,
    creación y actualización de reservas.

    Atributos:
        conexion: Objeto de conexión a la base de datos.

    Métodos:
        find_all(): Obtiene todas las reservas.
        find_by_id(id): Busca una reserva por su ID.
        create(reserva): Crea una nueva reserva.
        update(reserva): Actualiza una reserva existente.
        convertir_reserva(reserva): Convierte un diccionario en un objeto Reserva.
    """

    def __init__(self, conexion):
        """
        Inicializa una instancia de ReservaDao.

        Args:
            conexion: Objeto de conexión a la base de datos.
        """
        self.conexion = conexion

    def find_all(self):
        """
        Obtiene todas las reservas de la base de datos.

        Returns:
            list[Reserva]: Una lista de objetos Reserva que representan todas las reservas.
            None: Si no hay conexión a la base de datos.
        """
        if self.conexion:
            cursor = self.conexion.cursor(dictionary=True)
            try:
                cursor.execute(find_all)
                result = cursor.fetchall()
                lista_reserva = list()
                for res in result:
                    lista_reserva.append(self.convertir_reserva(res))
                return lista_reserva
            finally:
                cursor.close()
        return None

    def find_by_id(self, id):
        """
        Busca una reserva por su ID en la base de datos.

        Args:
            id (int): El ID de la reserva a buscar.

        Returns:
            Reserva: Un objeto Reserva que representa la reserva encontrada.
            None: Si no se encuentra la reserva o no hay conexión a la base de datos.
        """
        if self.conexion:
            cursor = self.conexion.cursor(dictionary=True)
            try:
                cursor.execute(find_byId, (id,))
                result = cursor.fetchone()
                return self.convertir_reserva(result)
            finally:
                cursor.close()
        return None

    def create(self, reserva: Reserva):
        """
        Crea una nueva reserva en la base de datos.

        Args:
            reserva (Reserva): Un objeto Reserva con los datos de la nueva reserva.

        Returns:
            bool: True si la creación fue exitosa, False en caso contrario.
        """
        if self.conexion:
            cursor = self.conexion.cursor(dictionary=True)
            try:
                cursor.execute(
                    create,
                    (
                        reserva.tipo_reserva_id,
                        reserva.salon_id,
                        reserva.tipo_cocina_id,
                        reserva.id_cliente,
                        reserva.fecha,
                        reserva.ocupacion,
                        reserva.jornadas,
                        reserva.habitaciones,
                    ),
                )
                self.conexion.commit()
                return cursor.rowcount > 0
            finally:
                cursor.close()
        return False

    def update(self, reserva: Reserva):
        """
        Actualiza una reserva existente en la base de datos.

        Args:
            reserva (Reserva): Un objeto Reserva con los datos actualizados.

        Returns:
            bool: True si la actualización fue exitosa, False en caso contrario.
        """
        if self.conexion:
            cursor = self.conexion.cursor(dictionary=True)
            try:
                cursor.execute(
                    update,
                    (
                        reserva.tipo_reserva_id,
                        reserva.salon_id,
                        reserva.tipo_cocina_id,
                        reserva.id_cliente,
                        reserva.fecha,
                        reserva.ocupacion,
                        reserva.jornadas,
                        reserva.habitaciones,
                        reserva.reserva_id,
                    ),
                )
                self.conexion.commit()
                return cursor.rowcount > 0
            finally:
                cursor.close()
        else:
            return False

    def convertir_reserva(self, reserva):
        """
        Convierte un diccionario en un objeto Reserva.

        Args:
            reserva (dict): Un diccionario con los datos de la reserva.

        Returns:
            Reserva: Un objeto Reserva creado a partir del diccionario.
        """
        return Reserva.from_dict(reserva)

    def traer_details_delete(self, id_reserva):
        if self.conexion:
            cursor = self.conexion.cursor(dictionary=True)
            try:
                cursor.execute(details_delete, (id_reserva,))
                result = cursor.fetchone()
                return f"{result['Nombre']} {result['Apellidos']} en la fecha {result['fecha']}"
            finally:
                cursor.close()
        return None

    def find_all_by_salon_id(self, id_salon):
        """
        Obtiene todas las reservas de la base de datos.

        Returns:
            list[Reserva]: Una lista de objetos Reserva que representan todas las reservas.
            None: Si no hay conexión a la base de datos.
        """
        if self.conexion:
            cursor = self.conexion.cursor(dictionary=True)
            try:
                cursor.execute(find_all_by_id_salones, (id_salon,))
                result = cursor.fetchall()
                lista_reserva = list()
                for res in result:
                    lista_reserva.append(self.convertir_reserva(res))
                return lista_reserva
            finally:
                cursor.close()
        return None

    def is_fecha_dispon(self, salon_id, fecha):
        if self.conexion:
            cursor = self.conexion.cursor()
            try:
                cursor.execute(is_date_dispon, (salon_id, fecha))
                result = cursor.fetchone()
                return not result[0] > 0
            finally:
                cursor.close()
        return False

    def delete(self, id_reserva):
        if self.conexion:
            cursor = self.conexion.cursor()
            try:
                cursor.execute(delete, (id_reserva,))
                self.conexion.commit()
                return cursor.rowcount > 0
            except Exception:
                self.conexion.rollback()
                return False
            finally:
                cursor.close()
        else:
            return None
