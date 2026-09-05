# clinicasegura/infraestructura/adaptadores.py
import uuid
from datetime import datetime

class GeneradorFolioUUID:
    """Implementación real del puerto GeneradorFolio usando la librería estándar."""
    def siguiente(self) -> str:
        return str(uuid.uuid4())


class RelojSistema:
    def ahora(self) -> datetime:
        return datetime.now()


class BitacoraMemoria:
    def __init__(self):
        self.eventos = []

    def registrar(self, evento: str, detalle: str) -> None:
        self.eventos.append((evento, detalle))