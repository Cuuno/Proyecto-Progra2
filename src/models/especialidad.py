from src import database as db
class Especialidad():
    def __init__ (self,nombre):
        self.nombre = nombre

    @staticmethod
    def obtener_especialidades():
        print ("MODELO: Pidiendo lista de especialidades")
        try:
            lista_especialidades=db.obtener_especialidades_db()
            return lista_especialidades
        except Exception as e:
            print(f"MODELO ERROR: Fallo inesperado al llamar a la BD: {e}")
            return None