# clinicasegura/dominio/puertos.py
from typing import Protocol
from decimal import Decimal
from clinicasegura.dominio.modelos import Receta, Despacho

class Pasarela(Protocol):
    """Puerto para enviar recetas a las farmacias externas."""
    def enviar(self, receta: Receta) -> Despacho:
        pass

class Reloj(Protocol):
    """Puerto para saber la fecha actual sin acoplarnos al sistema."""
    def ahora(self) -> str:
        pass

class GeneradorFolio(Protocol):
    """Puerto para generar números de folio sin usar random directo."""
    def siguiente(self) -> str:
        pass

        
class Bitacora(Protocol):
    """Puerto para registrar eventos sin depender de SQLite."""
    def registrar(self, evento: str, detalle: str) -> None:
        pass