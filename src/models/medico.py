from src.models.persona import Persona
class Medico(Persona):
    def __init__(self, nombre, apellido, nacimiento, email, cel, domicilio):
        super().__init__(nombre,apellido)
        self.nacimiento = nacimiento
        self.email = email
        self.cel = cel
        self.domicilio = domicilio
        self.esp_id = esp_id
        print (f"Objeto Medico '{self.nombre}'creado en memoria")
    def registrar_medico(self):
        con = ConexionDB().conectar()
        cur = con.cursor()
        '''''
        try:
            cur.execute("""
                INSERT INTO medicos (med_nombre, med_apellido, esp_id)
                VALUES (?, ?, ?)
            """, (self.nombre, self.apellido, self.esp_id))
            con.commit()
            print(f"✅ Médico '{self.nombre} {self.apellido}' registrado correctamente.")
        except sqlite3.Error as e:
            print(f" Error al registrar médico: {e}")
        finally:
            con.close()
        '''
    @staticmethod
    def eliminar_medico(self):
        pass
    def get_rol(self):
        return "Medico"

 