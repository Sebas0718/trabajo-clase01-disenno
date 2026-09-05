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

Las siete pruebas de etapa 5 pasan sin red ni base de datos. El servicio recibe
`pasarelas`, `reloj`, `folios` y `bitacora` en `clinicasegura/dominio/servicio.py:7`;
la fecha se calcula desde el reloj inyectado en `servicio.py:20` y las tres
pruebas propias cubren reloj fijo, cadena caída y receta inválida en
`mis_pruebas/test_propias.py:33`.

```
```

**Explicación:**

La predicción se confirmó: los dobles de `mis_pruebas/test_propias.py` permiten
controlar el reloj, el folio, la farmacia y la bitácora desde fuera del caso de
uso, y la salida `Despacho` más los eventos registrados hacen observable el
resultado. La prueba de cadena caída además verifica el error de dominio y su
contexto en `servicio.py:28`.

**Sello:**


  MARCADOR DE LA PRÁCTICA · Principios de diseño
  Sebastian Chaves Rojas   carné 2025121975
  ────────────────────────────────────────────────────────────
  Etapa 0  Diagnóstico                                  ████           verde
  ────────────────────────────────────────────────────────────
  4 pruebas en verde · 0 por resolver
  corrida #5 registrada
  SELLO: 09aa046b30cf7a7c
  Cópielo en la entrada de BITACORA.md de la etapa que acaba de cerrar.

## Etapa 1 — Dividir y conquistar, cohesión

**Predicción:**
Leyendo la clase ServicioRecetas, le cuento 6 responsabilidades distintas: valida la entrada, calcula el recargo, hace las peticiones HTTP, guarda en SQLite, genera el folio al azar y exporta a un archivo .txt.
Mi predicción es que voy a necesitar unos 7 archivos nuevos en total: 3 en la carpeta de dominio (como pide la guía: modelos, reglas y errores), tal vez 1 o 2 en aplicacion para coordinar, y al menos 2 en infraestructura (uno para la base de datos y otro para la red). Voy a ver si logro que el dominio quede completamente limpio de imports raros

**Observación:**

```
```

**Explicación:**

**Sello:**

3b303cc6d9dffdc4

  MARCADOR DE LA PRÁCTICA · Principios de diseño
  Sebastian Chaves Rojas   carné 2025121975
  ────────────────────────────────────────────────────────────
  Etapa 1  Dividir y conquistar · cohesión              ███████        verde
  ────────────────────────────────────────────────────────────
  7 pruebas en verde · 0 por resolver
  corrida #6 registrada
  SELLO: e77f1f6ee79f8130
  Cópielo en la entrada de BITACORA.md de la etapa que acaba de cerrar.

## Etapa 2 — Reducir el acoplamiento

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

## Etapa 3 — Abstracción y reuso

**Predicción:**
Al correr el comando grep, veo que las llaves exactas del JSON del proveedor (full_name, risk_lvl, etc.) aparecen incrustadas directamente en nuestro código. Esto viola la regla de Parnas sobre ocultar lo volátil. Mi predicción es que, al aplicar puertos y adaptadores, este número bajará a cero dentro de la carpeta dominio y aplicacion, y estas llaves solo van a existir encapsuladas en un adaptador dentro de la carpeta infraestructura

**Observación:**

```
```

**Explicación:**

**Sello:**

practica-principios-diseno main  ? ❯ python herramientas/marcador.py 3

  MARCADOR DE LA PRÁCTICA · Principios de diseño
  Sebastian Chaves Rojas   carné 2025121975
  ────────────────────────────────────────────────────────────
  Etapa 3  Abstracción y reuso                          ███████        verde
  ────────────────────────────────────────────────────────────
  7 pruebas en verde · 0 por resolver
  corrida #2 registrada
  SELLO: a3d2365c8cc8993c
  Cópielo en la entrada de BITACORA.md de la etapa que acaba de cerrar.

## Etapa 4 — Flexibilidad, obsolescencia y portabilidad

**Predicción:**


El experimento define una cuarta cadena llamada FarmaViva desde afuera del código principal. Mi predicción es que si mi diseño desacopló bien las pasarelas usando un registro dinámico, el sistema procesará la receta con éxito sin necesidad de que toque ni una sola línea del servicio central. Si por el contrario hubiera dejado un condicional (if/elif) rígido, la prueba fallará al intentar buscar a FarmaViva


**Observación:**

```
```

**Explicación:**

**Sello:**

  MARCADOR DE LA PRÁCTICA · Principios de diseño
  Sebastian Chaves Rojas   carné 2025121975
  ────────────────────────────────────────────────────────────
  Etapa 4  Flexibilidad · obsolescencia · portabilidad  ███████        verde
  ────────────────────────────────────────────────────────────
  7 pruebas en verde · 0 por resolver
  corrida #8 registrada
  SELLO: 5c770a55f08e1cb9
  Cópielo en la entrada de BITACORA.md de la etapa que acaba de cerrar.

## Etapa 5 — Testabilidad

**Predicción:**
Intentar emitir una receta con el código legado requiere que la base de datos SQLite esté accesible, que haya conexión de red real para llamar a las APIs de las farmacias, y que el reloj y los números aleatorios corran en tiempo real sin control externo. Mi predicción es que al aislar el servicio e inyectar un reloj fijo, un generador de folios y adaptadores simulados, podré correr pruebas automatizadas instantáneas sin tocar red ni base de datos real

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
