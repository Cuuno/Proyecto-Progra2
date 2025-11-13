from src.models.paciente import Paciente
from src.models.medico import Medico
from src.models.admision import Admision
from src.models.habitacion import Habitacion
from src.models.especialidad import Especialidad
from src import reportes
from src import backups

def mostrar_menu():
    print("\n--- MENÚ GESTIÓN HOSPITAL ---")
    print("1- Registrar Paciente")
    print("2- Admitir Paciente")
    print("3- Habitaciones Disponibles")
    print("4- Especialidades Disponibles")
    print("5- Registrar Alta")
    print("6- Pacientes Internados Actualmente")
    print("7- Historial clínico por paciente (dni)")
    print("--- Reportes ---")
    print("8- Gráfico de promedio de días de internación")
    print("9- Gráfico de habitaciones (ocupadas o libres)")
    print("--- Administración ---")
    print("10- Exportar Backup (CSV)")
    print("11- Restaurar Backup (CSV)")
    print("0- Salir")

def main():
 while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("== 1. Registrar Paciente ==")
            dni = input("DNI: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            nacimiento = input("Nacimiento (YYYY-MM-DD): ")
            email = input("Email: ")
            cel = input("Celular: ")
            domicilio = input("Domicilio: ")
            
            pac = Paciente(dni, nombre, apellido, nacimiento, email, cel, domicilio)
            pac.registrar()

        elif opcion == '2':
            print("== 2. Admitir Paciente ==")
            pac_id = input("ID del Paciente a admitir: ")
            med_id = input("ID del Médico responsable: ")
            diag_id = input("ID del Diagnóstico: ")
            hab_id = input("ID de la Habitación asignada: ")
            fecha_ingreso = input("Fecha de Ingreso (YYYY-MM-DD): ")

            adm = Admision(pac_id, med_id, diag_id, hab_id, fecha_ingreso)
            adm.registrar_ingreso()
            print("¡Paciente admitido!")

        elif opcion == '3':
            print("== 3. Habitaciones Disponibles ==")
            # TÚ llamas al Experto (Central)
            lista_habitaciones = Habitacion.get_disponibles()
            
            # TÚ muestras los resultados
            if lista_habitaciones:
                for hab in lista_habitaciones:
                    # (Central te devolverá un objeto o diccionario)
                    print(f"ID: {hab['hab_id']} | Nro: {hab['hab_nro']} | Piso: {hab['hab_piso']}")
            else:
                print("No hay habitaciones disponibles.")

        elif opcion == '4':
            print("== 4. Especialidades Disponibles ==")
            # TÚ llamas al Experto (Central)
            lista_especialidades = Especialidad.get_todas()
            
            # TÚ muestras los resultados
            if lista_especialidades:
                for esp in lista_especialidades:
                    print(f"ID: {esp['esp_id']} | Nombre: {esp['esp_nombre']}")
            else:
                print("No hay especialidades registradas.")

        elif opcion == '5':
            print("== 5. Registrar Alta ==")
            # TÚ pides los datos
            adm_id = input("ID de la Admisión a dar de alta: ")
            hab_id = input("ID de la Habitación que se libera: ") # Central necesita esto
            fecha_alta = input("Fecha de Alta (YYYY-MM-DD): ")
            observaciones = input("Observaciones del alta: ")

            # TÚ llamas al Experto (Central)
            Admision.registrar_alta(adm_id, fecha_alta, observaciones, hab_id)
            print("Alta registrada exitosamente.")

        elif opcion == '6':
            print("== 6. Pacientes Internados Actualmente ==")
            # TÚ llamas al Experto (Central)
            lista_internados = Admision.get_internados_actuales()
            
            # TÚ muestras los resultados
            if lista_internados:
                print("--- Pacientes Internados ---")
                for pac in lista_internados:
                    # (Central te dará una lista con Joins)
                    print(f"ID Adm: {pac['adm_id']} | Paciente: {pac['pac_nombre']} {pac['pac_apellido']} | Hab: {pac['hab_nro']}")
            else:
                print("No hay pacientes internados actualmente.")

        elif opcion == '7':
            print("== 7. Historial Clínico por Paciente ==")
            # TÚ pides los datos
            dni_buscar = input("Ingrese el DNI del paciente: ")
            
            # TÚ llamas al Experto (Central)
            historial = Admision.get_historial_de_paciente(dni_buscar)
            
            # TÚ muestras los resultados
            if historial:
                print(f"--- Historial de DNI {dni_buscar} ---")
                for adm in historial:
                    print(f"ID Adm: {adm['adm_id']} | Ingreso: {adm['adm_fecha_ingreso']} | Alta: {adm['adm_fecha_alta']} | Diag: {adm['diag_nostico']}")
            else:
                print(f"No se encontró historial para el DNI {dni_buscar}.")
        
        elif opcion == '8':
            print("== 8. Gráfico Promedio Días ==")
            reportes.generar_grafico_promedio_dias()
            
        elif opcion == '9':
            print("== 9. Gráfico Habitaciones ==")
            reportes.generar_grafico_estado_habitaciones()

        elif opcion == '10':
            print("== 10. Exportar Backup ==")          
            backups.exportar_csv()

        elif opcion == '11':
            print("== 11. Restaurar Backup ==")
            backups.importar_csv()

        elif opcion == '0':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()


