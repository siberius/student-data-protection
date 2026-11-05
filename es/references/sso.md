# 16. Identificación federada escolar y SSO [P]

<!-- Referencia generada; edita la guía independiente mantenida. -->

Secciones de origen: 16.

## 16. Identificación federada escolar y SSO [P]

Aplica solo donde se use proveedor de identidad. No sustituyas un acceso funcional solo para introducir SSO. Utiliza biblioteca de protocolo mantenida e instrucciones actuales del proveedor; la autorización OAuth por sí sola no demuestra identidad.

Para OIDC, valida emisor, firma con descubrimiento confiable de claves, audiencia prevista y parte autorizada cuando se exija, caducidad, nonce y correlación con la transacción. Usa flujo de código de autorización con PKCE donde sea compatible y requerido por el perfil del cliente; restringe exactamente URI de redirección, vincula el retorno al navegador iniciador e impide CSRF de acceso y repetición de códigos. No trates un token de acceso como token de identidad. Para SAML, valida firmas exigidas, emisor, audiencia, destino, destinatario, correlación de petición, condiciones temporales y repetición de aserción con implementación mantenida. No inventes un analizador de firmas XML. Elige comprobaciones del protocolo y flujo reales, no ambos protocolos por defecto.

Vincula identidades con identificador estable verificado y limitado al emisor confiable, por ejemplo emisor más sujeto; mapea después pertenencia autorizada a centro y papel correctos. Correo, nombre visible, dominio o declaración de centro no confiable por sí solos no deben fusionar cuentas ni conceder acceso de personal. Define alta, vinculación de cuentas, cambio de direcciones, cambios de sujeto, nombres duplicados y retirada de pertenencia. Asignar papeles privilegiados necesita datos confiables de derechos o un paso administrativo autorizado. Autenticarse ante el proveedor no concede por sí solo acceso a todos los registros escolares.

Mantén revocables las sesiones locales; cerrar sesión en proveedor y en aplicación tiene alcances diferentes. Reevalúa pertenencia y privilegios según propagación documentada y permite revocación inmediata en aplicación ante retirada conocida. No conserves silenciosamente acceso de personal hasta una caducidad lejana del token. Ante caída de proveedor o metadatos inválidos, deniega acceso protegido y ofrece alternativa operativa adecuada; no eludas MFA ni confíes en aserciones no verificadas.

En el flujo implementado, prueba emisor y audiencia erróneos, firma exigida ausente o inválida, aserción o código caducados o repetidos, estado o nonce de retorno discordantes, mapeo de centro ajeno, correo duplicado, pertenencia retirada y caída de proveedor. Registra versiones de protocolo y biblioteca y resultados reales. La tabla compartida añade escenarios SSO pertinentes; superar una prueba genérica de sesión no basta.

Orientación técnica: [OWASP OAuth2](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html), [OWASP SAML Security](https://cheatsheetseries.owasp.org/cheatsheets/SAML_Security_Cheat_Sheet.html).

Las adiciones específicas sobre papel del DPD, RAG y SSO se revisaron el 5 de noviembre de 2026 en la actualización de origen. La fecha original de comprobación de fuentes anterior es histórica; esta edición no afirma una auditoría jurídica completa nueva. Consulta el registro de fuentes para distinguir afirmaciones comprobadas y pendientes.

Autor: Luděk Sušický. Licencia [Creative Commons Atribución 4.0 Internacional (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). Conserva la atribución y el aviso de licencia al compartir o adaptar este documento.

© 2026 Luděk Sušický. [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Edición revisada de la versión 1.1, basada en la guía original de octubre de 2026. Conserva autor, licencia y avisos de cambios.
