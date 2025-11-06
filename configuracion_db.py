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
if __name__ == "__main__":
    crear_db()