from abc import ABC, abstractmethod
class Persona(ABC):
    def __init__ (self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    @abstractmethod
    def get_rol(self):
        pass