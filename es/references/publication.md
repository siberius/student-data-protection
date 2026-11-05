# 18. Publicación, documentos y salidas derivadas [D/O]

<!-- Referencia generada; edita la guía independiente mantenida. -->

Secciones de origen: 18.

## 18. Publicación, documentos y salidas derivadas [D/O]

### 18.1 Traza el límite real de publicación

Carga este módulo para portales, portfolios, muestras públicas, sitios generados, importación de documentos o exportaciones. Compara código, comandos de compilación y configuración de despliegue actuales con la documentación; una aplicación descrita como local puede publicar ya en un alojamiento. No ejecutes compilación ni despliegue solo para inspeccionar: pueden copiar registros reales, enviar datos o crear un artefacto público.

Traza la ruta pertinente desde fuentes y transformaciones hasta destinatarios: registros, adjuntos, OCR, notas de trabajo, HTML/JSON generado, índices de búsqueda, vistas previas, PDF, capturas, paquetes, cachés del alojamiento/CDN y versiones anteriores. Incluye logs de compilación y artefactos de CI si pueden contener datos personales. Un artefacto es una copia aunque no se despliegue una base de datos. Identifica público por salida: material privado de trabajo, acceso escolar autenticado o publicación abierta. El acceso docente a una fuente no autoriza por sí solo su publicación.

### 18.2 Construye una proyección pública explícita

Separa registros de trabajo y campos/archivos publicables. Construye configuración pública y exportaciones desde una lista de campos permitidos para público y finalidad definidos; excluir solo una contraseña puede exponer un futuro campo interno. Excluye campos desconocidos hasta evaluarlos. Mantén fuentes originales fuera del directorio público. Previsualiza la selección sin subir registros reales a un servicio externo de vistas previas.

Por elemento publicado conserva un registro interno mínimo: fuente/versión, campos seleccionados, público, decisión responsable, base de tratamiento u otra justificación aplicable y condición de revisión/retirada. Un botón de publicación o la aprobación del creador no demuestra resolver derechos de todas las personas ni condiciones jurídicas. No exijas nueva aprobación manual para cada cambio rutinario cubierto por una decisión vigente; revisa cambios materiales de contenido, público, finalidad o destinatarios. No exportes el registro de decisiones con fragmentos sensibles.

### 18.3 Revisa texto libre, medios e importaciones

Revisa comentarios, trabajos del alumnado, OCR, nombres de archivo, URL, metadatos de imágenes y contenido incrustado, además de campos estructurados. Un documento puede mencionar hermanos, representantes, compañeros o personal; determina qué datos de quién son necesarios. Suprime u oculta irreversiblemente en la copia distribuida y comprueba texto oculto, capas, OCR y adjuntos originales. Conserva un original restringido solo con justificación. Revisa también textos alternativos y pies de imagen.

Detectores de palabras, fechas aproximadas y clasificadores de IA ayudan a señalar revisiones; su silencio no demuestra seguridad y una alerta no es diagnóstico. No traslades una regla genealógica como «bastan nombre y año de nacimiento» a una política escolar general. Limita fragmentos sensibles en informes automáticos, tareas y logs.

Trata CSV, JSON, GEDCOM, documentos y archivos comprimidos importados como datos no fiables. Usa analizadores adecuados y valida esquema, tipos, límites de tamaño/cantidad, codificación y referencias entre registros. En archivos comprimidos limita expansión y rutas. Evita ejecutar un archivo Python/JavaScript recibido como importación de datos. El código de proyecto fiable tiene otro límite; no lo sustituyas sin evidencias. Separa previsualización, corrección y incorporación autorizada a registros oficiales. Complementa con [OWASP File Upload](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html).

### 18.4 Conserva procedencia sin etiquetar al alumnado

Cuando un valor importado o extraído por IA pueda afectar a una persona, registra fuente, versión/fecha pertinente, estado de verificación y responsabilidad de rectificación. Distingue declaración recibida, registro comprobado, transcripción, interpretación y conflicto pendiente. Una segunda fuente copiada puede tener el mismo origen y no ser corroboración independiente. Una sugerencia de IA o coincidencia plausible no debe fusionar personas silenciosamente ni convertirse en nota oficial, diagnóstico o etiqueta permanente de capacidad. El historial necesario de rectificaciones tiene permisos y conservación propios.

### 18.5 Comprueba acceso y destinatarios externos

Protege de forma coherente HTML, imágenes, originales, JSON y fragmentos del índice de búsqueda, incluidas URL directas, orígenes alternativos y vistas previas de despliegue si existen. Ocultar enlaces, usar noindex o buscar en el navegador no restringe acceso. Determina si alojamiento, mapas, fuentes, analítica y soporte reciben solicitudes o datos. Una petición de teselas externas puede revelar metadatos del visitante y áreas consultadas; inspecciona el comportamiento antes de afirmar envío de nombres o registros.

El hash de una respuesta compartida en una cookie sigue siendo una credencial compartida. No acredita identidad individual ni permite revocación individual. Ajusta autenticación, caducidad y revocación a los datos; usa el módulo de identidad para registros personales. Consulta [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html). Una actividad realmente pública sin datos personales no requiere cuentas automáticamente.

### 18.6 Revisa la versión y la retirada

Recomienda una comprobación de publicación proporcional al riesgo: compara el artefacto candidato real con la proyección permitida, inspecciona campos y archivos personales añadidos/modificados/eliminados e identifica contenido sensible o sin revisar. El verificador informa de cobertura y distingue advertencias de condiciones que impiden publicar adoptadas por el proyecto. Compilar correctamente no sustituye esta revisión. Permisos sin resolver o una exposición indebida conocida impiden esa publicación personal; el trabajo autorizado no afectado puede continuar.

Planifica retirada de HTML activo, carpetas públicas, índices, exportaciones y cachés. Un bucle que solo añade archivos puede conservar contenido retirado. Usa un manifiesto o compilación limpia de preparación; elimina solo archivos generados obsoletos confirmados, nunca fuentes ni archivos ajenos del usuario. Comprueba que restaurar o recompilar no vuelva a publicar lo retirado. URL anteriores, conservación del alojamiento y copias descargadas tienen límites explícitos; no prometas supresión remota sin evidencias. Revertir restaura una versión autorizada cuyas decisiones de publicación deben seguir vigentes.

Antes de actualizar plantilla/skill compara versiones y cambios locales, respalda archivos afectados y prepara recuperación. Conserva registros y controles de acceso del despliegue. Actualizar una plantilla no autoriza instalar, gastar ni publicar. Separa comportamiento observado tras actualizar y comprobaciones previstas.

### 18.7 Entrega y comentarios saneados

Añade a la ficha solo inventario pertinente de salidas, proyección permitida, estado de revisión, límites de retirada y siguiente acción responsable. El informe debe permitir corregir e identificar artefactos sin inspeccionar. Propón marcadores sintéticos distinguibles para comprobar filtración al índice o supresión; no incluyas datos reales del alumnado en evidencias de prueba.

Los comentarios reutilizables para quien mantiene el skill incluyen herramienta/versión, reproducción sintética, comportamiento esperado frente al observado y corrección general. Elimina identificadores, secretos e indicios indirectos; no adjuntes logs de producción, registros familiares, escaneos ni bases escolares. Muestra el contenido saneado antes de cualquier envío externo autorizado por separado. Los comentarios son opcionales y nunca se envían automáticamente.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Edición revisada de la versión 1.1, basada en la guía original de octubre de 2026; conserva atribución, licencia y avisos de cambios. Las fuentes externas conservan sus derechos.

## Licencia

MIT License

Copyright (c) 2026 Luděk Sušický

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Edición revisada de la versión 1.1, basada en la guía original de octubre de 2026. Conserva autor, licencia y avisos de cambios.
