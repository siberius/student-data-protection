# 4. Modelo de datos, recogida y minimización [P]

<!-- Referencia generada; edita la guía independiente mantenida. -->

Secciones de origen: 4.

## 4. Modelo de datos, recogida y minimización [P]

### 4.1 Inventario de datos e identidad

- Para cada campo, determina finalidad, fuente, obligatoriedad u opcionalidad, base jurídica, destinatarios, sensibilidad, conservación y forma de supresión. Rechazar un campo opcional no debe bloquear un servicio básico no relacionado.
- Separa `school_id`, `user_id` de cuenta, `student_id` interno, `record_id`, un `submission_id` opcional y el token secreto de sesión. La cuenta y la persona a quien se refieren los datos no son lo mismo: docente o progenitor pueden actuar legítimamente por el estudiante. Un identificador aleatorio público no es un permiso.
- Un nombre introducido por el usuario es dato no confiable, no autenticación. No utilices nombre, fecha de nacimiento, clase o identificador de dispositivo como clave única para acceder al historial o modificar un perfil existente.
- Separa el vínculo de identidad de los registros de contenido cuando lo permita el funcionamiento. En envíos no verificados, mantén sin confirmar la vinculación con el estudiante; verifica y audita la asignación. No fusiones personas por compartir nombre.
- Permite recogida anónima o seudónima si la finalidad no necesita identidad. No llames anónimo a un formulario vinculable con una cuenta, identificador, hora u otro registro.
- No recojas IMEI, MAC, identificador publicitario ni huella digital del dispositivo. Si necesitas identificador de instalación, genéralo aleatoriamente y limita finalidad y conservación. No es autenticación ni anonimización. En dispositivos compartidos, prefiere un identificador limitado a la sesión.
- Registra fuente del registro, estado de verificación, autor del cambio, versión y categoría de conservación; establece `expires_at` cuando pueda determinarse el plazo. Nombres, contactos y contenido no deben aparecer en URL, nombres de archivo, métricas ni errores.

### 4.2 Formularios, adjuntos e integraciones

- En el servidor, admite solo campos y valores declarados. Rechaza campos desconocidos y protege los del sistema frente a asignación masiva. Define longitudes, tipos, rangos, codificación y tamaño del envío; no ejecutes HTML ni fórmulas.
- Un formulario público no debe ofrecer búsqueda de personas, lista de clase con nombres ni historial de envíos. Un envío no verificado no actualiza automáticamente registros escolares. Limita abuso automatizado y volumen; la protección frente a bots no debe introducir seguimiento no verificado de menores.
- En texto libre, advierte qué no debe introducirse y ofrece campos estructurados mínimos. Evalúa por separado fotografías, voz, ubicación, salud y orientación; no empieces a recogerlos «para el futuro».
- Admite adjuntos mediante lista permitida de tipos, verifica formato real, tamaño y contenido malicioso. Guárdalos fuera del directorio público web, con nombre aleatorio y sin ejecución; rechaza o aísla con seguridad contenido activo. Previsualizaciones, OCR, miniaturas y metadatos siguen permisos y conservación del original.
- Autoriza siempre la descarga de un adjunto según centro, persona, finalidad y papel. Un enlace firmado breve es un permiso transferible; limita duración y alcance. Compartirlo no debe convertir un documento en público.
- Una importación CSV o API incluye vista previa del mapeo, validación de duplicados y centro destino, confirmación atómica y auditoría. Un identificador externo es único dentro del sistema origen y centro. No sobrescribas registros por coincidencia de nombre.
- Las integraciones tienen identidad de servicio propia con alcance mínimo, rotación y revocación de secretos. Verifica webhooks por firma, ventana temporal y protección contra repetición. El perfil predeterminado envía notificaciones push y correo sin contenido sensible, solo un enlace a interfaz autenticada.

Fundamento de minimización y separación: [ENISA: Data Protection Engineering](https://www.enisa.europa.eu/sites/default/files/publications/ENISA%20Report%20-%20Data%20Protection%20Engineering.pdf). El esquema y las decisiones concretas son propuestas de este skill.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Edición revisada de la versión 1.1, basada en la guía original de octubre de 2026. Conserva autor, licencia y avisos de cambios.
