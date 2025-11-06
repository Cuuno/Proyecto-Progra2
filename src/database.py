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

    # except sqlite3.IntegrityError as e:
    #     # Esto es clave: Se activa si el DNI ya existe (por la restricción UNIQUE)
    #     print(f"Error en BD - El DNI '{dni}' ya existe: {e}")
    #     return False
    # except sqlite3.Error as e:
    #     # Atrapa cualquier otro error de SQLite
    #     print(f"Error general de SQLite en insertar_paciente_db: {e}")
    #     return False
    # finally:
    #     # PASE LO QUE PASE (éxito o error), cerrar la conexión
    #     if conn:
    #         conn.close()
