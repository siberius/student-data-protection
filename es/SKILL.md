---
name: proteccion-datos-alumnado
description: Diseña, implementa o audita la protección de datos del alumnado en aplicaciones educativas de España. Úsalo cuando cambien datos personales, identidad, permisos, conservación, exportaciones o flujos de IA, o para una revisión solicitada. No conviertas una edición estética ajena a estos riesgos en una auditoría completa.
metadata:
  version: "1.1"
  language: "es"
  jurisdiction: "ES/EU"
  license: "CC-BY-4.0"
  author: "Luděk Sušický"
  repo: "https://github.com/siberius/student-data-protection"
---

# Protección de datos del alumnado

Trabaja según el alcance solicitado y las evidencias disponibles. El skill apoya software educativo; no certifica conformidad ni autoriza cambios en producción. Esta edición se localiza para España y la UE. Identifica titularidad, comunidad autónoma y autoridad competente. Para otro país hay que revisar el marco; el idioma no determina la jurisdicción.

## Modo y límite afectado

Deduce diseño, implementación, auditoría o incidente de la solicitud. Una auditoría examina e informa sin modificar la aplicación. Analizar un incidente no autoriza apagar servicios, revocar cuentas o enviar avisos. En una implementación autorizada cambia el límite afectado y comprueba regresiones significativas. Una corrección pequeña no necesita repetir toda la auditoría. Señala un riesgo grave adyacente con pruebas y propuesta, sin ampliar el trabajo silenciosamente.

Reutiliza finalidades, flujos, centro/tenant, roles, alojamiento y condiciones conocidos. Pregunta solo por datos que cambien la decisión. Los datos sintéticos permiten desarrollar mientras falte la decisión de tratamiento real. Una actividad sin tratamiento personal no requiere cuentas o almacenamiento; revisa metadatos operativos antes de llamarla anónima.

Para una aplicación existente ofrece auditoría inicial enfocada y plan de corrección, o revisión más amplia previa al despliegue cuando proceda. Si ya se pidió auditoría o implementación, respeta ese alcance sin preguntar de nuevo ni ampliarlo silenciosamente. La sección 17.6 de la guía práctica detalla evidencias, prioridades y estado.

## Límites duraderos

- Minimiza por finalidad. Seudónimos, registros cifrados, resúmenes del razonamiento y embeddings pueden seguir siendo datos personales.
- Autentica según los datos y aplica permisos de objeto/tenant en el servidor u otro límite fiable. Nombre, código compartido, UUID e instrucciones del modelo no son autorización. Separa envíos no verificados y registros confirmados.
- Entradas, adjuntos, documentos recuperados y salidas del modelo no son fiables. Protege secretos y valida antes de escrituras autoritativas. No envíes registros, logs o claves reales a un chat ordinario de IA.
- Resuelve conjuntamente supresión, rectificación, copias derivadas, respaldo y recuperación. Un dispositivo compartido no debe revelar al usuario anterior. Identifica controles inciertos o fallidos.
- Distingue obligaciones jurídicas [Z], decisiones del perfil adoptado [P], recomendaciones [D] y puntos pendientes [O]. El perfil estricto detallado aplica cuando se adopta; evalúa salvaguardas existentes equivalentes antes de proponer sustituir la arquitectura. No inventes exenciones legales ni reduzcas protección necesaria.
- El responsable decide sobre tratamiento y despliegue. Consulta al DPD oportunamente para asesoramiento y supervisión independientes; no conviertas su aprobación en requisito jurídico universal ni le transfieras la responsabilidad del responsable.

Consulta [procedimiento](references/workflow.md) cuando necesites detalle de alcance, perfil y gobierno. Carga [marco jurídico](references/legal.md) para bases, derechos, transferencias y deberes españoles; [Reglamento de IA](references/ai-act.md) cuando proceda su uso o clasificación. Al verificar afirmaciones consulta [estado de fuentes](references/source-status.md). Comprueba fuentes actuales antes de decisiones jurídicas relevantes; una URL accesible no equivale a revisión jurídica.

## Carga solo el módulo pertinente

Cuando se pida una solución práctica, recomienda un modo de datos y desarrolla solo ese procedimiento. Los seis modos de datos difieren de los modos de trabajo anteriores. Carga la guía práctica solo para esta elección. Mantén breve el núcleo; considera skills separados cuando incidentes, auditoría o implementación requieran un flujo independiente con entradas y permisos distintos.

| Trabajo | Referencia |
|---|---|
| Elección práctica del modo de datos y ficha de solución | [Soluciones prácticas](references/practical-solutions.md) |
| Recogida, campos, archivos, importaciones y conectores | [Flujos](references/data.md) |
| Cuentas, códigos, roles, sesiones e integridad | [Identidad](references/identity.md) |
| Integración del proveedor OIDC/SAML | [SSO](references/sso.md) |
| Cifrado, claves y transporte | [Criptografía](references/crypto.md) |
| SQLite, CSV y exportaciones | [Almacenamiento](references/storage.md) |
| Caché web/PWA, dispositivos compartidos y navegador | [Web](references/web.md) |
| Conservación, auditoría, restauración e incidente | [Operaciones](references/operations.md) |
| Tutor con IA o RAG implementado/solicitado | [Datos de IA](references/ai-data.md) |
| Lista pertinente, aceptación y entrega | [Verificación](references/verification.md) |

No cargues todos los módulos automáticamente ni añadas tecnología para usar uno. El perfil es un diseño de referencia: explica diferencias y riesgos sin suponer que otra solución mantenida es defectuosa.

## Verificación y entrega

En implementación elige pruebas de la función cambiada y sus riesgos, en entornos autorizados con datos sintéticos. En auditoría entrega ubicación/evidencia, gravedad, efecto, recomendación y verificación necesaria; no declares superada una prueba propuesta. Distingue fallo observado, hipótesis, no comprobado y no aplicable con motivo. Separa incertidumbre jurídica y fallo técnico. Informa de propiedades concretas y decisiones pendientes, sin prometer seguridad total ni certificación RGPD.

## Integración y atribución

Adecuado para registros, portales, formularios y herramientas educativas con IA cuando la tarea afecta a datos personales. No requiere stack, proveedor, API, cuentas ni currículo concreto. Conserva este archivo, references/ y LICENSE juntos. Elige una edición pertinente; el entorno del skill nativo debe admitir sus archivos. La guía independiente sigue disponible. Este skill no autoriza instalación, servicios de pago, publicación, acceso a producción ni cambios fuera de la solicitud.

© 2026 Luděk Sušický. CC BY 4.0. Conserva atribución, licencia y avisos de cambios al redistribuir; las fuentes externas conservan sus derechos. La edición revisada 1.1 adapta la guía original de octubre de 2026 con modos delimitados, módulos, controles IA/SSO y gobierno del DPD; la localización española revisa sus referencias nacionales.
