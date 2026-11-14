# 15. Flujos de datos de IA, tutoría y RAG [P/O]

<!-- Referencia generada; edita la guía independiente mantenida. -->

Secciones de origen: 15.

## 15. Flujos de datos de IA, tutoría y RAG [P/O]

Aplica solo a una función de IA implementada o pedida explícitamente. No añadas modelo, base vectorial ni registro de conversaciones para usar esta sección. Un asistente de desarrollo y un servicio para alumnado tienen flujos diferentes y necesitan entradas de inventario separadas.

### 15.1 Minimiza y delimita el flujo

Registra para cada flujo finalidad, papeles de responsable y encargado, fuentes aprobadas, categorías de datos, acceso de usuarios, destinatarios, región y soporte remoto, conservación contractual, supresión y transferencias necesarias. Incluye prompts, respuestas, adjuntos, conversaciones, puntos de control, trazas de moderación y soporte, cachés, representaciones vectoriales, índices vectoriales, registros del proveedor y salidas de herramientas o conectores. Los datos derivados pueden seguir siendo personales sin nombres; las representaciones vectoriales no garantizan anonimización.

Antes de llamar al servicio, selecciona solo campos necesarios para tarea actual y destinatario autorizado. Retira identificadores irrelevantes y secretos. No supongas que el docente puede subir el registro de toda la clase. Verifica ajustes y condiciones del proveedor para cuenta y endpoint reales; «entrenamiento desactivado», etiqueta educativa o región UE por sí solos no resuelven conservación, acceso de soporte ni transferencias. Condiciones o configuración no disponibles siguen sin verificar; puede continuar el desarrollo con datos sintéticos.

Mantén claves del servicio en servidor. Impón permisos de destino, herramientas y alcance de datos fuera del prompt. Entradas del estudiante, documentos recuperados y salidas generadas no son confiables. No permitas que documento o respuesta cambien papeles, llamen URL arbitrarias o envíen registros a destinatario nuevo. Si las herramientas obtienen recursos, restringe destinos y prueba vías de falsificación de solicitudes y exfiltración. Valida salidas estructuradas antes de cambiar registros y codifica con seguridad el texto mostrado.

### 15.2 Aplica acceso durante toda la recuperación

Asocia documentos, fragmentos, representaciones vectoriales y resúmenes derivados con ID de fuente, centro, permisos de persona o grupo aplicables, versión de contenido y categoría de conservación. Autoriza antes de recuperar y antes de divulgar resultados; una puntuación de similitud no es permiso. Los índices compartidos necesitan aislamiento efectivo entre organizaciones. Filtra búsquedas, recuentos, citas, previsualizaciones, exportaciones y reutilización de conversaciones, no solo la respuesta visible final. Retirar permisos o borrar invalida cachés de recuperación y copias derivadas dentro de ventana definida; si no se confirma aún la invalidación, bloquea resultados afectados en lugar de servir permisos que sabes obsoletos.

Conserva procedencia y distingue cita, interpretación del modelo y afirmación sin respaldo. Prueba recuperación entre centros con texto sintético distintivo y cambio de papel tras indexación. Una cita fabricada no demuestra corrección. Delimita contenido recuperado y valida acciones; «ignora instrucciones maliciosas» no es un control de aislamiento adecuado.

### 15.3 Registros de tutoría y supresión

Para aprendizaje reanudable, guarda solo objetivo, referencias necesarias a tareas, respuesta o razonamiento expresados, condiciones de ayuda, revisiones observadas y siguiente paso necesarios para la finalidad. No deduzcas ni archives diagnósticos, personalidad o procesos privados de pensamiento. Un resumen del razonamiento puede ser dato personal. Dale los mismos permisos, transparencia y conservación por finalidad que la actividad subyacente; en dispositivos compartidos, facilita una vía clara de terminar y borrar.

Mapea supresión y corrección en fuentes originales, fragmentos, índices vectoriales, resúmenes, puntos de control exportados, colas, copias y ejemplares del proveedor. Registra qué puede borrarse directamente, qué exige petición al proveedor y qué permanece bajo conservación limitada justificada. Suspende recuperación cuando borrar fuente o cambiar permisos invalide resultados. Impide reindexación desde cola o copia obsoletas tras supresión. No prometas eliminación inmediata en copias inmutables o terceros sin evidencia. Prueba el procedimiento real del proveedor con datos sintéticos cuando esté disponible; no supongas que una petición API borró todas las copias.

Si el modelo no está disponible o no se valida su salida, conserva trabajo y marca retroalimentación pendiente. No conviertas un tiempo agotado en todos los puntos, inventes evaluación ni cambies silenciosamente de proveedor. La evaluación con consecuencias sigue sujeta a revisión humana adecuada con responsabilidad definida.

Orientación técnica: [OWASP RAG Security](https://cheatsheetseries.owasp.org/cheatsheets/RAG_Security_Cheat_Sheet.html). Son controles de implementación, no sustituyen la clasificación jurídica y evaluación del proveedor separadas.

### 15.4 Salvaguardas arquitectónicas para modelos de IA locales y no locales y k-anonimidad [P/Z]

Cuando el creador proponga integrar un modelo de IA, distingue primero si el modelo se ejecuta **localmente en el perímetro del responsable (L0)** o si es un **modelo no local (en la nube / externo) (C1/C2)**. Con modelos no locales, alerta proactivamente de que debe establecerse una capa de transformación intermedia en la aplicación antes de transmitir datos fuera del centro escolar:

| Modo arquitectónico de IA | Características del flujo | Salvaguardas obligatorias de preparación de datos [P] |
|---|---|---|
| **L0: IA local / en navegador** (modelo local en servidor escolar o navegador sin telemetría externa) | Los datos no salen del dispositivo ni del servidor del centro; sin destinatarios externos. | No requiere k-anonimidad externa ni contrato del art. 28 RGPD. Aplica permisos locales (sección 6) y limpia memoria/caché en equipos compartidos al cerrar sesión (sección 9). |
| **C1: IA no local - Interacción individual (1:1)** (retroalimentación a la tarea de un alumno) | La consulta atañe a un único alumno; la k-anonimidad matemática no puede aplicarse a una petición aislada. | Crea una **pasarela de seudonimización local** (EDPB 01/2025): 1. Elimina identificadores directos (`nombre`, `correo`, `student_id`, `aula`). 2. Conserva la tabla de correspondencia (`lookup table`) exclusivamente en la base de datos local del centro. 3. Desinfecta el texto libre de PII (nombres, contactos, denominación del centro). 4. Utiliza llamadas sin estado con retención cero verificada con el proveedor. |
| **C2: IA no local - Analítica de aula / grupo y exportaciones (1:N)** (análisis de tendencias, predicción de abandono, RAG grupal) | Se envían registros de múltiples alumnos. En un aula pequeña la seudonimización simple (`Alumno_01`) fracasa. | Crea una **canalización de agregación o k-anonimidad** (EDPB 02/2026, AEPD): 1. Prioriza el envío de **resúmenes agregados** (medias, distribución de errores sin microdatos individuales). 2. Si se requieren registros individuales, impone **k-anonimidad (`k >= 5` personas distintas)** y **l-diversidad (`l >= 2` valores sensibles distintos)** por clase de equivalencia. |

#### Reglas para la canalización de k-anonimidad en IA no local y exportaciones (Modos C2 y M5)

1. **Clasificación de atributos antes de transformar:** Los identificadores directos (`nombre`, `DNI/NIE`, `correo`, `teléfono`, `student_id`, `device_id`, `voz`, `foto`) se eliminan obligatoriamente (no utilices hash simple, que sigue siendo dato personal y permite correlación). Para cuasi-identificadores (`aula`, `fecha de nacimiento / edad`, `género`, `NEE/ACNEAE`, `municipio / CP`, `marca temporal`), aplica **generalización** (p. ej., `3º ESO B` -> `ESO`; `14 años` -> `13-16 años`; `hora exacta` -> `semana/mes`). Para atributos sensibles u objetivo (`calificación`, `tipo de error`, `evaluación cualitativa`, `informe psicopedagógico`), verifica la diversidad del grupo.
2. **Contra el aislamiento de registros (No Record Isolation -> k-anonimidad):** Agrupa los registros según todos los cuasi-identificadores. Cada grupo (clase de equivalencia) DEBE incluir registros de al menos **5 personas físicas distintas (`k >= 5` calculado mediante `COUNT(DISTINCT student_id)`)**. Si un alumno tiene varias filas (serie temporal de intentos), 5 filas del mismo alumno NO constituyen `k = 5`. Los grupos con `k < 5` deben generalizarse más o suprimirse permanentemente (**supresión de registros / record suppression**).
3. **Contra la correlación de registros (No Linkage):** Mezcla aleatoriamente el orden de las filas (**permutación / shuffling**) antes de exportar para impedir la identificación por orden alfabético o de registro. En tablas resumen con totales de fila y columna, aplica **supresión complementaria** (PTAC) para que una celda con `k < 5` no pueda deducirse por resta de totales.
4. **Contra la inferencia (No Inference -> l-diversidad):** Si todos los alumnos de una clase de equivalencia comparten el mismo valor sensible (`l = 1`, p. ej., todos obtienen calificación insuficiente o comparten la misma adaptación curricular), se revela el dato sensible mediante ataque por homogeneidad. Exige al menos **`l >= 2` valores distintos** del atributo objetivo en cada grupo, o fusiona la clase con una categoría superior.
5. **Límite jurídico (Perspectiva del encargado según EDPB 02/2026 y Dictamen 28/2024):** [Z] Si el proveedor de IA no local trata datos por cuenta del centro (encargado según art. 28 RGPD) y el centro conserva los datos identificados originales, la naturaleza de los datos se valora desde la perspectiva del responsable. La k-anonimidad técnica no exime de suscribir el contrato de encargo ni de comprobar la edad de consentimiento (en España, art. 7 LOPDGDD fija 14 años; condiciones de OpenAI y Google exigen a partir de 13 años con consentimiento de tutores). La k-anonimidad actúa como salvaguarda técnica esencial para mitigar el impacto (arts. 25 y 32 RGPD).

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Edición revisada de la versión 1.2, basada en la guía original de octubre de 2026. Conserva autor, licencia y avisos de cambios.
