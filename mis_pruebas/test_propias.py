# mis_pruebas/test_propias.py
import pytest
from clinicasegura.dominio.errores import FarmaciaNoDisponible
from clinicasegura.dominio.modelos import Receta, Cedula
from clinicasegura.dominio.servicio import EmisionDeRecetas
from clinicasegura.aplicacion.borde import SolicitudReceta, a_receta

class RelojFijo:
    def ahora(self):
        return "2026-03-01 09:00:00"

class FolioSecuencial:
    def siguiente(self):
        return "999999"

class BitacoraEspia:
    def __init__(self):
        self.eventos = []
    def registrar(self, evento, detalle):
        self.eventos.append((evento, detalle))

class PasarelaMock:
    def enviar(self, receta, folio, vence):
        class DespachoMock:
            def __init__(self):
                self.folio = folio
                self.cadena = "test"
                self.vence = vence
        return DespachoMock()

class PasarelaCaida:
    def enviar(self, receta, folio, vence):
        raise TimeoutError("Conexión agotada con la farmacia")

def test_vigencia_con_reloj_fijo():
    """1) Prueba la vigencia determinista usando un reloj inyectado."""
    servicio = EmisionDeRecetas(
        pasarelas={"test": PasarelaMock()},
        reloj=RelojFijo(),
        folios=FolioSecuencial(),
        bitacora=BitacoraEspia()
    )
    receta = Receta(cedula=Cedula("1-1234-5678"), dias=30, dosis_mg=500.0)
    despacho = servicio.emitir(receta, "test")
    assert despacho.vence.isoformat() == "2026-03-31"

def test_cadena_caida_lanza_timeout():
    """2) Simula una cadena caída que lanza TimeoutError de red."""
    servicio = EmisionDeRecetas(
        pasarelas={"caida": PasarelaCaida()},
        reloj=RelojFijo(),
        folios=FolioSecuencial(),
        bitacora=BitacoraEspia()
    )
    receta = Receta(cedula=Cedula("1-1234-5678"), dias=30, dosis_mg=500.0)
    with pytest.raises(FarmaciaNoDisponible) as error:
        servicio.emitir(receta, "caida")
    assert "caida" in str(error.value)

def test_receta_invalida_rechazada_en_borde():
    """3) Rechaza una receta inválida antes de entrar al dominio."""
    with pytest.raises(ValueError):
        a_receta(SolicitudReceta(
            cedula="12345678",
            medicamento="amoxicilina",
            dias=30,
            dosis_mg=500,
        ))