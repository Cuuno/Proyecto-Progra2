from src.models.paciente import Paciente
from src.models.medico import Medico
from src.models.admision import Admision
from src.models.habitacion import Habitacion
from src.models.especialidad import Especialidad
from src.models.diagnostico import Diagnostico
from src import reportes
from src import backups
import datetime

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
    print("12- Ver Todos los Pacientes Registrados")
    print("0- Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == '1':
            print("\n== 1. Registrar Paciente ==")
            dni = input("DNI: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            nacimiento = input("Nacimiento (YYYY-MM-DD): ")
            email = input("Email: ")
            cel = input("Celular: ")
            domicilio = input("Domicilio: ")
            
            pac = Paciente(dni, nombre, apellido, nacimiento, email, cel, domicilio)
            exito = pac.registrar()
            if exito is None:
                print ("ERROR: No se pudo registrar al paciente.")
            elif exito:
                print(f"Paciente {pac.nombre} registado con exito.")
            input("\nPresione ENTER para continuar...")


        elif opcion == '2':
            print("\n== 2. Admitir Paciente ==")

            try:
                #buscar paciente por dni
                pac_dni=input("DNI del Paciente a admitir: ")
                paciente = Paciente.buscar_por_dni(pac_dni)
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

                selec_num= int(input("Seleccione el Numero de habitacion: "))
                hab_elegida=lista_habitaciones[selec_num-1]
                hab_id=hab_elegida['hab_id']

                #fecha
                fecha_ingreso_input = input("Fecha de Ingreso (YYYY-MM-DD) [Presione ENTER para usar la fecha actual]: ")
                fecha_ingreso = None
                if not fecha_ingreso_input:
                    fecha_ingreso = datetime.date.today().isoformat()
                    print(f"Usando fecha actual: {fecha_ingreso}")
                else:
                    fecha_ingreso = fecha_ingreso_input

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
                input("\nPresione ENTER para continuar...")

            except (ValueError, IndexError):
                print("Error: Escribio un numero incorrecto.")
                continue

            except Exception as e:
                print(f"Error inesperado en la admisión: {e}")
                continue
                
        elif opcion == '3':
            print("\n== 3. Habitaciones Disponibles ==")
            lista_habitaciones = Habitacion.obtener_disponibles()
            
            if lista_habitaciones is None:
                print("ERROR: No se pudo obtener la lista de habitaciones.")
            elif not lista_habitaciones:
                print("No hay habitaciones disponibles en este momento")
            else:
                print("\n--- Habitaciones Disponibles ---")
                for hab in lista_habitaciones:
                    print(f"ID: {hab['hab_id']} | Nro: {hab['hab_nro']} | Piso: {hab['hab_piso']}")
            input("Presione ENTER para continuar...")

        elif opcion == '4':
            print("\n== 4. Especialidades Disponibles ==")
            lista_especialidades = Especialidad.obtener_especialidades()
            if lista_especialidades is None:
                print("ERROR: No se pudo obtener la lista de especialidades.")
            elif not lista_especialidades:
                print("No hay especialidades registradas en el sistema.")
            else:
                print("\n--- Especialidades Encontradas ---")
                for esp in lista_especialidades:
                    print(f"ID: {esp['esp_id']} | Nombre: {esp['esp_nombre']}")
            input("\nPresione ENTER para continuar...")

        elif opcion == '5':
            print("\n== 5. Registrar Alta ==")

            try:
                dni_buscar = input("Ingrese el DNI del paciente a dar de alta: ")
                
                admision = Admision.buscar_admision_activa(dni_buscar)
                
                if admision is None:
                    print(f"Error: No se encontró ningún paciente internado con el DNI {dni_buscar}.")
                    continue
                
                print("\n--- Paciente Internado Encontrado ---")
                print(f"  Paciente: {admision['pac_nombre']} {admision['pac_apellido']}")
                print(f"  Habitación: {admision['hab_nro']} (Piso: {admision['hab_piso']})")
                print(f"  Fecha de Ingreso: {admision['adm_fecha_ingreso']}")
                print(f"  (ID Admisión: {admision['adm_id']})")
                
                print("-" * 20)

                confirmar = input(f"¿Desea registrar el ALTA para {admision['pac_nombre']}? (S/N)(presione S para registrar): ")
                
                if confirmar.lower() != 's':
                    print("\nAcción cancelada. Volviendo al menú.")
                    continue 

                print("\n--- Registrando Alta ---")
                
                fecha_alta_input = input("Fecha de Alta (YYYY-MM-DD) [Presione ENTER para usar la fecha actual]: ")
                fecha_alta = None
                if not fecha_alta_input:
                    fecha_alta = datetime.date.today().isoformat()
                    print(f"Usando fecha actual: {fecha_alta}")
                else:
                    fecha_alta = fecha_alta_input
                
                observaciones = input("Observaciones del alta: ")
                
                adm_id = admision['adm_id']
                hab_id = admision['hab_id']

                exito = Admision.registrar_alta(adm_id, fecha_alta, observaciones, hab_id)
                
                if exito:
                    print("¡Alta registrada exitosamente!")
                else:
                    print("Error: No se pudo registrar el alta.")
                input("\nPresion ENTER para continuar...")
            
            except Exception as e:
                print(f"Error inesperado: {e}")

        elif opcion == '6':
            print("\n== 6. Pacientes Internados Actualmente ==")
            lista_internados = Admision.obtener_internados_actuales()

            if lista_internados is None:
                print("ERROR: No se pudo obtener la lista de pacientes")
            elif not lista_internados:
                print("No hay pacientes internados actualmente")
            else:
                print("\n--- Pacientes Internados ---")
                for pac in lista_internados:
                    print(f"  Paciente: {pac['pac_nombre']} {pac['pac_apellido']}")
                    print(f"  Habitación: {pac['hab_nro']} (Piso: {pac['hab_piso']})")
                    print(f"  Fecha de Ingreso: {pac['adm_fecha_ingreso']}")
                    print(f"  (ID Admisión: {pac['adm_id']})")
                    print("-" * 20)
            input("\nPresione ENTER para continuar...")

        elif opcion == '7':
            print("\n== 7. Historial Clínico por Paciente ==")
            dni_buscar = input("Ingrese el DNI del paciente: ")        
            historial = Admision.obtener_historial_paciente(dni_buscar)
            
            if historial is None:                        
                print("Error: No se pudo obtener el historial.")
                        
            elif not historial: 
                print(f"No se encontró historial para el DNI {dni_buscar}.")
            
            else:
                print(f"\n--- Historial de DNI {dni_buscar} ---")
                for adm in historial:                   
                    fecha_alta = adm['adm_fecha_alta'] if adm['adm_fecha_alta'] else '---'
                    medico = f"{adm['med_nombre']} {adm['med_apellido']}" if adm['med_nombre'] else 'No asignado'                   
                    print(f"  ID Admisión: {adm['adm_id']}")
                    print(f"  Ingreso: {adm['adm_fecha_ingreso']}")
                    print(f"  Alta: {fecha_alta}")
                    print(f"  Diagnóstico: {adm['diag_nostico']}")
                    print(f"  Médico: {medico}")
                    print("-" * 20)
            input("\nPresione ENTER para continuar...")

        elif opcion == '8':
            print("\n== 8. Gráfico Promedio Días ==")
            reportes.generar_grafico_promedio_dias()
            input("\nPresione ENTER para continuar...")
            
        elif opcion == '9':
            print("\n== 9. Gráfico Habitaciones ==")
            reportes.generar_grafico_estado_habitaciones()
            input("\nPresione ENTER para continuar...")

        elif opcion == '10':
            print("\n== 10. Exportar Backup ==")          
            backups.exportar_csv()
            input("\nPresione ENTER para continuar...")

        elif opcion == '11':
            print("\n== 11. Restaurar Backup ==")
            backups.importar_csv()
            input("\nPresione ENTER para continuar...")
        
        elif opcion == '12':
            print("\n== Ver Todos los Pacientes Registrados ==")
            lista_pacientes = Paciente.obtener_pacientes()
            
            if lista_pacientes is None:
                print("Error: No se pudo obtener la lista de pacientes.")
            
            elif not lista_pacientes: 
                print("No hay pacientes registrados en el sistema.")
            
            else:
                print("\n--- Lista de Pacientes ---")
                
                for pac in lista_pacientes:
                    print(f"  ID: {pac['pac_id']} | DNI: {pac['pac_dni']} | Nombre: {pac['pac_nombre']} {pac['pac_apellido']}")  

            input("\nPresione ENTER para continuar...")

        elif opcion == '0':
            print("\nSaliendo...")
            break

        else:
            print("\nOpción no válida. Intente de nuevo.")
            
if __name__ == "__main__":
    main()


