from src import database as db
from src.models.paciente import Paciente
class Admision ():
    def __init__ (self, pac_id, med_id, diag_id, hab_id, fecha_ingreso):
        self.pac_id = pac_id       
        self.med_id = med_id       
        self.diag_id = diag_id     
        self.hab_id = hab_id       
        self.adm_fecha_ingreso = fecha_ingreso
        self.adm_id = None 
        self.adm_fecha_alta = None
        self.adm_observaciones_alta = None
   
    @staticmethod
    def registrar_ingreso_por_dni(dni_paciente, med_id, diag_id, hab_id, fecha_ingreso):
            print(f"MODELO: Iniciando admisión por DNI {dni_paciente}...")
            paciente_encontrado = Paciente.buscar_por_dni(dni_paciente)
            if not paciente_encontrado:
                print(f"Paciente no encontrado.") 
                return False
            pac_id = paciente_encontrado['pac_id']
            
            try:
                exito_adm = db.crear_admision_db(pac_id, med_id, diag_id, hab_id, fecha_ingreso)            
                if not exito_adm:
                    return False            
                exito_hab = db.actualizar_habitacion_estado_db(hab_id, 0)
                return exito_hab 
            except Exception as e:
                return False
    
    @staticmethod
    def obtener_internados_actuales():
        print("MODELO: Pidiendo lista de pacientes internados...")
        try:
            lista_internados=db.obtener_pacientes_internados_db()
            return lista_internados
        except Exception as e:
            print (f"MODELO ERROR: Fallo inesperado al llamar a la BD: {e}")
            return None
        
    @staticmethod
    def obtener_historial_paciente(dni):
        print (f"MODELO: Pidiendo historial de DNI {dni}...")
        try:
            historial=db.obtener_historial_paciente_db(dni)
            return historial
        except Exception as e:
            print (f"MODELO ERROR: Fallo inesperado al llamar a la BD: {e}")
            return None
        
    @staticmethod
    def buscar_admision_activa(dni):
        print(f"MODELO: Buscando admisión activa para DNI {dni}...")
        try:
            admision=db.buscar_admision_activa_por_dni_db(dni)
            return admision
        except Exception as e:
            print(f"MODELO ERROR: Fallo inesperado al llamar a la BD: {e}")
            return None

    @staticmethod
    def registrar_alta(adm_id, fecha_alta, observaciones, hab_id):

        print(f"MODELO: Registrando alta para admisión {adm_id}...")
        try:
            exito_alta = db.actualizar_alta_db(adm_id, fecha_alta, observaciones)
            if not exito_alta:
                print("MODELO ERROR: No se pudo actualizar la admisión (ID no existe).")
                return False

            exito_hab = db.actualizar_habitacion_estado_db(hab_id, 1) 
            if not exito_hab:
                print("MODELO ADVERTENCIA: Alta registrada, pero no se pudo liberar la habitación.")
                pass

            print("MODELO: Alta registrada y habitación liberada.")
            return True
        except Exception as e:
            print(f"MODELO ERROR: Fallo inesperado al registrar el alta: {e}")
            return False