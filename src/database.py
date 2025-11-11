import sqlite3
def db_conexion():
    try:
        conexion=sqlite3.connect('hospital.db')
        conexion.row_factory=sqlite3.Row
        return conexion
    except sqlite3.Error as e:
        print(f"Error al conectar con la base de daatos: {e}")
        return None
def registrar_paciente(dni,nombre,apellido,nacimiento,email,cel,domicilio):
    conexion=None
    try:
        conexion=db_conexion()
        if conexion is None:
            return False
        cursor=conexion.cursor()
        #codigo de cristian=
    #     sql = """
    #     INSERT INTO pacientes (pac_dni, pac_nombre, pac_apellido, pac_email, pac_cel, pac_domicilio)
    #     VALUES (?, ?, ?, ?, ?, ?)
    #     """
        
    #     # Ejecutamos el SQL, pasando los valores como una tupla
    #     # Esto previene automáticamente la Inyección SQL
    #     cursor.execute(sql, (dni, nombre, apellido, email, cel, domicilio))
        
    #     # ¡IMPORTANTE! Guardar los cambios
    # #     conn.commit()
        
    #     print(f"Paciente {nombre} insertado en la BD (Capa DB).")
    #     return True # Éxito

    except sqlite3.IntegrityError as e:
        # Error si el DNI ya existe (por la restricción UNIQUE)
        print(f"Error en BD - El DNI '{dni}' ya existe: {e}")
        return False
    except sqlite3.Error as e:
        # Atrapa cualquier otro error de SQLite
        print(f"Error general de SQLite en insertar_paciente_db: {e}")
        return False
    finally:
        if conexion:
            conexion.close()

def buscar_paciente_por_dni_db(dni):
    """
    Busca un paciente por DNI.
    (Cristian debe rellenar esto con SELECT * FROM pacientes WHERE pac_dni = ?)
    """
    print(f"DB: Buscando paciente {dni}...")
    pass # Reemplazar con lógica de SQL

# --- CONTRATO DE HABITACIONES ---

def get_habitaciones_disponibles_db():
    """
    Retorna una lista de habitaciones con disponibilidad = True.
    (Cristian debe rellenar esto con SELECT * FROM habitaciones WHERE hab_disponibilidad = 1)
    """
    print("DB: Buscando habitaciones disponibles...")
    pass # Reemplazar con lógica de SQL

def set_habitacion_estado_db(hab_id, estado):
    """
    Cambia el estado de disponibilidad de una habitación.
    (Cristian debe rellenar esto con UPDATE habitaciones SET hab_disponibilidad = ? WHERE hab_id = ?)
    """
    print(f"DB: Cambiando estado de habitación {hab_id} a {estado}...")
    pass # Reemplazar con lógica de SQL

# --- CONTRATO DE ESPECIALIDADES ---

def get_especialidades_db():
    """
    Retorna la lista completa de especialidades.
    (Cristian debe rellenar esto con SELECT * FROM especialidades)
    """
    print("DB: Obteniendo lista de especialidades...")
    pass # Reemplazar con lógica de SQL

# --- CONTRATO DE ADMISIONES (El más complejo) ---

def crear_admision_db(pac_id, med_id, diag_id, hab_id, fecha_ingreso):
    """
    Crea un nuevo registro de admisión.
    (Cristian debe rellenar esto con INSERT INTO admisiones ...)
    """
    print(f"DB: Creando admisión para paciente {pac_id}...")
    pass # Reemplazar con lógica de SQL

def actualizar_alta_db(adm_id, fecha_alta, observaciones):
    """
    Registra el alta en una admisión existente.
    (Cristian debe rellenar esto con UPDATE admisiones SET adm_fecha_alta = ?, ... WHERE adm_id = ?)
    """
    print(f"DB: Registrando alta para admisión {adm_id}...")
    pass # Reemplazar con lógica de SQL

def get_pacientes_internados_db():
    """
    Retorna pacientes con alta IS NULL.
    (Cristian debe rellenar esto con un SELECT ... JOIN ... WHERE adm_fecha_alta IS NULL)
    """
    print("DB: Buscando pacientes internados...")
    pass # Reemplazar con lógica de SQL

def get_historial_paciente_db(dni):
    """
    Retorna todas las admisiones (pasadas y presentes) de un paciente.
    (Cristian debe rellenar esto con un SELECT ... JOIN ... WHERE pacientes.pac_dni = ?)
    """
    print(f"DB: Buscando historial de DNI {dni}...")
    pass # Reemplazar con lógica de SQL

# --- CONTRATO DE REPORTES (Consultas complejas) ---

def get_datos_grafico_promedio_dias_db():
    """
    Retorna el promedio de días por diagnóstico.
    (Cristian debe rellenar esto con SELECT ... AVG(...) ... GROUP BY diag_nostico)
    """
    print("DB: Calculando promedio de días por diagnóstico...")
    pass # Reemplazar con lógica de SQL

def get_datos_grafico_habitaciones_db():
    """
    Retorna el conteo de habitaciones ocupadas vs. libres.
    (Cristian debe rellenar esto con SELECT hab_disponibilidad, COUNT(*) ... GROUP BY hab_disponibilidad)
    """
    print("DB: Contando habitaciones...")
    pass # Reemplazar con lógica de SQL