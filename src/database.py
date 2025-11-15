import sqlite3
# Conexion con la base de datos
def db_conexion():
    try:
        conexion=sqlite3.connect('hospital.db')
        conexion.row_factory=sqlite3.Row
        return conexion
    except sqlite3.Error as e:
        print(f"Error al conectar con la base de daatos: {e}")
        return None
    
# Construcción de la opcion 1    
def registrar_paciente_db(dni,nombre,apellido,nacimiento,email,cel,domicilio):
    conexion=None
    try:
        conexion=db_conexion()
        if conexion is None:
            return False
        cursor=conexion.cursor()

        sql = """
        INSERT INTO pacientes (pac_dni, pac_nombre, pac_apellido, pac_nacimiento, pac_email, pac_cel, pac_domicilio)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (dni, nombre, apellido, nacimiento, email, cel, domicilio))
        conexion.commit()

        print(f"Paciente {nombre} {apellido} insertado en la BD (Capa DB).")
        return True
    
    except sqlite3.IntegrityError as e:
        print(f"Error en BD - El DNI '{dni}' o el email '{email}' ya existen: {e}")
        if conexion:
            conexion.rollback()
        return False
    except sqlite3.Error as e:
        print(f"Error general de SQLite en registrar_paciente: {e}")
        if conexion:
            conexion.rollback()
    finally:
        if conexion:
            conexion.close()    

# Construcción de la opcion 2
def buscar_por_dni_db(dni):
    conexion=None
    try:
        conexion=db_conexion()
        if conexion is None:
            return None
        cursor = conexion.cursor() 
        sql= "SELECT * FROM pacientes WHERE pac_dni = ?"

        cursor.execute(sql,(dni,))
        paciente=cursor.fetchone()

        if paciente:
            print (f"DB: Paciente {dni} encontrado.")
            return paciente
        else:
            print (f"DB: Paciente {dni} no encontrado.")
            return None
    except sqlite3.Error as e:
        print (f"Error General de SQLite en buscar paciente: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

# Construcción de la opcion 2
def obtener_medicos_db():
    conexion = None
    try:
        conexion = db_conexion()
        if conexion is None: 
            return None
        cursor = conexion.cursor()
        sql = """
        SELECT m.med_id, m.med_nombre, m.med_apellido, e.esp_nombre
        FROM medicos m
        LEFT JOIN especialidades e ON m.esp_id = e.esp_id
        ORDER BY m.med_apellido
        """
        cursor.execute(sql)
        medicos = cursor.fetchall()
        return medicos
    except sqlite3.Error as e:
        print(f"DB ERROR en obtener_medicos_db: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

# Construcción de la opcion 2
def obtener_diagnosticos_db():
    conexion = None
    try:
        conexion = db_conexion()
        if conexion is None: 
            return None
        cursor = conexion.cursor()
        sql = "SELECT * FROM diagnosticos ORDER BY diag_nostico"
        cursor.execute(sql)
        diagnosticos = cursor.fetchall()
        return diagnosticos
    except sqlite3.Error as e:
        print(f"DB ERROR en obtener diagnosticos: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

# Construcción de la opcion 2
def crear_diagnostico_db(descripcion):
    conexion = None
    try:
        conexion = db_conexion()
        if conexion is None: 
            return None
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnosticos (diag_nostico) VALUES (?)"
        cursor.execute(sql, (descripcion,))
        conexion.commit()
        nuevo_id = cursor.lastrowid
        return nuevo_id
    except sqlite3.IntegrityError: return None
    except sqlite3.Error as e:
        print(f"DB ERROR en crear_diagnostico_db: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

# Construcción de la opcion 2 y sirve para la opcion 3
def obtener_habitaciones_disponibles_db():
    conexion= None
    try:
        conexion = db_conexion()
        if conexion is None: 
            return None
        cursor = conexion.cursor()
        sql = "SELECT * FROM habitaciones WHERE hab_disponibilidad = 1 ORDER BY hab_piso, hab_nro"
        cursor.execute(sql)
        habitaciones = cursor.fetchall()
        print(f"DB: Hay {len(habitaciones)} habitaciones disponibles.")
        return habitaciones
    except sqlite3.Error as e:
        print (f"DB ERROR en obtener habitaciones: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

# Construcción de la opcion 2
def crear_admision_db(pac_id, med_id, diag_id, hab_id, fecha_ingreso):
    conexion = None
    try:
        conexion = db_conexion()
        if conexion is None: return False
        cursor = conexion.cursor()
        sql = "INSERT INTO admisiones (pac_id, med_id, diag_id, hab_id, adm_fecha_ingreso) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(sql, (pac_id, med_id, diag_id, hab_id, fecha_ingreso))
        conexion.commit()
        return True
    except sqlite3.Error as e:
        print(f"DB ERROR en crear_admision_db: {e}")
        return False
    finally:
        if conexion:
            conexion.close()

# Construcción de la opcion 2 y sirve para la opcion 5
def actualizar_habitacion_estado_db(hab_id, estado):
    conexion=None
    try:
        conexion=db_conexion()
        if conexion is None:
            return False
        cursor = conexion.cursor()
        sql = "UPDATE habitaciones SET hab_disponibilidad = ? WHERE hab_id = ?"
        cursor.execute(sql, (estado,hab_id))
        conexion.commit()
        return True
    except sqlite3.Error as e:
        print (f"DB ERROR en actualizar estado de habitacion: {e}")
        return False
    finally:
        if conexion:
            conexion.close()       

# Construcción de la opcion 4
def obtener_especialidades_db():
    print("DB: Obteniendo lista de especialidades...")
    conexion=None
    try:
        conexion=db_conexion()
        if conexion is None:
            return None
        cursor=conexion.cursor()
        sql="SELECT * FROM especialidades ORDER BY esp_nombre"
        cursor.execute(sql)
        especialidades=cursor.fetchall()
        print(f"DB: Encontradas {len(especialidades)} especialidades.")
        return especialidades
    except sqlite3.Error as e:
        print (f"DB ERROR en obtener especialidades: {e}")
    finally:
        if conexion:
            conexion.close

# Construcción de la opcion 5
def buscar_admision_activa_por_dni_db(dni):
    conexion = None
    try:
        conexion = db_conexion()
        if conexion is None: 
            return None
        cursor = conexion.cursor()
        sql = """
        SELECT a.adm_id, a.hab_id, p.pac_nombre, p.pac_apellido, 
               h.hab_nro, h.hab_piso, a.adm_fecha_ingreso
        FROM admisiones a
        JOIN pacientes p ON a.pac_id = p.pac_id
        JOIN habitaciones h ON a.hab_id = h.hab_id
        WHERE p.pac_dni = ? AND a.adm_fecha_alta IS NULL
        """
        cursor.execute(sql, (dni,))
        admision_activa = cursor.fetchone()
        return admision_activa
    except sqlite3.Error as e:
        print(f"DB ERROR en buscar_admision_activa_por_dni_db: {e}")
        return None
    finally:
        if conexion: conexion.close()

# Construcción de la opcion 5
def actualizar_alta_db(adm_id, fecha_alta, observaciones):
    conexion= None
    try:
        conexion=db_conexion()
        if conexion is None:
            return None
        cursor=conexion.cursor()
        sql="""
        UPDATE admisiones 
        SET adm_fecha_alta = ?, adm_observaciones_alta = ?
        WHERE adm_id = ?
        """
        cursor.execute(sql, (fecha_alta, observaciones, adm_id))
        conexion.commit()
        if cursor.rowcount == 0: return False 
        return True
    except sqlite3.Error as e:
        print(f"DB ERROR en actualizar_alta_db: {e}")
        return False
    finally:
        if conexion: conexion.close()

# Construcción de la opcion 6 y sirve para la opcion 5
def obtener_pacientes_internados_db():
    conexion=None
    try:
        conexion=db_conexion()
        if conexion is None:
            return None
        cursor=conexion.cursor()
        sql="""
        SELECT 
            a.adm_id,
            p.pac_nombre,
            p.pac_apellido,
            h.hab_nro,
            h.hab_piso,
            a.adm_fecha_ingreso
        FROM admisiones a
        JOIN pacientes p ON a.pac_id = p.pac_id
        JOIN habitaciones h ON a.hab_id = h.hab_id
        WHERE a.adm_fecha_alta IS NULL
        ORDER BY a.adm_fecha_ingreso ASC
        """
        cursor.execute(sql)
        pacientes_internados=cursor.fetchall()

        print(f"DB: Se encontraron {len(pacientes_internados)} pacientes internados")
        return pacientes_internados
    except sqlite3.Error as e:
        print (f"DB ERROR en obtener pacientes: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

# Construcción de la opcion 7
def obtener_historial_paciente_db(dni):
    conexion=None
    try:
        conexion=db_conexion()
        if conexion is None:
            return None
        
        cursor=conexion.cursor()
        sql="""
        SELECT 
            a.adm_id, 
            a.adm_fecha_ingreso, 
            a.adm_fecha_alta, 
            d.diag_nostico,
            m.med_nombre,
            m.med_apellido
        FROM 
            admisiones a
        JOIN 
            pacientes p ON a.pac_id = p.pac_id
        LEFT JOIN 
            diagnosticos d ON a.diag_id = d.diag_id
        LEFT JOIN 
            medicos m ON a.med_id = m.med_id
        WHERE 
            p.pac_dni = ?
        ORDER BY 
            a.adm_fecha_ingreso DESC
        """
        cursor.execute(sql,(dni,))

        historial=cursor.fetchall()

        print (f"DB: Historial encontrado para DNI {dni} (filas: {len(historial)})")
        return historial
    except sqlite3.Error as e:
        print (f"DB ERROR en obtener historial del paciente: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

# Construcción de la opcion 8
def obtener_datos_grafico_promedio_dias_db():
    conexion=None
    try:
        conexion=db_conexion()
        if conexion is None:
            return None, None
        sql = """
        SELECT 
            d.diag_nostico AS Diagnostico, 
            AVG( JULIANDAY(a.adm_fecha_alta) - JULIANDAY(a.adm_fecha_ingreso) ) AS Promedio_Dias
        FROM 
            admisiones a
        JOIN 
            diagnosticos d ON a.diag_id = d.diag_id
        WHERE 
            a.adm_fecha_alta IS NOT NULL  -- ¡Solo admisiones CERRADAS!
        GROUP BY 
            d.diag_nostico
        ORDER BY
            Promedio_Dias DESC
        """

        print ("DB: Ejecutando consulta de promedio de dias...")
        return sql, conexion
    except sqlite3.Error as e:
        print (f"ERROR en obtener datos para el grafico: {e}")
        if conexion:
            conexion.close()
        return None, None

# Construcción de la opcion 9
def obtener_datos_grafico_habitaciones_db():
    conexion=None
    try:
        conexion=db_conexion()
        if conexion is None:
            return None, None
        
        sql="""
            SELECT 
                CASE 
                    WHEN hab_disponibilidad = 1 THEN 'Libres'
                    ELSE 'Ocupadas'
                END AS Estado,
                COUNT(*) AS Cantidad
            FROM 
                habitaciones
            GROUP BY 
                hab_disponibilidad
            """
        print("DB: Ejecutando consulta de estado de habitaciones...")
        return sql, conexion
    except sqlite3.Error as e:
        print (f"ERROR en obtener datos para el grafico: {e}")
        if conexion:
            conexion.close()
        return None, None

# Construccion de la opcion 12
def obtener_todos_los_pacientes_db():
    conexion = None
    try:
        conexion = db_conexion() 
        if conexion is None: 
            return None 
        
        cursor = conexion.cursor()
        
        sql = "SELECT pac_id, pac_dni, pac_nombre, pac_apellido FROM pacientes ORDER BY pac_apellido"
        cursor.execute(sql)
        
        pacientes = cursor.fetchall()
        
        print(f"DB: Encontrados {len(pacientes)} pacientes en total.")
        return pacientes

    except sqlite3.Error as e:
        print(f"DB ERROR en obtener todos los pacientes: {e}")
        return None
    finally:
        if conexion:
            conexion.close()        