from  src import database as db

class Habitacion():
    def __init__(self,numero,piso,disponibilidad):
        self.numero = numero
        self.piso = piso
        self.disponibilidad = disponibilidad
    # mostramos la info de las habitaciones

    def mostrar_info(self):
        estado = "Libre" if self.disponibilidad else "Ocupada"
        print(f"Habitación {self.numero} | Piso {self.piso} | Estado: {estado}")
   
    # Mostrar solo habitaciones disponibles
    @staticmethod
    def obtener_disponibles():
        disponibles = [h for h in habitaciones if h.disponibilidad]
        if not disponibles:
            print(" No hay habitaciones disponibles.")
            return
        print("\n--- HABITACIONES DISPONIBLES ---")
        for hab in disponibles:
            hab.mostrar_info()
        print()
    
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