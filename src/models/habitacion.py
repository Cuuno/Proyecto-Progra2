from  src import database as db

class Habitacion():
    def __init__(self,numero,piso,disponibilidad):
        self.numero = numero
        self.piso = piso
        self.disponibilidad = disponibilidad
   
    # Mostrar solo habitaciones disponibles
    @staticmethod
    def obtener_disponibles():
       pass
    
    # cambiar estado de habitacion 
    def cambiar_estado(hab_elegida):
        numero = hab_elegida
        for hab in habitaciones:
            if hab.numero == numero:
                hab.disponibilidad = not hab.disponibilidad
                estado = "libre" if hab.disponibilidad else "ocupada"
                print(f"✅ Habitación {numero} ahora está {estado}.")
                return
        print("No se encontró la habitación indicada.")