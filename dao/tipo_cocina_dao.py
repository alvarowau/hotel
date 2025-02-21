from dao.queries import tipo_cocina_dao_find_all
from model.tipos_cocina import TiposCocina


class TipoCocinaDao:
    """
    Clase que maneja las operaciones de acceso a datos (DAO) para la entidad TiposCocina.

    Esta clase proporciona métodos para interactuar con la base de datos, como la búsqueda
    de todos los tipos de cocina disponibles.

    Atributos:
        conexion: Objeto de conexión a la base de datos.

    Métodos:
        find_all(): Obtiene todos los tipos de cocina.
        convertir_tipo_cocina(cocina): Convierte un diccionario en un objeto TiposCocina.
    """

    def __init__(self, conexion):
        """
        Inicializa una instancia de TipoCocinaDao.

        Args:
            conexion: Objeto de conexión a la base de datos.
        """
        self.conexion = conexion

    def find_all(self):
        """
        Obtiene todos los tipos de cocina de la base de datos.

        Returns:
            list[TiposCocina]: Una lista de objetos TiposCocina que representan todos los tipos de cocina.
            None: Si no hay conexión a la base de datos.
        """
        if self.conexion:
            cursor = self.conexion.cursor(dictionary=True)
            try:
                cursor.execute(tipo_cocina_dao_find_all)
                result = cursor.fetchall()
                tipos_cocina = list()
                for cocina in result:
                    tipos_cocina.append(self.convertir_tipo_cocina(cocina))
                return tipos_cocina
            finally:
                cursor.close()
        else:
            return None

    def convertir_tipo_cocina(self, cocina):
        """
        Convierte un diccionario en un objeto TiposCocina.

        Args:
            cocina (dict): Un diccionario con los datos del tipo de cocina.

        Returns:
            TiposCocina: Un objeto TiposCocina creado a partir del diccionario.
        """
        return TiposCocina.from_dict(cocina)
