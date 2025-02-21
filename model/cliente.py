class Cliente:
    """
    Representa un cliente en el sistema.

    Atributos:
        Id (int, opcional): Identificador único del cliente.
        Nombre (str, opcional): Nombre del cliente.
        Apellidos (str, opcional): Apellidos del cliente.
        Num_Identificacion (str, opcional): Número de identificación del cliente.
        Fec_Nac (str, opcional): Fecha de nacimiento del cliente.
        Pais (str, opcional): País del cliente.
        Telefono (str, opcional): Número de teléfono del cliente.
        email (str, opcional): Dirección de correo electrónico del cliente.
        Sexo (str, opcional): Sexo del cliente.
        Menores (bool, opcional): Indica si el cliente es menor de edad.
        activo (int, opcional): Estado de actividad del cliente. Por defecto es 1 (activo).
    """

    def __init__(
        self,
        Id=None,
        Nombre=None,
        Apellidos=None,
        Num_Identificacion=None,
        Fec_Nac=None,
        Pais=None,
        Telefono=None,
        email=None,
        Sexo=None,
        Menores=None,
        activo=1,
    ):
        """
        Inicializa una nueva instancia de la clase Cliente.

        Args:
            Id (int, opcional): Identificador único del cliente.
            Nombre (str, opcional): Nombre del cliente.
            Apellidos (str, opcional): Apellidos del cliente.
            Num_Identificacion (str, opcional): Número de identificación del cliente.
            Fec_Nac (str, opcional): Fecha de nacimiento del cliente.
            Pais (str, opcional): País del cliente.
            Telefono (str, opcional): Número de teléfono del cliente.
            email (str, opcional): Dirección de correo electrónico del cliente.
            Sexo (str, opcional): Sexo del cliente.
            Menores (bool, opcional): Indica si el cliente es menor de edad.
            activo (int, opcional): Estado de actividad del cliente.
        """
        self.Id = Id
        self.Nombre = Nombre
        self.Apellidos = Apellidos
        self.Num_Identificacion = Num_Identificacion
        self.Fec_Nac = Fec_Nac
        self.Pais = Pais
        self.Telefono = Telefono
        self.email = email
        self.Sexo = Sexo
        self.Menores = Menores
        self.activo = activo

    def __str__(self):
        """
        Devuelve una representación en forma de cadena del cliente.

        Returns:
            str: Cadena que representa al cliente.
        """
        return f"Cliente(Id={self.Id}, Nombre='{self.Nombre}', Apellidos='{self.Apellidos}', Num_Identificacion='{self.Num_Identificacion}')"

    @classmethod
    def from_dict(cls, data_dict):
        """
        Crea una instancia de Cliente a partir de un diccionario de datos.

        Args:
            data_dict (dict): Diccionario con los datos del cliente.

        Returns:
            Cliente: Instancia de la clase Cliente.
        """
        return cls(**data_dict)

    # Getters y Setters

    @property
    def Id(self):
        """Obtiene el identificador del cliente."""
        return self._Id

    @Id.setter
    def Id(self, value):
        """Establece el identificador del cliente."""
        self._Id = value

    @property
    def Nombre(self):
        """Obtiene el nombre del cliente."""
        return self._Nombre

    @Nombre.setter
    def Nombre(self, value):
        """Establece el nombre del cliente."""
        self._Nombre = value

    @property
    def Apellidos(self):
        """Obtiene los apellidos del cliente."""
        return self._Apellidos

    @Apellidos.setter
    def Apellidos(self, value):
        """Establece los apellidos del cliente."""
        self._Apellidos = value

    @property
    def Num_Identificacion(self):
        """Obtiene el número de identificación del cliente."""
        return self._Num_Identificacion

    @Num_Identificacion.setter
    def Num_Identificacion(self, value):
        """Establece el número de identificación del cliente."""
        self._Num_Identificacion = value

    @property
    def Fec_Nac(self):
        """Obtiene la fecha de nacimiento del cliente."""
        return self._Fec_Nac

    @Fec_Nac.setter
    def Fec_Nac(self, value):
        """Establece la fecha de nacimiento del cliente."""
        self._Fec_Nac = value

    @property
    def Pais(self):
        """Obtiene el país del cliente."""
        return self._Pais

    @Pais.setter
    def Pais(self, value):
        """Establece el país del cliente."""
        self._Pais = value

    @property
    def Telefono(self):
        """Obtiene el número de teléfono del cliente."""
        return self._Telefono

    @Telefono.setter
    def Telefono(self, value):
        """Establece el número de teléfono del cliente."""
        self._Telefono = value

    @property
    def email(self):
        """Obtiene la dirección de correo electrónico del cliente."""
        return self._email

    @email.setter
    def email(self, value):
        """Establece la dirección de correo electrónico del cliente."""
        self._email = value

    @property
    def Sexo(self):
        """Obtiene el sexo del cliente."""
        return self._Sexo

    @Sexo.setter
    def Sexo(self, value):
        """Establece el sexo del cliente."""
        self._Sexo = value

    @property
    def Menores(self):
        """Obtiene si el cliente es menor de edad."""
        return self._Menores

    @Menores.setter
    def Menores(self, value):
        """Establece si el cliente es menor de edad."""
        self._Menores = value

    @property
    def activo(self):
        """Obtiene el estado de actividad del cliente."""
        return self._activo

    @activo.setter
    def activo(self, value):
        """Establece el estado de actividad del cliente."""
        self._activo = value
