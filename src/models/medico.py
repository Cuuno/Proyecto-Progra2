from src.models.persona import Persona
class Medico(Persona):
    def __init__(self, nombre, apellido, nacimiento, email, cel, domicilio):
        super().__init__(nombre,apellido)
        self.nacimiento = nacimiento
        self.email = email
        self.cel = cel
        self.domicilio = domicilio
        self.esp_id = esp_id
        print (f"Objeto Medico '{self.nombre}'creado en memoria")
    def obtener_medicos():
        pass
    def get_rol(self):
        return "Medico"

 