# 10. Auditoría, conservación y recuperación [P/Z]

<!-- Referencia generada; edita la guía independiente mantenida. -->

Secciones de origen: 10, 11.

## 10. Auditoría, conservación y recuperación [P/Z]

### Auditoría [P]

Registra hora UTC, actor interno, centro, operación, objeto, resultado e identificador de correlación. Incluye inicio de sesión y fallo, retirada de permisos, verificación o reasignación de identidad, cambios de datos, lecturas de registros muy sensibles, exportaciones, supresión masiva, uso de acceso excepcional, rotación de claves y restauraciones. No escribas tokens, códigos, claves, contenido de formularios, mensajes ni nombres en registros operativos ordinarios. Mantén separado el historial protegido de cambios importantes.

Guarda la auditoría en un destino de solo adición del que la aplicación ordinaria no pueda borrar. Comprueba integridad y acceso, sincroniza la hora. Una cadena de hashes sin anclaje protegido independientemente no demuestra inmutabilidad. Un cambio crítico de datos, permisos o exportación debe tener registro duradero de auditoría o bandeja de salida transaccional antes de confirmar éxito; un fallo de auditoría no debe eludirse silenciosamente para realizar el cambio.

### Tabla de conservación

[Z] Conserva los datos solo el tiempo necesario para finalidad y obligaciones aplicables. El RGPD no fija un número universal de días para todas las aplicaciones escolares. [P] Los valores siguientes son una propuesta que el centro debe confirmar; prevalecen las obligaciones legales y el cuadro de clasificación y conservación documental aplicable.

| Categoría | Propuesta predeterminada |
|---|---|
| Código de entrada o secreto QR | Invalidar al caducar o cerrar entrada; no conservar secreto utilizable. |
| Secreto de sesión | Revocar inmediatamente al cerrar sesión o caducar; eliminar verificadores inactivos en 24 horas; la auditoría sin secretos puede conservarse más. |
| Participación temporal e identificador de dispositivo para actividad puntual | Eliminar en 24 horas tras terminar, salvo otra finalidad necesaria documentada. |
| Envíos en elaboración | Guardado automático solo cuando sea necesario; propuesta de 7 días desde última edición, con caducidad conocida por el usuario. |
| Formulario o inscripción puntual | Plazo según cumplimiento de finalidad y eventual revisión; fijar desencadenante y plazo concretos antes del lanzamiento. Sin conservación universal para todos los formularios. |
| Registros del alumnado, asistencia, evaluación y contactos | Plazos concretos por finalidad y cuadro documental aplicable; terminar la cuenta no elimina automáticamente registros obligatorios. |
| Mensajes, portafolios y adjuntos | Categorías separadas; confirmar necesidad tras terminar enseñanza o relación con el centro. Las copias derivadas no deben conservarse ilimitadamente. |
| Historial de correcciones y vínculos con personas | Definir según verificabilidad y revisión; no debe ser archivo ilimitado de todos los datos borrados. |
| Exportación temporal del servidor | Máximo 24 horas; volver a verificar siempre el derecho de descarga. |
| Auditoría ordinaria de seguridad | 90 días; un incidente puede justificar suspensión limitada del borrado. |
| Registros automáticos de IA de alto riesgo | Régimen separado conforme al artículo 26.6 aplicable; no aplicar 90 días ciegamente. |
| Copias de seguridad | Ventana móvil de 30 días, sin conservación interminable de instantáneas antiguas. |

Ejecuta limpieza automática diaria y supervisa errores. La supresión incluye índices, adjuntos, exportaciones, cachés y colas. En copias inmutables, hasta finalizar un plazo limitado puedes usar aislamiento del funcionamiento ordinario y reaplicación obligatoria de supresiones al restaurar; documenta el procedimiento y no ocultes las copias. Verifica anonimización también frente a identificación de clases pequeñas o combinaciones raras de datos.

Las copias están cifradas, separadas y al menos una protegida contra modificación por un atacante. Objetivos operativos predeterminados: RPO 24 horas, RTO 8 horas; para registros críticos, el centro los endurece según impacto de pérdida o caída. Restaura al menos trimestralmente en aislamiento, incluidas claves, relaciones, auditoría, supresiones e invalidación de sesiones históricas. Una copia satisfactoria no demuestra por sí sola capacidad de recuperación.

## 11. Incidentes [Z/P]

[Z] El encargado comunica una violación al responsable sin dilación indebida. El responsable notifica a la **autoridad de control competente** sin dilación indebida y, cuando sea posible, dentro de las 72 horas desde que tiene constancia, salvo que sea improbable el riesgo para derechos y libertades; justifica cualquier retraso. Para España, verifica si corresponde la AEPD o una autoridad autonómica competente en el caso concreto. Si es probable un riesgo alto, informa a las personas afectadas sin dilación indebida, evaluando las excepciones del artículo 34. También se documentan las violaciones no notificadas. Cifrar puede reducir riesgo, pero la filtración de clave, integridad o disponibilidad necesita valoración propia. [RGPD, artículos 33–34](https://eur-lex.europa.eu/eli/reg/2016/679/oj).

[P] Prepara contactos del responsable, DPD y servicio operativo. Objetivo interno: escalar a la persona responsable en 1 hora, primera evaluación en 24 horas; son objetivos organizativos, no plazos jurídicos. Procedimiento:

1. Registra hora de detección y alcance; conserva evidencias con seguridad, no distribuyas bases completas.
2. Limita daños: revoca sesiones e invitaciones, cierra el endpoint peligroso, aísla el servicio afectado; asegura funcionamiento alternativo del proceso afectado.
3. Determina datos, personas, destinatarios, disponibilidad de claves y posibles consecuencias; considera confidencialidad, integridad y disponibilidad.
4. Prepara la decisión sobre notificación y sus fundamentos. No esperes un informe forense completo; la notificación puede completarse gradualmente.
5. Corrige la causa, rota claves según necesidad, restaura y verifica datos. Documenta medidas posteriores y actualiza pruebas.

Evalúa por separado las obligaciones nacionales de ciberseguridad aplicables en España, cuya norma y ámbito deben verificarse, y las del Reglamento de IA si corresponden al operador o sistema; sus plazos no son automáticamente las 72 horas del RGPD. La ley checa de ciberseguridad no se presenta aquí como norma aplicable en España. Fundamento metodológico: [NIST SP 800-61 Rev. 3, versión final de abril de 2025](https://csrc.nist.gov/pubs/sp/800/61/r3/final).

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Edición revisada de la versión 1.1, basada en la guía original de octubre de 2026. Conserva autor, licencia y avisos de cambios.
