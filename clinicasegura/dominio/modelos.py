# clinicasegura/dominio/modelos.py
from dataclasses import dataclass

@dataclass(frozen=True)
class Cedula:
    valor: str

@dataclass(frozen=True)
class Receta:
    cedula: Cedula
    dias: int
    dosis_mg: float
    riesgo_alto: bool = False
    medicamento: str = ""

@dataclass(frozen=True)
class Despacho:
    folio: str
    cadena: str
    vence: str