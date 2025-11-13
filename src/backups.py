import sqlite3
import csv
import os
from src import database as db

tablas_backup=['pacientes','especialidades','medicos','diagnosticos','habitaciones','admisiones']
backup_dir="backup_csv"

# Opción 10: Exportar Backup (CSV)
def exportar_csv():
    print("BACKUPEANDO...")

    os.makedirs(backup_dir, exist_ok=True)

    conexion=None
    try:
        conexion=db.db_conexion()

        if conexion is None:
            raise Exception ("No se pudo conectar con la DB")
        
        cursor=conexion.cursor()

        for tabla in tablas_backup:
            print(f"Exportando tabla: {tabla}...")
            cursor.execute(f"SELECT * FROM {tabla}")
            filas=cursor.fetchall()
            path_archivo= os.path.join(backup_dir, f"{tabla}.csv")
            with open (path_archivo,'w',newline='',encoding='utf-8') as f:
                writer = csv.writer(f)
                headers = [col[0] for col in cursor.description]
                writer.writerow(headers)
                writer.writerows(filas)
        print("BACKUP Completado")

    except Exception as e:
        print (f"BACKUP ERROR: {e}")

    finally:
        if conexion:
            conexion.close()

# Opción 11: Restaurar Backup (CSV)
def importar_csv():
    print("RESTAURANDO...")

    conexion=None

    try:
        conexion=db.db_conexion()

        if conexion is None:
            raise Exception("No se pudo conectar con la DB")
        
        cursor=conexion.cursor()

        cursor.execute("PRAGMA foreign_keys = OFF;")

        for tabla in tablas_backup:
            print(f"Restaurando tabla:{tabla}")
            cursor.execute(f"DELETE FROM {tabla}")
            path_archivo = os.path.join(backup_dir, f"{tabla}.csv")
            if not os.path.exists(path_archivo):
                print(f"OJO! No se encontro {path_archivo}, saltando.")
                continue

            with open(path_archivo, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                headers = next(reader,None)
                placeholders=','.join(['?']*len(headers))
                sql_insert = f"INSERT INTO {tabla} ({','.join(headers)}) VALUES ({placeholders})"

                cursor.executemany(sql_insert, reader)
        
        conexion.commit()

        cursor.execute("PRAGMA foreign_keys = ON")
            
        print ("RESTAURACION Completada")

    except Exception as e:
        print (f"ERROR AL RESTAURAR: {e}")

    finally:
        if conexion:
            conexion.close()