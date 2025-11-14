from src.models.paciente import Paciente
from src.models.medico import Medico
from src.models.admision import Admision
from src.models.habitacion import Habitacion
from src.models.especialidad import Especialidad
from src.models.diagnostico import Diagnostico
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
            if pac.registrar:
                print(f"Paciente {pac['pac_nombre']} registado con exito.")#probar


        elif opcion == '2':
            print("== 2. Admitir Paciente ==")

            try:
                #buscar paciente por dni
                pac_dni=input("DNI del Paciente a admitir: ")
                paciente=pac.buscar_por_dni(pac_dni)
                if paciente is None:
                    print(f"Paciente con DNI {pac_dni} no encontrado. Registre nuevamente")
                    continue
                print (f"Paciente encontrado: {paciente['pac_nombre']} {paciente['pac_apellido']}")

                #seleccionar medico
                print("\n--- Selecionar Medico ---")
                lista_medicos=Medico.obtener_medicos()

                for i, medico in enumerate(lista_medicos):
                    print (f"[{i+1}] - Dr. {medico['med_nombre']} {medico['med_apellido']} {medico['esp_nombre']}")
                selec_num=int(input("Seleccione el NUMERO del médico: "))
                medico_elegido= lista_medicos[selec_num-1]
                med_id = medico_elegido['med_id']

                #seleccionar diagnostico
                print("\n --- Seleccionar Diagnóstico ---")
                lista_diagnosticos = Diagnostico.obtener_diagnosticos()
                
                for i, diag in enumerate (lista_diagnosticos):
                    print (f"[{i+1}]-{diag['diag_nostico']}")
                print (f"[99] - Agregar nuevo diagnostico...")
                selec_num=int(input("Seleccione el NUMERO del diagnóstico (o 99): "))

                diag_id= None

                #agregar diagnostico
                if selec_num == 99:
                    print("\n --- Nuevo Diagnostico ---")
                    diag_nuevo= input("Descripcion del nuevo diagnostico: ")

                    if not diag_nuevo:
                        print ("Error: La descripcion no puede estar vacia. Cancelando admision...")
                        continue

                    diag_id = Diagnostico.crear_diagnostico(diag_nuevo)

                    if diag_id is not None:
                        print (f"Diagnostico '{diag_nuevo}' creado con ID {diag_id}")

                else:
                    diag_elegido = lista_diagnosticos[selec_num - 1]
                    diag_id = diag_elegido['diag_id']
                
                #Seleccionar habitacion
                print ("\n --- Seleccionar Habitacion Disponible ---")
                lista_habitaciones= Habitacion.obtener_disponibles()

                if not lista_habitaciones:
                    print ("Error: NO HAY HABITACIONES DISPONBILES")
                    continue
                
                for i, hab in enumerate(lista_habitaciones):
                    print (f"[{i+1}] - Habitación Nro: {hab['hab_nro']} (Piso: {hab['hab_piso']})")

                selec_num= int(input("Seleccione el Numero de habitacion"))
                hab_elegida=lista_habitaciones[selec_num-1]
                hab_id=hab_elegida['hab_id']

                #fecha
                fecha_ingreso=input("\nFecha de ingreso (YYYY-MM-DD)")

                #llamada a admision
                print("Procesando admision...")
                exito=Admision.registrar_ingreso_por_dni(
                    pac_dni,
                    med_id,
                    diag_id,
                    hab_id,
                    fecha_ingreso
                )

                if exito:
                    print("Paciente admitido exitosamente")
                else:
                    print("No se pudo admitir, verifique datos ingresados")

            except (ValueError, IndexError):
                print("Error: Escribio un numero incorrecto.")
                continue

            except Exception as e:
                print(f"Error inesperado en la admisión: {e}")
                continue

                
        elif opcion == '3':
            print("== 3. Habitaciones Disponibles ==")
            lista_habitaciones = Habitacion.habitaciones_disponibles()
            
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


