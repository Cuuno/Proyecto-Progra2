from  src import database as db
class Habitacion():
    def __init__(self,numero,piso,disponibilidad):
        self.numero = numero
        self.piso = piso
        self.disponibilidad = disponibilidad

    @staticmethod
    def obtener_disponibles():
        print("MODELO: Pidiendo habitaciones disponibles...")
        try:
            lista_habitaciones=db.obtener_habitaciones_disponibles_db()
            return lista_habitaciones
        except Exception as e:
            print (f"MODELO ERROR: Fallo inesperado al llamar a la BD {e}")
            return None 

    
