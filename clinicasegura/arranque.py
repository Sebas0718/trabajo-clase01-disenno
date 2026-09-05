# clinicasegura/arranque.py
import os
from clinicasegura.dominio.servicio import EmisionDeRecetas
from clinicasegura.infraestructura.adaptadores import (
    BitacoraMemoria,
    GeneradorFolioUUID,
    RelojSistema,
)
from clinicasegura.infraestructura.registro import construir_registro

def construir_servicio():
    configuracion = {
        "vigencia_dias": int(os.getenv("VIGENCIA_DIAS", 30)),
        "tarifa_diaria": int(os.getenv("TARIFA_DIARIA", 250)),
        "timeout": float(os.getenv("TIMEOUT", 1.5))
    }
    pasarelas = construir_registro({})
    return EmisionDeRecetas(
        pasarelas=pasarelas,
        reloj=RelojSistema(),
        folios=GeneradorFolioUUID(),
        bitacora=BitacoraMemoria(),
    )