from src.models.persona import Persona
from src import database as db
class Paciente(Persona):
    def __init__(self, dni, nombre, apellido, nacimiento, email, cel, domicilio):
        super().__init__(nombre,apellido)
        self.dni = dni
        self.nacimiento = nacimiento
        self.email = email
        self.cel = cel
        self.domicilio = domicilio
        print (f"Objeto Paciente '{self.nombre}'creado en memoria")
    def get_rol(self):
        return "Paciente" #defino el rol
    def registrar(self,dni):
        print (f"MODELO: Registrando a {self.nombre}")
        #validacion de DNI 
        try:
            if len(str(self.dni)) < 7 or len(str(self.dni)) > 8: #len no cuenta numeros, por eso uso str
                print(f"MODELO ERROR: El DNI '{self.dni}' no tiene 7 u 8 dígitos.")
                return False
        except Exception as e:
            print(f"MODELO ERROR: El DNI '{self.dni}' no es válido: {e}")
            return False
        #
        exito = db.registrar_paciente_db(
            self.dni,
            self.nombre,
            self.apellido,
            self.nacimiento,
            self.email,
            self.cel,
            self.domicilio
        )
        return exito
    @staticmethod
    def buscar_por_dni(pac_dni):
        pass
    