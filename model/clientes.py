class Cliente:
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
        Constructor de la clase Cliente.

        Args:
            Id (int, opcional): Identificador único del cliente (clave primaria). Autoincremental en la base de datos.
            Nombre (str, opcional): Nombre del cliente.
            Apellidos (str, opcional): Apellidos del cliente.
            Num_Identificacion (str, opcional): Número de identificación único del cliente.
            Fec_Nac (date, opcional): Fecha de nacimiento del cliente.
            Pais (str, opcional): País de residencia del cliente.
            Telefono (str, opcional): Número de teléfono del cliente.
            email (str, opcional): Correo electrónico del cliente.
            Sexo (str, opcional): Sexo del cliente ('H' para Hombre, 'M' para Mujer, 'N' para No binario, etc.).
            Menores (int, opcional): Indica si el cliente tiene menores a su cargo (1 para Sí, 0 para No).
            activo (int, opcional): Indica si el cliente está activo (1) o inactivo (0). Por defecto es 1 (activo).
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
        Método para representar el objeto Cliente como una cadena (string).
        Útil para debuggear o imprimir información del cliente.
        """
        return f"Cliente(Id={self.Id}, Nombre='{self.Nombre}', Apellidos='{self.Apellidos}', Num_Identificacion='{self.Num_Identificacion}')"

    @classmethod
    def from_dict(cls, data_dict):
        """
        Método de clase para crear un objeto Cliente a partir de un diccionario.

        Args:
            data_dict (dict): Diccionario que contiene los datos del cliente.
                              Las claves del diccionario deberían corresponder
                              a los atributos de la clase Cliente (Id, Nombre, Apellidos, etc.).

        Returns:
            Cliente: Un nuevo objeto Cliente instanciado con los datos del diccionario.

        Ejemplo de uso:
        cliente_dict = {
            "Nombre": "Elena",
            "Apellidos": "Martínez Sanz",
            "Num_Identificacion": "32C",
            "Fec_Nac": "1988-05-10",
            "Pais": "Francia",
            "Telefono": "777111222",
            "email": "elena.martinez@gmail.com",
            "Sexo": "M",
            "Menores": 1,
            "activo": 1,
            "Id": 32 # (Opcional, si el Id ya existe o lo quieres especificar)
        }
        cliente_desde_dict = Cliente.from_dict(cliente_dict)
        print(cliente_desde_dict)
        """
        return cls(**data_dict)
