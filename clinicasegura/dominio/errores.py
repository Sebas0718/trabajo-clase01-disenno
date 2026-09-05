# clinicasegura/dominio/errores.py
class ErrorDominio(Exception):
    """Clase base para todos los errores de nuestro negocio."""
    pass

class RecetaInvalida(ErrorDominio):
    """Se lanza cuando los datos de la receta no son válidos."""
    pass

class CadenaNoSoportada(ErrorDominio):
    """Se lanza cuando se intenta despachar a una cadena de farmacias que no existe."""
    pass

class FarmaciaNoDisponible(ErrorDominio):
    """Se lanza cuando la farmacia externa no responde o da timeout."""
    pass