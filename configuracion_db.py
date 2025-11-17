import sqlite3
db=('hospital.db')#no es necesaria, puedo usar el string directamente
def crear_db():
    print("Iniciando la creacion de la base de datos...")
    try:
        conexion=sqlite3.connect(db)#aqui puedo usar el string
        cursor=conexion.cursor()
        print("Conexión existosa. Creando tablas...")
        sql_script="""
        CREATE TABLE IF NOT EXISTS pacientes(
        pac_id INTEGER PRIMARY KEY AUTOINCREMENT,
        pac_dni INTEGER NOT NULL,
        pac_nombre VARCHAR(30) NOT NULL,
        pac_apellido VARCHAR(30) NOT NULL,
        pac_nacimiento DATE NOT NULL,
        pac_email VARCHAR(30),
        pac_cel INTEGER,
        pac_domicilio VARCHAR(50) NOT NULL
        );

        CREATE TABLE IF NOT EXISTS especialidades(
        esp_id INTEGER PRIMARY KEY AUTOINCREMENT,
        esp_nombre VARCHAR(30)
        );

        CREATE TABLE IF NOT EXISTS habitaciones(
        hab_id INTEGER PRIMARY KEY AUTOINCREMENT,
        hab_nro INTEGER NOT NULL,
        hab_piso INTEGER NOT NULL,
        hab_disponibilidad BOOLEAN NOT NULL
        );

        CREATE TABLE IF NOT EXISTS medicos(
        med_id INTEGER PRIMARY KEY AUTOINCREMENT,
        med_nombre VARCHAR(30) NOT NULL,
        med_apellido VARCHAR(30) NOT NULL,
        esp_id INTEGER,
        CONSTRAINT fk_med_esp FOREIGN KEY (esp_id)
        REFERENCES especialidades (esp_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
        );

        CREATE TABLE IF NOT EXISTS diagnosticos(
        diag_id INTEGER PRIMARY KEY AUTOINCREMENT,
        diag_nostico TEXT
        );

        CREATE TABLE IF NOT EXISTS admisiones(
        adm_id INTEGER PRIMARY KEY AUTOINCREMENT,
        adm_fecha_ingreso DATE NOT NULL,
        adm_fecha_alta DATE,
        adm_observaciones_alta TEXT,
        pac_id INTEGER,
        med_id INTEGER,
        diag_id INTEGER,
        hab_id INTEGER,
        CONSTRAINT fk_adm_pac FOREIGN KEY (pac_id)
        REFERENCES pacientes (pac_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
        CONSTRAINT fk_adm_med FOREIGN KEY (med_id)
        REFERENCES medicos (med_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
        CONSTRAINT fk_adm_diag FOREIGN KEY (diag_id)
        REFERENCES diagnosticos (diag_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
        CONSTRAINT fk_adm_hab FOREIGN KEY (hab_id)
        REFERENCES habitaciones (hab_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
        );
        """
        cursor.executescript(sql_script)
        conexion.commit()
        print("Tablas creadas exitosamente.")
    except sqlite3.Error as e:
        print(f"Error al crear la base de datos: {e}")
    finally:
        if conexion:
            conexion.close()
            print("Conexión cerrada.")

def insertar_datos_de_prueba():
    print("Insertando datos de prueba a la DB...")
    try:
        conexion=sqlite3.connect(db)#aqui puedo usar el string
        cursor=conexion.cursor()
        print("Conexión existosa. Insertando datos...")
        # --- ESPECIALIDADES ---
        especialidades = [
            ('Cardiología',),
            ('Traumatología',),
            ('Clínica Médica',),
            ('Nutrición',),
            ('Proctología',),
            ('Neurología',),
            ('Endocrinología',)
        ]
       
        cursor.executemany("INSERT OR IGNORE INTO especialidades (esp_nombre) VALUES (?)", especialidades)

        # --- MEDICOS ---
        medicos = [
            ('Lionel', 'Messi', 3),
            ('René', 'Favaloro', 1),
            ('Julián', 'Alvarez', 2),
            ('Dibu', 'Martinez', 2),
            ('Juan','Pérez',7),
            ('Elias','Tapia',6),
            ('Analia','Torres',4),
            ('Olivia','Paganeti',5)
            ]
        cursor.executemany("INSERT OR IGNORE INTO medicos (med_nombre, med_apellido, esp_id) VALUES (?, ?, ?)", medicos)

        # --- HABITACIONES ---
        habitaciones = [
            # (id, nro, piso, disponibilidad: 1=Libre, 0=Ocupada)
            (101, 1, 1),
            (102, 1, 1),
            (103, 1, 1),
            (104, 1, 1),
            (105, 1, 1),
            (201, 2, 1),
            (202, 2, 1),
            (203, 2, 1),
            (204, 2, 1),
            (205, 2, 1),
            (301, 3, 1),
            (302, 3, 1),
            (303, 3, 1),
            (304, 3, 1),
            (305, 3, 1),
            (401, 4, 1),
            (402, 4, 1),
            (403, 4, 1),
            (404, 4, 1),
            (405, 4, 1)
        ]
        cursor.executemany("INSERT OR IGNORE INTO habitaciones (hab_nro, hab_piso, hab_disponibilidad) VALUES (?, ?, ?)", habitaciones)

        # --- DIAGNÓSTICOS DE PRUEBA ---
        diagnosticos = [
            ('Gripe A',),
            ('Quebradura de pie',),
            ('Tuberculosis',)
        ]
        cursor.executemany("INSERT OR IGNORE INTO diagnosticos (diag_nostico) VALUES (?)", diagnosticos)

        conexion.commit()
        print("DB: Datos de prueba insertados exitosamente.")

    except sqlite3.Error as e:
        print(f"DB ERROR al insertar datos de prueba: {e}")
        conexion.rollback() 

if __name__ == "__main__":
    crear_db()
    insertar_datos_de_prueba()