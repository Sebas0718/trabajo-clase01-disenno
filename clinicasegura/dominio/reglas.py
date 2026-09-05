# clinicasegura/dominio/reglas.py

def calcular_recargo(dias_restantes: int, tarifa_diaria: int, recargo_por_riesgo: bool) -> int:
    """Función pura: no lee variables globales, solo usa lo que recibe."""
    if recargo_por_riesgo:
        return tarifa_diaria * dias_restantes * 2
    return tarifa_diaria * dias_restantes