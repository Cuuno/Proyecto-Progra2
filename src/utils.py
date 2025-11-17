import sys
import os

def resource_path(relative_path):
    """
    Obtiene la ruta absoluta al recurso.
    Funciona para desarrollo (ejecutando .py) y
    para despliegue (ejecutando .exe de PyInstaller).
    """
    try:
        # PyInstaller crea una carpeta temporal y guarda la ruta en _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # Si no está "congelado" (es un .py), usa la ruta normal
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)