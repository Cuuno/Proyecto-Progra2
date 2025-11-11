import sqlite3
import csv
import os
from src import database as db

tablas_backup=['pacientes','especialidades','medicos','diagnosticos','habitaciones','admisiones']
backup_dir="backup.csv"

def exportar_csv():
    """

    """
    print("BACKUPEANDO")

    os.makedirs(backup_dir, exist_ok=True)

    conexion=None
    try:
        conexion=db.db_conexion
        if conexion is None:
            raise Exception ("No se pudo conectar con la DB")
        cursor=conexion.cursor()
        for tabla in tablas_backup:
            print(f"Exportando tabla: {tabla}...")
            pass
        print("BACKUP Complete")
    except Exception as e:
        print (f"BAKCUP ERROR: {e}")
    finally:
        if conexion:
            conexion.close()
def importar_csv():
    """
    
    """
    print("RESTAURANDO")
    conexion=None
    try:
        conexion=db.db_conexion()
        if conexion is None:
            raise Exception("No se pudo conectar con la DB")
        cursor=conexion.cursor()
        for tabla in tablas_backup:
            print(f"Restaurando tabla:{tabla}")
            pass
        print ("RESTORE Complete")
    except Exception as e:
        print (f"RESTORE ERROR: {e}")
    finally:
        if conexion:
            conexion.close()