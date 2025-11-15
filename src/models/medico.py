from src.models.persona import Persona
from src import database as db
class Medico(Persona):
    def __init__(self, nombre, apellido, nacimiento, email, cel, domicilio, esp_id):
        super().__init__(nombre,apellido)
        self.nacimiento = nacimiento
        self.email = email
        self.cel = cel
        self.domicilio = domicilio
        self.esp_id = esp_id

        print (f"Objeto Medico '{self.nombre}'creado en memoria")
    def get_rol(self):
        return "Medico"
    @staticmethod
    def obtener_medicos():
            print ("Pidiendo lista de medicos...")
            return db.obtener_medicos_db()
 