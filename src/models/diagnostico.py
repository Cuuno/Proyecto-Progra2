from src import database as db
class Diagnostico ():
    def __init__(self, diagnostico):
        self.diagnostico = diagnostico
    @staticmethod
    def obtener_diagnosticos():
        print("MODELO: Pidiendo lista de todos los diagnósticos...")
        try:
            lista_diagnosticos=db.obtener_diagnosticos_db()
            return lista_diagnosticos
        except Exception as e:
            print(f"MODELO ERROR: {e}")
            return None
 
    @staticmethod
    def crear_diagnostico(descripcion):
        print(f"MODELO: Creando nuevo diagnóstico: {descripcion}...")       
        try:
            diag_id = db.crear_diagnostico_db(descripcion)
            return diag_id
        except Exception as e:
            print(f"MODELO ERROR: {e}")
            return None