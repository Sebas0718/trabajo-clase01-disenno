# clinicasegura/dominio/servicio.py
from clinicasegura.dominio.modelos import Receta

class EmisionDeRecetas:
    def __init__(self, configuracion: dict = None):
        # La configuración se inyecta, no es global
        self.configuracion = configuracion

    def emitir(self, receta: Receta, cadena: str):
        # Recibe el objeto Receta, nunca un diccionario crudo
        pass