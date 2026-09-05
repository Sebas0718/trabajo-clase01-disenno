# Bitácora de la práctica

Estudiante:
Carné:

> Cómo se llena cada entrada, en este orden y sin saltarse pasos:
>
> 1. **Predicción** — escríbala ANTES de correr nada. Qué cree que va a
>    pasar y por qué. Equivocarse aquí y entender después vale más que
>    acertar; no vuelva a corregirla.
> 2. **Observación** — corra el experimento de la etapa y pegue la salida.
> 3. **Explicación** — por qué pasó lo que pasó, en sus palabras, citando
>    **su** archivo y **su** línea (`servicio.py:24`).
> 4. **Sello** — corra `python herramientas/marcador.py` al cerrar la
>    etapa y pegue el sello que imprime.

## Etapa 0 — Diagnóstico

**Predicción:**
Antes de abrir legado.py, mi predicción es que se están violando unos 8 o 9 de los 11 principios. Siento que seguro todo lo de acoplamiento y cohesión está destruido porque todo está en un solo archivo, pero me imagino que al menos principios como el de "no reinventar la rueda" (usar librerías estándar) o el de portabilidad tal vez sí se salvan de pura casualidad. Vamos a ver

**Observación:**

```
```

**Explicación:**

**Sello:**

## Etapa 1 — Dividir y conquistar, cohesión

**Predicción:**

**Observación:**

```
```

**Explicación:**

**Sello:**

## Etapa 2 — Reducir el acoplamiento

**Predicción:**

Leyendo la clase ServicioRecetas, le cuento 6 responsabilidades distintas: valida la entrada, calcula el recargo, hace las peticiones HTTP, guarda en SQLite, genera el folio al azar y exporta a un archivo .txt.
Mi predicción es que voy a necesitar unos 7 archivos nuevos en total: 3 en la carpeta de dominio (como pide la guía: modelos, reglas y errores), tal vez 1 o 2 en aplicacion para coordinar, y al menos 2 en infraestructura (uno para la base de datos y otro para la red). Voy a ver si logro que el dominio quede completamente limpio de imports raros

**Observación:**

```
```

**Explicación:**

**Sello:**

## Etapa 3 — Abstracción y reuso

**Predicción:**
Antes de revisar el código, predije que cambiar CONFIG["vigencia_dias"] afectaría un solo lugar (donde se calcula la fecha de vencimiento). Sin embargo, al observar legado.py, noté que este cambio altera la fecha que se envía a todas las farmacias (líneas 69, 74, y 78 de legado.py). Esto demuestra el peligro del acoplamiento común: un cambio global afecta el comportamiento de múltiples líneas sin que ninguna función lo indique en sus parámetros
**Observación:**

```
```

**Explicación:**

**Sello:**

practica-principios-diseno main  ? ❯ python herramientas/marcador.py 2

  MARCADOR DE LA PRÁCTICA · Principios de diseño
  Sebastian Chaves Rojas   carné 2025121975
  ────────────────────────────────────────────────────────────
  Etapa 2  Acoplamiento                                 █████          verde
  ────────────────────────────────────────────────────────────
  5 pruebas en verde · 0 por resolver
  corrida #1 registrada
  SELLO: 430cd0f644b473c8
  Cópielo en la entrada de BITACORA.md de la etapa que acaba de cerrar.


## Etapa 4 — Flexibilidad, obsolescencia y portabilidad

**Predicción:**

**Observación:**

```
```

**Explicación:**

**Sello:**

## Etapa 5 — Testabilidad

**Predicción:**

**Observación:**

```
```

**Explicación:**

**Sello:**

## Etapa 6 — Diseño defensivo

**Predicción:**

**Observación:**

```
```

**Explicación:**

**Sello:**

## Cierre — Los principios en conflicto

Nombre dos principios que se estorbaron entre sí en SU rediseño, y con qué
criterio resolvió el conflicto. Cite el archivo donde se ve la decisión.

**Conflicto 1:**

**Conflicto 2:**
