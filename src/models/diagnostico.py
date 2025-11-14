from src import database as db
class Diagnostico ():
    def __init__(self, diagnostico):
        self.diagnostico = diagnostico
    def obtener_diagnosticos():
        print("MODELO: Pidiendo lista de todos los diagnósticos...")
        try:
            return db.obtener_diagnosticos_db()
        except Exception as e:
            print(f"MODELO ERROR: {e}")
            return None
    def crear_diagnostico(descripcion):
        print(f"MODELO: Creando nuevo diagnóstico: {descripcion}...")       
        try:
            diag_id = db.crear_diagnostico_db(descripcion)
            return diag_id
        except Exception as e:
            print(f"MODELO ERROR: {e}")
            return None