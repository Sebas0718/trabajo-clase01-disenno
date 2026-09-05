# clinicasegura/aplicacion/borde.py
import re
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field, field_validator

from clinicasegura.dominio.modelos import Cedula, Receta


class SolicitudReceta(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    cedula: str
    medicamento: str
    dias: int = Field(gt=0, le=90)
    dosis_mg: Decimal = Field(gt=0)
    riesgo_alto: bool = False

    @field_validator("cedula")
    @classmethod
    def cedula_valida(cls, cedula):
        if not re.fullmatch(r"\d-\d{4}-\d{4}", cedula):
            raise ValueError("la cédula debe tener formato 0-0000-0000")
        return cedula


def a_receta(solicitud: SolicitudReceta) -> Receta:
    return Receta(
        cedula=Cedula(solicitud.cedula),
        medicamento=solicitud.medicamento,
        dias=solicitud.dias,
        dosis_mg=solicitud.dosis_mg,
        riesgo_alto=solicitud.riesgo_alto,
    )


def validar_cedula_regex(cedula: str) -> bool:
    return bool(re.fullmatch(r"\d-\d{4}-\d{4}", cedula))