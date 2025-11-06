from src.models.persona import Persona
class Medico(Persona):
    def __init__(self, nombre, apellido, nacimiento, email, cel, domicilio):
        super().__init__(nombre,apellido)
        print (f"Objeto Medico '{self.nombre}'creado en memoria")
    def registrar_medico(self):
        pass
    @staticmethod
    def eliminar_medico(self):
        pass
    def get_rol(self):
        return "Medico"