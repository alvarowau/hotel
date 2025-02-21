from dao.queries import tipo_reserva_dao_find_all
from model.tipo_reservas import TipoReservas


class TipoReservasDao:
    """
    Clase que maneja las operaciones de acceso a datos (DAO) para la entidad TipoReservas.

    Esta clase proporciona métodos para interactuar con la base de datos, como la búsqueda
    de todos los tipos de reservas disponibles.

    Atributos:
        conexion: Objeto de conexión a la base de datos.

    Métodos:
        find_all(): Obtiene todos los tipos de reservas.
        convertir_tipo_reservas(tipo_reserva): Convierte un diccionario en un objeto TipoReservas.
    """

    def __init__(self, conexion):
        """
        Inicializa una instancia de TipoReservasDao.

        Args:
            conexion: Objeto de conexión a la base de datos.
        """
        self.conexion = conexion

    def find_all(self):
        """
        Obtiene todos los tipos de reservas de la base de datos.

        Returns:
            list[TipoReservas]: Una lista de objetos TipoReservas que representan todos los tipos de reservas.
            None: Si no hay conexión a la base de datos.
        """
        if self.conexion:
            cursor = self.conexion.cursor(dictionary=True)
            try:
                cursor.execute(tipo_reserva_dao_find_all)
                result = cursor.fetchall()
                lista_tipo_reservas = list()
                for tipo in result:
                    lista_tipo_reservas.append(self.convertir_tipo_reservas(tipo))
                return lista_tipo_reservas
            finally:
                cursor.close()
        return None

    def convertir_tipo_reservas(self, tipo_reserva):
        """
        Convierte un diccionario en un objeto TipoReservas.

        Args:
            tipo_reserva (dict): Un diccionario con los datos del tipo de reserva.

        Returns:
            TipoReservas: Un objeto TipoReservas creado a partir del diccionario.
        """
        return TipoReservas.from_dict(tipo_reserva)
