# clinicasegura/dominio/servicio.py
from clinicasegura.dominio.modelos import Receta, Despacho
from clinicasegura.dominio.errores import CadenaNoSoportada, FarmaciaNoDisponible
from datetime import datetime, timedelta

class EmisionDeRecetas:
    def __init__(self, pasarelas, reloj, folios, bitacora):
        self.pasarelas = pasarelas
        self.reloj = reloj
        self.folios = folios
        self.bitacora = bitacora

    def emitir(self, receta: Receta, cadena: str) -> Despacho:
        pasarela = self._buscar_pasarela(cadena)
        if pasarela is None:
            raise CadenaNoSoportada(f"La cadena '{cadena}' no está soportada.")

        folio = str(self.folios.siguiente())
        ahora = self.reloj.ahora()
        fecha_base = (datetime.fromisoformat(ahora)
                      if isinstance(ahora, str) else ahora)
        vence = (fecha_base + timedelta(days=30)).date()

        try:
            pasarela.enviar(receta, folio, vence)
        except TimeoutError as error:
            detalle = f"{cadena} no disponible para el folio {folio}: {error}"
            self.bitacora.registrar("farmacia_no_disponible", detalle)
            raise FarmaciaNoDisponible(detalle) from error

        despacho = Despacho(folio=folio, cadena=cadena, vence=vence)
        self.bitacora.registrar("receta_emitida", folio)
        return despacho

    def _buscar_pasarela(self, cadena):
        if isinstance(self.pasarelas, dict):
            return next((pasarela for nombre, pasarela in self.pasarelas.items()
                         if str(nombre).lower() == cadena.lower()), None)
        return next((pasarela for pasarela in self.pasarelas
                     if cadena.lower() in str(getattr(
                         pasarela, "cadena", type(pasarela).__name__)).lower()), None)