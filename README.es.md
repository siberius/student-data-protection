# Protección de los datos del alumnado

[![Skills.sh](https://img.shields.io/badge/skills.sh-Install-blue)](https://skills.sh/siberius/student-data-protection)

## Instalación y uso rápido

Instala la edición que utilices en tu asistente de código (Claude Code, Cursor, Codex, Antigravity, OpenCode, Cline y otros) mediante la CLI de [skills.sh](https://skills.sh):

```bash
# Instalación de la edición en español (España / UE)
npx skills add siberius/student-data-protection --skill proteccion-datos-alumnado --full-depth -g -a codex

# O listar todas las 7 ediciones disponibles
npx skills add siberius/student-data-protection --full-depth --list
```

Para probar el skill de forma temporal:

```bash
npx skills use siberius/student-data-protection --skill proteccion-datos-alumnado --full-depth --agent codex
```

Perfil práctico para diseñar, implementar o auditar aplicaciones escolares que tratan datos personales del alumnado, de sus representantes legales o del personal. Cubre el ciclo de vida de los datos, identidad y permisos, formularios y archivos, cifrado, sesiones, almacenamiento, conservación, recuperación e incidentes. Incluye orientación condicional para IA, RAG, SSO, k-anonimidad y 38 escenarios de aceptación.

**Versión 1.2, edición española para España de 14 de noviembre de 2026.** La comprobación original de fuentes de 22 de octubre de 2026 es histórica. Las revisiones específicas posteriores deben identificarse en el registro de fuentes; no equivalen a una auditoría jurídica completa nueva ni a pruebas ejecutadas de proveedores.

Antes del trabajo sustantivo el skill establece el contexto y pregunta por información decisiva pendiente. Reutiliza hechos y permisos aportados; las preguntas decisivas sin respuesta detienen solo el trabajo dependiente. La [entrada del procedimiento](es/references/workflow.md) cubre alcance, datos, público, destinatarios, ciclo de vida y entorno pertinentes.

[Publicación y salidas derivadas](es/references/publication.md) trata campos públicos permitidos, documentos/medios, procedencia, artefactos compilados reales, índices, acceso, retirada y actualizaciones seguras. Se carga solo para tareas pertinentes. Los comentarios técnicos usan ejemplos sintéticos saneados y nunca se envían automáticamente.

## Soluciones prácticas y tamaño del paquete

Empieza por el núcleo breve y carga solo la referencia pertinente. [Soluciones prácticas](es/references/practical-solutions.md) ofrece seis modos de datos: práctica puntual, recogida limitada, progreso guardado, registros oficiales, informes/exportaciones y tutor con IA. Incluye vías de implementación, contención frente a corrección duradera y ficha de solución. Desarrolla solo el procedimiento elegido. Son ejemplos de diseño, no evidencia de salvaguardas desplegadas.

La guía completa conserva su uso independiente; no la cargues junto con todas las referencias. Mantén un skill por ahora. Separa incidentes, auditoría o implementación solo cuando tengan entradas, permisos y entregables independientes; evita duplicar protecciones comunes.

## Elige un formato

- Paquete nativo: [es/SKILL.md](es/SKILL.md), acompañado de sus referencias. Conserva juntos los archivos y utiliza el mecanismo admitido por tu agente. Un archivo en disco no garantiza descubrimiento ni uso.
- Documento independiente: [docs/proteccion-datos-alumnado.md](docs/proteccion-datos-alumnado.md). Contiene el perfil completo en español para un agente que pueda recibir instrucciones Markdown directamente.

## Ediciones disponibles y skills nativos

| Idioma / Jurisdicción | Skill nativo | Guía independiente | Registro de fuentes | Readme |
|---|---|---|---|---|
| **Español (España / UE)** | [es/SKILL.md](es/SKILL.md) | [docs/proteccion-datos-alumnado.md](docs/proteccion-datos-alumnado.md) | [docs/registro-fuentes.md](docs/registro-fuentes.md) | [README.es.md](README.es.md) |
| **Čeština (Chequia / UE)** | [cs/SKILL.md](cs/SKILL.md) | [docs/ochrana-dat-zaku.md](docs/ochrana-dat-zaku.md) | [docs/registr-zdroju.md](docs/registr-zdroju.md) | [README.cs.md](README.cs.md) |
| **English (UE / Contexto checo)** | [SKILL.md](SKILL.md) | [docs/student-data-protection.md](docs/student-data-protection.md) | [docs/source-register.md](docs/source-register.md) | [README.md](README.md) |
| **Polski (Polonia / UE)** | [pl/SKILL.md](pl/SKILL.md) | [docs/ochrana-danych-uczniow.md](docs/ochrana-danych-uczniow.md) | [docs/rejestr-zrodel.md](docs/rejestr-zrodel.md) | [README.pl.md](README.pl.md) |
| **Українська (Ucrania / UE)** | [uk/SKILL.md](uk/SKILL.md) | [docs/zakhyst-danykh-uchniv.md](docs/zakhyst-danykh-uchniv.md) | [docs/reiestr-dzherel.md](docs/reiestr-dzherel.md) | [README.uk.md](README.uk.md) |
| **Deutsch (Alemania / UE)** | [de/SKILL.md](de/SKILL.md) | [docs/schuelerdatenschutz.md](docs/schuelerdatenschutz.md) | [docs/quellenregister.md](docs/quellenregister.md) | [README.de.md](README.de.md) |
| **Français (Francia / UE)** | [fr/SKILL.md](fr/SKILL.md) | [docs/protection-donnees-eleves.md](docs/protection-donnees-eleves.md) | [docs/registre-sources.md](docs/registre-sources.md) | [README.fr.md](README.fr.md) |

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

Autor original: **Luděk Sušický**. El contenido se distribuye bajo [MIT](https://opensource.org/license/mit). Conserva atribución y aviso de licencia al compartir o adaptar. Esta es una edición traducida y adaptada al ámbito español; no cambia la licencia del contenido original. Las normas y publicaciones enlazadas conservan sus propios derechos.

[Registro de fuentes](docs/registro-fuentes.md) · [Evaluación del skill](docs/evaluacion-skill.md) · [English](README.md) · [Čeština](README.cs.md)
