from  src import database 

class Habitacion():
    def __init__(self,numero,piso,disponibilidad):
        self.numero = numero
        self.piso = piso
        self.disponibilidad = disponibilidad
# mostramos la info de las habitaciones

    def mostrar_info(self):
        estado = "Libre" if self.disponibilidad else "Ocupada"
        print(f"Habitación {self.numero} | Piso {self.piso} | Estado: {estado}")

habitaciones = []

#mostramos las habitaciones registradas.

def mostrar_habitaciones():
    if not habitaciones:
        print("No hay habitaciones registradas.")
        return
    print("\n--- LISTA DE HABITACIONES ---")
    for hab in habitaciones:
        hab.mostrar_info()
    print()

# Mostrar solo habitaciones disponibles
def mostrar_disponibles():
    disponibles = [h for h in habitaciones if h.disponibilidad]
    if not disponibles:
        print(" No hay habitaciones disponibles.")
        return
    print("\n--- HABITACIONES DISPONIBLES ---")
    for hab in disponibles:
        hab.mostrar_info()
    print()

# cambiar estado de habitacion 
def cambiar_estado():
    numero = input("Ingrese número de habitación para cambiar estado: ")
    for hab in habitaciones:
        if hab.numero == numero:
            hab.disponibilidad = not hab.disponibilidad
            estado = "libre" if hab.disponibilidad else "ocupada"
            print(f"✅ Habitación {numero} ahora está {estado}.")
            return
    print("No se encontró la habitación indicada.")