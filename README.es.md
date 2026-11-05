# Protección de los datos del alumnado

Perfil práctico para diseñar, implementar o auditar aplicaciones escolares que tratan datos personales del alumnado, de sus representantes legales o del personal. Cubre el ciclo de vida de los datos, identidad y permisos, formularios y archivos, cifrado, sesiones, almacenamiento, conservación, recuperación e incidentes. Incluye orientación condicional para IA, RAG y SSO y 36 escenarios de aceptación.

**Versión 1.1, edición española para España de 5 de noviembre de 2026.** La comprobación original de fuentes de 22 de octubre de 2026 es histórica. Las revisiones específicas posteriores deben identificarse en el registro de fuentes; no equivalen a una auditoría jurídica completa nueva ni a pruebas ejecutadas de proveedores.

## Soluciones prácticas y tamaño del paquete

Empieza por el núcleo breve y carga solo la referencia pertinente. [Soluciones prácticas](es/references/practical-solutions.md) ofrece seis modos de datos: práctica puntual, recogida limitada, progreso guardado, registros oficiales, informes/exportaciones y tutor con IA. Incluye vías de implementación, contención frente a corrección duradera y ficha de solución. Desarrolla solo el procedimiento elegido. Son ejemplos de diseño, no evidencia de salvaguardas desplegadas.

La guía completa conserva su uso independiente; no la cargues junto con todas las referencias. Mantén un skill por ahora. Separa incidentes, auditoría o implementación solo cuando tengan entradas, permisos y entregables independientes; evita duplicar protecciones comunes.


## Elige un formato

- Paquete nativo: [es/SKILL.md](es/SKILL.md), acompañado de sus referencias. Conserva juntos los archivos y utiliza el mecanismo admitido por tu agente. Un archivo en disco no garantiza descubrimiento ni uso.
- Documento independiente: [docs/proteccion-datos-alumnado.md](docs/proteccion-datos-alumnado.md). Contiene el perfil completo en español para un agente que pueda recibir instrucciones Markdown directamente.

Utiliza un formato adecuado a tu entorno. No hace falta cargar ambas versiones a la vez. Leer esta guía no instala software, cambia el proyecto, crea cuentas ni autoriza enviar datos, utilizar servicios de pago o publicar contenido.

## Ámbito español

La sección jurídica se adapta a España y distingue RGPD, LOPDGDD, normativa educativa y competencia de la autoridad de control que corresponda. Antes de desplegar, concreta comunidad autónoma, titularidad, responsable, tratamiento y normas vigentes. No presupongas que toda competencia corresponde siempre a la AEPD. Esta edición no pretende resolver los marcos jurídicos de otros países hispanohablantes.

Los controles técnicos distinguen requisitos jurídicos [Z], decisiones del perfil [P], recomendaciones [D] y puntos pendientes de verificar [O]. Los algoritmos, plazos internos y valores operativos del perfil no deben presentarse como mandatos literales universales del RGPD. Aplica solo los módulos pertinentes al sistema real: una actividad sin datos personales no necesita cuentas, base de datos, KMS ni IA por utilizar este documento.

## Uso

Explica si necesitas diseño, implementación, auditoría o revisión de un incidente. Aporta finalidad, arquitectura y restricciones conocidas sin datos personales reales, secretos ni registros de producción. El agente debe reutilizar ese contexto, preguntar por carencias que cambien decisiones y usar datos sintéticos para comprobar comportamientos.

> Audita el formulario escolar existente y su exportación CSV. No modifiques la aplicación. Identifica límites de acceso, datos recogidos, conservación y riesgos de exportación. Distingue fallos observados, sospechas y configuración no verificada. Propón correcciones proporcionadas y pruebas con datos sintéticos.

Una auditoría entrega hallazgos y propuestas; no autoriza cambios de producción, revocaciones ni notificaciones. La implementación necesita el alcance autorizado. Ejecuta pruebas solo en un entorno permitido, marca las no realizadas y no conviertas un plan en una afirmación de ejecución. No se afirma que se hayan probado proveedores de IA, mecanismos de borrado externos o protocolos de identidad por el hecho de incluirlos en el perfil.

El responsable del tratamiento decide sobre el despliegue con evaluación adecuada y asesoramiento oportuno del DPD. El documento no es asesoramiento jurídico, certificación RGPD ni evaluación de conformidad de IA de alto riesgo. Mantén visibles las limitaciones y comprueba textos y condiciones actuales antes de decisiones jurídicas significativas.

## Autoría y licencia

Luděk Sušický

biolog, středoškolský a vysokoškolský učitel informatických předmětů

Autor original: **Luděk Sušický**. El contenido se distribuye bajo [Creative Commons Atribución 4.0 Internacional (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). Conserva atribución y aviso de licencia al compartir o adaptar. Esta es una edición traducida y adaptada al ámbito español; no cambia la licencia del contenido original. Las normas y publicaciones enlazadas conservan sus propios derechos.

[Registro de fuentes](docs/registro-fuentes.md) · [Evaluación del skill](docs/evaluacion-skill.md) · [English](README.md) · [Čeština](README.cs.md)
