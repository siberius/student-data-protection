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

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Edición revisada de la versión 1.1, basada en la guía original de octubre de 2026. Conserva autor, licencia y avisos de cambios.
