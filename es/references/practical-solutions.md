# 17. Guía de soluciones prácticas

<!-- Referencia generada; edita la guía independiente mantenida. -->

Secciones de origen: 17.

## 17. Guía de soluciones prácticas

### 17.1 Elige un modo de tratamiento

[D] Consulta este módulo cuando se solicite una solución práctica o un nivel de protección adecuado. Son patrones de diseño para situaciones escolares, no despliegues probados en centros ni niveles de conformidad jurídica. Complementan los modos de trabajo (diseño, implementación, auditoría, incidente); no autorizan su ejecución. Reutiliza el contexto conocido. Pregunta solo por carencias que cambien la elección: finalidad y campos necesarios, identidad verificada, persistencia o uso oficial, dispositivos compartidos y destinatarios, incluidos alojamiento, analítica e IA.

Recomienda un modo con motivo y, cuando sirva, una alternativa más sencilla. Combina modos por función: un ejercicio anónimo y un informe nominal del docente pueden tener límites distintos. No impongas el modo más complejo a toda aplicación. Usar datos reales sigue requiriendo la decisión de tratamiento y las salvaguardas aplicables.

| Modo y ejemplo escolar | Diseño mínimo | Comprobaciones antes del uso real |
|---|---|---|
| M1 Práctica puntual: fracciones | Sin nombre ni cuenta cuando no sean necesarios; respuestas en memoria de trabajo; borrado al terminar. Una actividad local/estática puede evitar el registro central. | Recarga, historial y siguiente usuario sin revelar respuestas; revisa solicitudes, logs, telemetría y almacenamiento del navegador antes de afirmar anonimato. |
| M2 Recogida limitada: inscripción en una actividad | Solo campos necesarios; recepción y acceso protegidos; evento de supresión según finalidad. Un envío no verificado queda pendiente. | Acceso a registros ajenos, campos modificables inesperados, límites de envío y supresión. Un código compartido no acredita identidad para registros oficiales. |
| M3 Continuidad del aprendizaje: progreso guardado | Progreso mínimo; identidad escolar verificada para el historial personal. Evalúa el acceso seudónimo según las consecuencias de su abuso. | Historial ajeno, cierre en dispositivo compartido, cambios de grupo y recuperación. Un seudónimo no es automáticamente anónimo. |
| M4 Registros oficiales: notas o asistencia | Identidad verificada, autorización fiable, escrituras controladas, concurrencia, historial de rectificaciones y almacenamiento recuperable; conservación según la gestión concreta. | Titular o nota falsificados, acceso revocado, ediciones simultáneas y restauración. No copies un plazo genérico de borrado de ejercicios. |
| M5 Informes docentes y exportaciones | Acceso por grupos asignados y finalidad; agregación cuando baste; campos mínimos y nueva comprobación de permisos al descargar. | Grupo ajeno, enlace caducado/revocado, fórmulas en CSV, nombres reveladores y ciclo de vida de copias descargadas. |
| M6 Tutor con IA | Considera primero explicaciones estáticas revisadas. Si hace falta IA, define destinatarios aprobados, entrada mínima, claves en servidor y salida validada. | Permisos de recuperación, datos realmente enviados, inyección, caída, conservación y supresión del proveedor. La salida del modelo por sí sola no escribe una nota oficial. |

Para permisos sobre objetos consulta [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html). La tabla y los ejemplos escolares son recomendaciones de esta guía; no afirman que OWASP haya evaluado esas aplicaciones.

### 17.2 Elige una vía de implementación

- **Actividad local/estática:** adecuada sin registro compartido. Comprueba persistencia local, recursos externos y metadatos del alojamiento; trabajar sin conexión no demuestra por sí solo ausencia de datos personales.
- **Plataforma escolar existente:** reutiliza identidad, permisos y almacenamiento mantenidos cuando sean adecuados. Verifica configuración real, destinatarios, exportaciones y comportamiento de supresión.
- **Aplicación propia con servidor:** usa componentes mantenidos de autenticación y sesiones, aplica permisos en servidor, valida entradas y asegura almacenamiento, recuperación y una persona responsable de operación. PHP con SQLite es una posibilidad; conserva una arquitectura equivalente con soporte.
- **Servicio opcional de IA:** delimita el flujo, limita recursos, controla fallos y aplica revisión humana según consecuencias. La actividad educativa debe conservar una alternativa utilizable.

Estima esfuerzo tras examinar entorno y dependencias. No prometas seguridad en minutos fijos ni crees otro sistema de contraseñas cuando exista SSO escolar adecuado.

### 17.3 Desarrolla solo el procedimiento elegido

En M1 traza red y almacenamiento, elimina recogida innecesaria, implementa cierre/reinicio y comprueba la experiencia del siguiente usuario. En M2 define campos permitidos, límites protegidos de envío/lectura y responsabilidad de supresión. En M3 establece identidad y titularidad del registro, después continuidad/cierre y revocación. En M4 define escrituras permitidas, rectificaciones y conflictos antes de persistencia y recuperación. En M5 prepara una consulta acotada, minimiza la exportación y autoriza la descarga. Carga módulos técnicos solo cuando proceda.

En M6 resuelve la identidad necesaria, aplica permisos antes de seleccionar fuentes y enviarlas al modelo, minimiza la solicitud, valida la respuesta y muéstrala o presenta una escritura autorizada por separado para revisión. Filtrar después de la llamada no deshace la comunicación al proveedor. Incluye índices, cachés y resúmenes en permisos y supresión. Ante caída o validación incierta conserva el trabajo y ofrece una alternativa clara sin escritura autoritativa silenciosa. Consulta la sección 15 y [OWASP RAG Security](https://cheatsheetseries.owasp.org/cheatsheets/RAG_Security_Cheat_Sheet.html).

### 17.4 Corrige una aplicación existente

Separa contención inmediata y corrección duradera. Propón la medida eficaz más acotada, como restringir una exportación pública o detener recogida innecesaria. Quitar una clave expuesta del cliente no basta: evalúa revocación y exposición mediante el proceso de incidentes autorizado. Indica usuarios afectados, verificación, exposición residual y siguiente acción. Conserva evidencias necesarias sin copiar logs sensibles a un chat.

La corrección duradera trata el límite demostrado de identidad, autorización, almacenamiento u operación y conserva componentes adecuados. Una migración de registros necesita comprobaciones de integridad, respaldo/recuperación y plan de reversión. Proponer contención no autoriza apagar producción, revocar credenciales ni enviar notificaciones. Deriva una posible comunicación indebida a evaluación del incidente conforme al marco español y la autoridad competente.

### 17.5 Entrega una ficha de solución

Mantén breve la respuesta inicial; desarrolla solo el modo elegido y sus controles pertinentes. Adapta esta ficha:

```text
Situación y objetivo:
Modo recomendado y motivo:
Datos necesarios y datos que evitar:
Flujo, destinatarios y almacenamiento:
Identidad y permisos:
Conservación, supresión y recuperación:
Pasos concretos de implementación:
Comprobaciones previas y estado real de ejecución:
Riesgos residuales y supuestos no verificados:
Persona responsable y siguiente decisión:
```

Distingue comprobaciones propuestas y ejecutadas, y justifica las no aplicables. Usa ejemplos sintéticos sin registros reales del alumnado. En España consulta el módulo jurídico español y concreta comunidad autónoma, titularidad y autoridad competente. El modo o el idioma no seleccionan automáticamente la jurisdicción.


### 17.6 Empieza con una aplicación existente

Si el usuario aporta una aplicación existente, ofrece una auditoría inicial proporcionada y un plan de corrección. Reutiliza código, arquitectura y hallazgos disponibles. Si ya pidió auditoría, procede dentro de ese alcance sin volver a pedir aprobación del mismo paso. Ante una implementación acotada, revisa el límite afectado como parte del trabajo; ofrece una auditoría más amplia por separado cuando las evidencias lo justifiquen.

Ofrece dos profundidades útiles: revisión de la función cambiada y su flujo de datos, o revisión más amplia previa al despliegue de identidad, permisos, destinatarios, conservación y recuperación. Recomienda según consecuencias reales, como primer uso de datos reales, registros oficiales, exportación pública, nuevo destinatario de IA o fallo grave observado. La falta de código o configuración limita conclusiones; solicita código/configuración sin datos sensibles o una demostración sintética, nunca una base de producción ni secretos. Una captura por sí sola no acredita seguridad del servidor.

Mapea comportamiento y evidencias actuales; entrega hallazgos priorizados con ubicación, datos/usuarios afectados, fallo observado frente a hipótesis, corrección propuesta, esfuerzo/dependencias y forma de verificación. Empieza por exposición o riesgos de integridad demostrados, después carencias pertinentes; separa mejoras opcionales. Reconoce controles que funcionan. Desarrolla la corrección elegida mediante la ficha y conserva la arquitectura adecuada.

Pedir auditoría autoriza evaluación, no cambios en la aplicación. Propón correcciones salvo que la implementación ya esté autorizada; ejecuta solo ese alcance. Distingue propuesta, implementado sin verificar, verificado con evidencias concretas y pendiente. Las comprobaciones intrusivas requieren un entorno autorizado; sin ejecución entrega un plan. La ausencia de hallazgos por sí sola no acredita seguridad para datos reales.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Edición revisada de la versión 1.1, basada en la guía original de octubre de 2026. Conserva autor, licencia y avisos de cambios.
