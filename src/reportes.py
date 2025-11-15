import pandas as pd
import matplotlib.pyplot as plt
from src import database as db

# Opción 8: Gráfico de Promedio de Días
def generar_grafico_promedio_dias():
    print ("REPORTES: Iniciando grafico de promedio de dias...")
    sql_query, conexion = None, None
    try:
        sql_query, conexion=db.obtener_datos_grafico_promedio_dias_db()
        if sql_query is None or conexion is None:
            print ("REPORTES ERROR: No se pudieron obtener los datos de la DB")
            return
        df=pd.read_sql_query(sql_query, conexion)

        if df.empty:
            print ("REPORTES: No hay datos de admisiones cerradas para graficar")
            return
        print("REPORTES: Datos recibidos de la DB, generando grafico...")
        
        df.plot(
            kind='bar',
            x='Diagnóstico',
            y='Promedio_dias',
            title='Promedio de días de Internación por Diagnóstico',
            legend=False
        )

        plt.ylabel('Días Promedio')
        plt.xlabel('Diagnóstico')
        plt.tight_layout()

        file='grafico_prom_dias.png'
        plt.savefig(file)
        print (f"REPORTES: Gráfico Guardado como '{file}'")

    except Exception as e:
        print(f"REPORTES ERROR: Error inesperado al generar gráfico: {e}")
    finally:
        if conexion:
            conexion.close()
            
# Opción 9: Grafico de Habitaciones
def generar_grafico_estado_habitaciones():
    print("REPORTES: Iniciando gráfico de estado de habitaciones...")
    sql_query, conexion = None, None
    try:
        sql_query, conexion = db.obtener_datos_grafico_habitaciones_db()

        if sql_query is None or conexion is None:
            print ("REPORTES ERROR: No se obtuvieron los datos de la DB")
            return
        
        df = pd.read_sql_query(sql_query,conexion)

        if df.empty:
            print ("REPORTES: No hay datos de habitaciones para graficar.")
            return
        
        print ("REPORTES: Datos recibidos, generando gráfico...")

        df.set_index('Estado', inplace=True)

        df.plot(
            kind='pie',
            y='Cantidad',
            title='Estado de ocupacion de Habitaciones',
            autopct='%1.1f%%',
            legend=False
        )

        plt.ylabel("")
        plt.tight_layout()

        file="grafico_habitaciones.png"
        plt.savefig(file)
        print (f"REPORTES: Gráfico guardado como {file}")

    except Exception as e:
        print(f"REPORTES ERROR: Error inesperado al generar gráfico: {e}")
    
    finally:
        if conexion:
            conexion.close()