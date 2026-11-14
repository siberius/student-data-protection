# 2. RGPD y marco español

<!-- Referencia generada; edita la guía independiente mantenida. -->

Secciones de origen: 2.

## 2. RGPD y marco español

### 2.1 Datos personales y categorías especiales

[Z] Un nombre vinculado a asistencia, contacto, mensajes, resultados o calificaciones es un dato personal. Identificadores aleatorios, hashes y registros cifrados pueden seguir siendo personales si permiten reidentificar. Seudonimizar no equivale a anonimizar. Una calificación no es automáticamente una categoría especial del artículo 9; salud y ciertos datos biométricos pueden serlo. Evita su recogida por defecto. Cuando sea necesaria, documenta tanto una base del artículo 6 como la condición aplicable del artículo 9.2 y limita accesos. Véase el [RGPD](https://eur-lex.europa.eu/eli/reg/2016/679/oj).

### 2.2 Decisiones del responsable y del proveedor

| Área | Requisito o decisión y evidencia |
| --- | --- |
| Finalidad y base | [Z] Determina por finalidad la base del artículo 6, datos necesarios y conservación. La AEPD explica el encaje de la enseñanza reglada en la función educativa y la disposición adicional 23 de la LOE; esto no autoriza cualquier telemetría ni uso comercial secundario. |
| Consentimiento | [Z] No exijas consentimiento familiar para todo tratamiento educativo. Si la base es consentimiento, aplica el artículo 7 de la LOPDGDD, incluidos los supuestos de menores de 14 años y sus excepciones legales. Esa regla no es una edad universal de acceso a cualquier aplicación ni justifica todo tratamiento escolar. |
| Responsabilidad | [Z/O] Identifica al responsable real: centro o Administración educativa según titularidad y tratamiento. Un proveedor que trata por instrucciones puede ser encargado; la entrega de software sin acceso a datos no basta para asignarle ese rol. |
| Contratos | [Z] Cuando exista encargado, aplica el artículo 28: instrucciones, confidencialidad, medidas, subencargados, asistencia, devolución/supresión y comprobación. Incluye soporte, analítica y servicios de IA. |
| Registros y DPD | [Z] Mantén registros conforme al artículo 30. El artículo 34.1.b de la LOPDGDD incluye centros docentes de los niveles previstos legalmente y universidades públicas y privadas en la obligación de designar DPD. Su asesoramiento no sustituye la decisión ni responsabilidad del responsable. |
| Riesgo | [Z] Aplica privacidad por diseño y defecto y seguridad según riesgo (artículos 25 y 32). Determina si procede EIPD (artículo 35); no presupongas exención por ser un centro educativo. Con riesgo residual alto, considera consulta previa del artículo 36. |

Fuentes locales: [LOPDGDD, Ley Orgánica 3/2018](https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673), [LOE, Ley Orgánica 2/2006](https://www.boe.es/buscar/act.php?id=BOE-A-2006-7899), [AEPD: DPD en centros docentes](https://www.aepd.es/preguntas-frecuentes/10-menores-y-educacion/FAQ-1007-estan-obligados-los-centros-docentes-a-designar-un-dpd), [AEPD: docencia y exámenes en línea](https://www.aepd.es/preguntas-frecuentes/10-menores-y-educacion/FAQ-1009-pueden-los-centros-educativos-impartir-clases-y-realizar-examenes-online-sin-el-consentimiento-de-los-interesados).

[O] Antes del despliegue identifica comunidad autónoma, titularidad, responsable y autoridad de control competente; no asumas que todas las actuaciones corresponden siempre a la AEPD. Verifica la normativa educativa y las reglas de archivo/conservación aplicables al tipo de centro y expediente. La edición española no importa la ley escolar checa, su umbral de consentimiento ni ÚOOÚ como autoridad local. Tampoco pretende cubrir otros países hispanohablantes.

### 2.3 Información, derechos y transferencias

[Z] Prepara información comprensible de los artículos 12–14: responsable y DPD, fines, bases, destinatarios, transferencias, conservación, derechos, reclamación y decisiones automatizadas relevantes. Asegura acceso, rectificación, limitación y demás derechos aplicables; la supresión no es absoluta y la portabilidad no cubre automáticamente todo expediente escolar. Verifica la identidad proporcionalmente sin recopilar copias de documentos de forma indiscriminada. El plazo general de respuesta es un mes; una ampliación exige sus condiciones y comunicación. Evalúa el artículo 22 para decisiones exclusivamente automatizadas de efecto jurídico o similar, incluso sin IA; un clic docente formal no demuestra revisión humana significativa.

[Z] El RGPD no exige por sí solo alojamiento exclusivamente español o europeo. Evalúa transferencias fuera del EEE, incluido soporte remoto y subencargados. [P] El perfil estricto utiliza alojamiento y copias en el EEE; una alternativa requiere mecanismo válido, evaluación y medidas adicionales cuando procedan. La ubicación no sustituye comprobar los flujos. El criterio de una autoridad es orientación, no certificación del producto.

### 2.4 Marco comparativo de jurisdicciones nacionales y edades de consentimiento [Z/P]

Al diseñar una aplicación escolar o integrar un modelo de IA, determina siempre la jurisdicción real del centro docente y de su alumnado. El idioma de la interfaz no define por sí solo el derecho aplicable. El art. 8 del RGPD permite a los Estados miembros fijar la edad de consentimiento digital entre los 13 y los 16 años; la normativa educativa y el criterio de las autoridades de control respecto a la nube y la IA presentan notables divergencias nacionales:

| País / Jurisdicción | Edad art. 8 RGPD | Autoridad de Control | Normativa Educativa y Restricciones de Nube / IA |
| --- | --- | --- | --- |
| **España (ES)** | 14 años (LOPDGDD art. 7) | AEPD + agencias autonómicas | LOE (DA 23); notas técnicas de la AEPD sobre k-anonimidad y obligatoriedad de DPD en centros docentes (art. 34.1.b LOPDGDD). |
| **Chequia (CZ)** | 15 años (Ley 110/2019) | ÚOOÚ | Ley de Educación 561/2004 (§ 28); enfoque pragmático para nubes licenciadas; orientaciones del ministerio MŠMT y NPI (AIDIG). |
| **Alemania (DE)** | 16 años (BDSG § 16) | DSK + 16 autoridades estatales (LfDI, BayLDA, LDI) | 16 leyes educativas estatales; prohibiciones o fuertes restricciones a nubes comerciales de EE. UU. (M365, Google); EIPD (DSFA) obligatoria para IA. |
| **Francia (FR)** | 15 años (Loi Informatique et Libertés) | CNIL | Code de l'éducation; plataformas públicas ENT; circulares ministeriales contra nubes estadounidenses gratuitas; directrices CNIL contra cuentas de aula que revelan identidades. |
| **Polonia (PL)** | 16 años (Ley de Protección de Datos 2018) | UODO | Prawo oświatowe; responsabilidad del director del centro como responsable; prohibición de introducir PII en IA sin contrato del art. 28; prohibición judicial de biometría en centros. |
| **Ucrania (UA)** | 14-18 años (capacidad parcial según CC) | Comisionado del Parlamento (Defensor del Pueblo) | Ley 2297-VI y proyecto de ley 8153 armonizado con RGPD; ecosistema estatal Mrija; el alumnado refugiado en la UE se rige íntegramente por el RGPD. |

#### Reglas de Implementación Transfronteriza y Específica por País

1. **Despliegues en Alemania (Prioridad Local Absoluta):** [Z] Para centros alemanes, aplica el límite de 16 años y la descentralización de 16 estados federales. Siguiendo los acuerdos de la DSK sobre Microsoft 365 y Copilot, prioriza el tratamiento estrictamente local (L0) en servidores escolares o código abierto (Moodle, IServ). Toda salida de datos requiere una rigurosa EIPD (DSFA) sin telemetría.
2. **Despliegues en Francia (Soberanía y Protección frente a la Identificación):** [Z] En centros franceses respeta la edad de 15 años y las directrices sobre entornos ENT. En despliegues de IA sigue las recomendaciones de la CNIL: prohíbe cuentas genéricas de aula donde los alumnos introduzcan cuasi-identificadores en sus consultas, y garantiza que las notas no dependan exclusivamente del modelo sin revisión docente.
3. **Despliegues en Polonia (Responsabilidad Directiva y Prohibición de Biometría):** [Z] En Polonia la responsabilidad jurídica recae íntegramente en la dirección del centro. El profesorado no puede dar de alta herramientas de IA sin contrato formal de encargo (art. 28 RGPD). Respeta la edad de 16 años y la prohibición judicial tajante de lectores biométricos en colegios.
4. **Despliegues en Ucrania (Integración en la UE y Estándares Europeos):** [Z] Para el alumnado ucraniano en centros escolares de la UE rige plenamente el RGPD europeo y la legislación de acogida. Para software desarrollado para el sistema ucraniano, ajusta el diseño al proyecto de ley 8153, a la plataforma Mrija y a la desidentificación obligatoria previa al uso de IA.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Edición revisada de la versión 1.2, basada en la guía original de octubre de 2026. Conserva autor, licencia y avisos de cambios.
