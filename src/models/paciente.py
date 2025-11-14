from src.models.persona import Persona
class Paciente(Persona):
    def __init__(self, dni, nombre, apellido, nacimiento, email, cel, domicilio):
        super().__init__(nombre,apellido)
        self.dni = dni
        self.nacimiento = nacimiento
        self.email = email
        self.cel = cel
        self.domicilio = domicilio
        print (f"Objeto Paciente '{self.nombre}'creado en memoria")
    def registrar(self):
        pass
    @staticmethod
    def buscar_por_dni(pac_dni):
        pass
    def get_rol(self):
        return "Paciente"