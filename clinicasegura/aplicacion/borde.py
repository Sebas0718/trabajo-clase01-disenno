# clinicasegura/aplicacion/borde.py
import re

def validar_cedula_regex(cedula: str) -> bool:
    """Reemplazamos el for iterativo viejo por una expresión regular de la librería estándar."""
    return bool(re.match(r"^\d-\d{4}-\d{4}$", cedula))