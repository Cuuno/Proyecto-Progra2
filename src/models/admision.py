from src import database as db
class Admision ():
    def __init__ (self,ingreso,alta,observacion):
        self.ingreso = ingreso
        self.alta = alta
        self.observacion = observacion
def registrar_ingreso_por_dni():
    # ... (Paso 1: Central busca el pac_id usando el DNI...)
        paciente_encontrado = Paciente.buscar_por_dni(dni_paciente)
        if not paciente_encontrado: return False
        pac_id = paciente_encontrado['pac_id']
        
        try:
            # --- ¡AQUÍ ESTÁ TU LÓGICA "AUTOMÁTICA"! ---
            
            # PASO A: Central llama a la herramienta 1 de Cristian
            exito_adm = db.crear_admision_db(pac_id, med_id, diag_id, hab_id, fecha_ingreso)
            
            if not exito_adm:
                return False # Falla al crear la admisión

            # PASO B: Central llama a la herramienta 2 de Cristian
            exito_hab = db.actualizar_habitacion_estado_db(hab_id, 0) # 0 = Ocupada
            
            return exito_hab # Si ambos tuvieron éxito, devuelve True

        except Exception as e:
            return False