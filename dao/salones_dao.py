from dao.queries import salones_dao_find_all
from model.salon import Salon


class SalonDao:
    """
    Clase que maneja las operaciones de acceso a datos (DAO) para la entidad Salón.

    Esta clase proporciona métodos para interactuar con la base de datos, como la búsqueda
    de todos los salones disponibles.

    Atributos:
        conexion: Objeto de conexión a la base de datos.

    Métodos:
        find_all(): Obtiene todos los salones.
        convertir_salon(salon): Convierte un diccionario en un objeto Salon.
    """

    def __init__(self, conexion):
        """
        Inicializa una instancia de SalonDao.

        Args:
            conexion: Objeto de conexión a la base de datos.
        """
        self.conexion = conexion

    def find_all(self):
        """
        Obtiene todos los salones de la base de datos.

        Returns:
            list[Salon]: Una lista de objetos Salon que representan todos los salones.
            None: Si no hay conexión a la base de datos.
        """
        if self.conexion:
            cursor = self.conexion.cursor(dictionary=True)
            try:
                cursor.execute(salones_dao_find_all)
                result = cursor.fetchall()
                lista_salones = list()
                for sal in result:
                    lista_salones.append(self.convertir_salon(sal))
                return lista_salones
            finally:
                cursor.close()
        return None

    def convertir_salon(self, salon):
        """
        Convierte un diccionario en un objeto Salon.

        Args:
            salon (dict): Un diccionario con los datos del salón.

        Returns:
            Salon: Un objeto Salon creado a partir del diccionario.
        """
        return Salon.from_dict(salon)
