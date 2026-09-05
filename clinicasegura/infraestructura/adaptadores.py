# clinicasegura/infraestructura/adaptadores.py
import uuid

class GeneradorFolioUUID:
    """Implementación real del puerto GeneradorFolio usando la librería estándar."""
    def siguiente(self) -> str:
        return str(uuid.uuid4())