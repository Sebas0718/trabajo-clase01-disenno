# Diagnóstico del código de partida

Lea `clinicasegura/legado.py` entero antes de escribir una sola línea de
código nuevo. Llene una fila por principio. En la columna de evidencia
cite **archivo y línea** (por ejemplo `legado.py:38`); una fila sin
evidencia no cuenta.

Si cree que un principio **no** está violado, escriba la fila igual y
explique por qué en la columna de hallazgo.

¡Excelente! Ahora que tengo tu código real, los números de línea y los detalles exactos van a calzar a la perfección.

Aquí tienes los textos listos para copiar y pegar, redactados con un tono natural y cumpliendo con la regla de hacer suposiciones (una buena y una un poco "ingenua" para que se note el proceso de aprendizaje).

**Para tu archivo `BITACORA.md` (Etapa 0)**
Copia y pega esto antes de hacer cualquier cambio:

> **Etapa 0 - Predicción:**
> Después de darle una leída rápida a `legado.py`, mi predicción es que sí se están violando los 11 principios completos. El acoplamiento y la cohesión saltan a la vista porque hay una variable global `CONFIG` y una clase que hace literalmente todo. Mi suposición "buena" es que arreglar lo de las farmacias (`if/elif`) me va a tomar un buen rato. Mi suposición "ingenua" (que seguro me va a dar problemas) es que la testabilidad tal vez no esté *tan* mal porque vi que la base de datos usa la carpeta `/tmp/`, lo cual me sonó amigable para pruebas, pero seguro el marcador me va a demostrar lo contrario por la forma en que se conecta.

---

**Para tu archivo `DIAGNOSTICO.md` (Etapa 0)**
Aquí tienes la tabla exacta con los números de línea sacados de tu código.

| Principio | Hallazgo concreto | Evidencia | Qué cuesta si no se corrige |
| --- | --- | --- | --- |
| **1. Dividir y conquistar** | La clase `ServicioRecetas` valida datos, calcula recargos, hace peticiones HTTP y escribe en base de datos. | legado.py:37 | Todo el sistema es un bloque gigante, lo que hace difícil encontrar y aislar errores. |
| **2. Alta cohesión** | El servicio hace cosas que no tienen relación directa, mezclando reglas de negocio con infraestructura. | legado.py:41 | Cambiar algo técnico (como la base de datos) puede romper las reglas médicas por accidente. |
| **3. Bajo acoplamiento** | `CONFIG` es un diccionario global mutable. Cualquier parte del código puede alterarlo. | legado.py:24 | Si una función cambia un valor sin avisar, el comportamiento de todo el sistema se vuelve impredecible. |
| **4. Ocultar lo volátil (Abstracción)** | El método `reporte` conoce la estructura exacta del JSON del proveedor (`["data"]["attributes"]...`). | legado.py:130 | Si el proveedor externo cambia el nombre de sus llaves, nuestro sistema se rompe. |
| **5. Firma estrecha** | El método `reporte` recibe el objeto `paciente` entero, aunque solo utiliza dos datos específicos. | legado.py:127 | Hace que la función sea imposible de reusar si no tienes un objeto idéntico armado. |
| **6. No reinventar la rueda** | La validación de la cédula separa los guiones y revisa los números a mano iterando caracteres. | legado.py:135 | Es frágil. La librería estándar (como expresiones regulares) lo hace más seguro y con menos código. |
| **7. Variación encapsulada** | Hay condicionales rígidos (`if/elif`) para determinar a cuál URL de farmacia enviar la receta. | legado.py:70 | Para agregar una nueva farmacia hay que modificar el método central de emisión. |
| **8. Obsolescencia** | La lógica de negocio construye sus propias conexiones con dependencias concretas (`sqlite3`, `urllib`). | legado.py:43 | Reemplazar la base de datos o la librería de red a futuro va a requerir reescribir la lógica principal. |
| **9. Portabilidad** | El método `exportar` asume una ruta estática exclusiva de Windows (`C:\\ClinicaSegura...`). | legado.py:148 | El sistema fallará instantáneamente si se ejecuta en un servidor Linux o Mac. |
| **10. Testabilidad** | Dependencias de tiempo (`datetime.now()`) y azar (`random.randint`) quemadas dentro de la lógica. | legado.py:57 | Es imposible escribir pruebas automatizadas predecibles porque el resultado siempre cambia. |
| **11. Diseño defensivo** | Usa `assert` para validar la entrada (que se ignora en producción) y atrapa errores ocultándolos (`except Exception: pass`). | legado.py:53 | Datos inválidos se procesan sin detenerse, y los fallos críticos viajan en total silencio. |