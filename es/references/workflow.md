# 1. Interpretación de los requisitos y proceso del asistente

<!-- Referencia generada; edita la guía independiente mantenida. -->

Secciones de origen: 1.

## 1. Interpretación de los requisitos y proceso del asistente

- **[Z] Requisito jurídico:** se aplica cuando se cumplen las condiciones indicadas. La norma citada prevalece sobre el consejo técnico.
- **[P] Perfil de seguridad:** decisión concreta de implementación de este skill. DEBE y NO DEBE en las secciones técnicas definen este perfil, no un mandato literal del RGPD. Documenta cualquier desviación con la amenaza, el control compensatorio, una prueba y la decisión de la persona responsable del centro.
- **[D] Recomendación:** ampliación útil según el riesgo y el funcionamiento.
- **[O] Verificar:** cuestión dependiente del uso real, el derecho vigente o una configuración no confirmada. No la presentes como satisfecha.

1. Determina el modo solicitado: diseño, implementación, auditoría o incidente. Una auditoría produce hallazgos y recomendaciones sin modificar la aplicación. Revisar un incidente no autoriza desactivar servicios reales, revocar cuentas ni notificar a personas. Ejecuta estas acciones solo dentro de la autorización efectiva.
2. Reutiliza el contexto conocido e identifica la finalidad afectada, los flujos de datos, los papeles y el cambio de riesgo. Pregunta solo por información ausente que cambie la decisión. Para una corrección acotada, evalúa el límite afectado y las regresiones en lugar de reiniciar la evaluación completa. Señala un problema adyacente grave con evidencias; no amplíes silenciosamente la implementación.
3. Mapea solo los datos, destinatarios, identidad, permisos, conservación y amenazas pertinentes. Conserva una arquitectura segura existente y los controles que funcionan. Usa datos sintéticos mientras sigan sin resolverse la finalidad, la base jurídica o las decisiones de despliegue.
4. En diseño, propone controles y criterios de aceptación proporcionados. En implementación autorizada, aplica los controles seleccionados y registra sus ubicaciones en código o configuración. En auditoría, informa de gravedad, evidencia, impacto, acción propuesta y verificación necesaria. Separa las sospechas de los fallos observados.
5. Selecciona escenarios de aceptación según las funciones afectadas y el riesgo. Informa de superado, fallido, no realizado y no aplicable, con motivo; cada corrección no requiere un rediseño completo. No afirmes ejecución a partir de un plan de pruebas propuesto.
6. Antes del despliegue con datos reales, verifica la base jurídica aplicable, la evaluación necesaria y el texto normativo vigente. El responsable decide el despliegue con asesoramiento oportuno del DPD y revisión especializada adecuada. Si falta una base o evaluación exigida, no recomiendes el tratamiento afectado; continúa el trabajo autorizado no afectado.

No introduzcas datos reales del alumnado, registros de producción, claves ni bases de datos en un chat ordinario de IA o repositorio público. Genera datos sintéticos para depurar. Usar datos reales en un servicio de IA exige una evaluación separada de finalidad, necesidad, contrato, destinatarios, conservación y transferencias; desactivar el entrenamiento no basta.

### 1.1 Selección de controles por flujo de datos y riesgo

Las obligaciones jurídicas se aplican cuando se cumplen sus condiciones. Los resultados básicos son limitación de finalidad, minimización, límites de acceso fiables, integridad, capacidad de recuperación y gestión responsable de incidentes y derechos, proporcionados al tratamiento real. Una actividad sin tratamiento personal no necesita cuentas, base de datos, KMS ni auditoría personal solo porque esta guía los describa. Comprueba el alojamiento y los metadatos operativos antes de llamarla anónima.

Los ajustes [P] detallados forman un perfil de referencia estricto para sistemas nuevos con registros escolares persistentes o cuando el proyecto lo adopta expresamente. Los algoritmos, tiempos de espera y objetivos operativos concretos son decisiones del perfil. En un sistema existente, evalúa primero los controles reales y las protecciones equivalentes frente a amenazas pertinentes; una tecnología diferente y mantenida no es automáticamente una vulnerabilidad. No debilites la autorización ni inventes exenciones legales. Documenta una desviación material del perfil adoptado con amenaza, control compensatorio, verificación y decisión del responsable. Una revisión puede proponer esa decisión; no debe fabricar aprobación ni exigir una nueva para cada edición rutinaria dentro del alcance.

Elige la arquitectura antes de aplicar recetas específicas de implementación. Los detalles internos de bibliotecas criptográficas y la gestión de nonces corresponden al componente que cifra, no automáticamente a la aplicación si lo hace un servicio de almacenamiento verificado. Explica acceso a claves, protección de copias, exposición de metadatos y riesgo residual de la solución real. Cualquier cambio de alojamiento, proveedor de identidad, servicio de pago o destinatarios requiere la autorización correspondiente.

### 1.2 Responsable del tratamiento y DPD

El responsable responde de las finalidades, la licitud y las decisiones de despliegue. El DPD informa, asesora y supervisa con independencia y se consulta con suficiente antelación, incluida la evaluación de impacto relativa a la protección de datos (EIPD). Esta guía no atribuye al DPD una aprobación operativa general ni la responsabilidad del responsable del tratamiento. Registra el asesoramiento y la decisión responsable; resuelve los desacuerdos mediante la gobernanza adecuada. Véase [CEPD: DPD](https://www.edpb.europa.eu/sme/be-compliant/data-protection-officer_en).

© 2026 Luděk Sušický. [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Edición revisada de la versión 1.1, basada en la guía original de octubre de 2026. Conserva autor, licencia y avisos de cambios.
