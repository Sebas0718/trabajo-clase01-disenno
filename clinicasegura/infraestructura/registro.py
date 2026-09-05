# clinicasegura/infraestructura/registro.py
from clinicasegura.dominio.errores import CadenaNoSoportada

def construir_registro(pasarelas: dict):
    """Construye un diccionario o mapa de pasarelas registradas."""
    return pasarelas