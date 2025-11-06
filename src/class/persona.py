from abc import ABC, abstractmethod
class Persona(ABC):
    def __init__ (self,dni,nombre,apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        print (f"Objeto Persona {self.nombre} inicializado")
    @abstractmethod
    def get_rol(self):
        pass