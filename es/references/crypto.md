# 7. Cifrado y gestión de claves [P]

<!-- Referencia generada; edita la guía independiente mantenida. -->

Secciones de origen: 7.

## 7. Cifrado y gestión de claves [P]

El RGPD no prescribe AES-256-GCM ni un cifrado universal único. Este perfil lo elige para proteger cargas personales en aplicación, archivos CSV y copias; TLS protege el transporte. Cifrar no sustituye la autorización ni protege frente a un proceso autorizado comprometido que posea la clave.

### 7.1 AES-256-GCM

- Usa biblioteca de alto nivel probada, clave aleatoria de 256 bits, nonce o IV de 96 bits y etiqueta de autenticación de 128 bits. No construyas tu propio cifrado. Una misma clave NO DEBE repetir un nonce, ni tras reiniciar, recuperar o entre instancias.
- Para cargas por fila, puedes usar nonce CSPRNG de 96 bits con índice único `(key_id, nonce)`, reserva atómica y regeneración ante colisión. Tras restaurar una base antigua, introduce primero una clave nueva para escrituras nuevas. Cuenta las operaciones agregadas de cifrado por clave; el perfil rota como máximo tras 10^6 operaciones o un año, antes ante incidente. Este límite conservador no redefine el límite general de NIST.
- Para un archivo CSV completo u objeto de copia, crea una clave de datos nueva por objeto y cífrala con una clave de envoltura gestionada. Procesa archivos grandes mediante biblioteca de flujo autenticado; no inventes formatos de fragmentos sin verificar.
- Los datos adicionales autenticados (AAD) deben vincular canónicamente versión de formato, centro, tipo e identificador del objeto y versión del registro. AAD no es secreto; no incluyas nombres. Obtén el contexto esperado independientemente, no solo de un envoltorio aportado por un atacante.
- El envoltorio contiene `format_version`, `algorithm`, `key_id`, `nonce`, `ciphertext`, `tag` y metadatos públicos necesarios. Rechaza cambios de nonce, AAD, texto cifrado o etiqueta sin devolver texto en claro. GCM por sí solo no impide reproducir una versión anterior válida completa; comprueba versión contra estado confiable y auditoría.

Fundamento: [NIST SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final), [NIST: anuncio de revisión](https://csrc.nist.gov/news/2024/nist-to-revise-sp-80038d-gcm-and-gmac-modes). No trates el anuncio como nueva norma terminada.

### 7.2 Claves y transporte

Separa claves de datos y datos; conserva claves de envoltura en KMS, HSM o gestor de secretos adecuado. La aplicación recibe permisos mínimos; las claves no deben aparecer en repositorio, JS de cliente, imagen ni copias junto a datos sin proteger. Separa producción y pruebas y finalidades de claves. La rotación debe conservar legibilidad de datos legítimamente retenidos y permitir revocación. Supervisa fallos de descifrado y operaciones de claves, no sus valores. [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html).

HTTPS y WSS en todas partes; prefiere TLS 1.3, TLS 1.2 solo cuando sea necesario por compatibilidad con ECDHE y AEAD. Desactiva SSL, TLS 1.0 y 1.1, conjuntos débiles y compresión TLS. AES-128-GCM o ChaCha20-Poly1305 en TLS no incumplen por sí solos el perfil. Verifica certificados, renovación y enlaces internos de red. Despliega HSTS tras verificar HTTPS, por ejemplo `max-age=31536000`; `includeSubDomains` solo tras comprobar todos los subdominios. Nunca envíes datos personales en solicitudes inseguras ni antes de una redirección. [OWASP TLS](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html).

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Edición revisada de la versión 1.1, basada en la guía original de octubre de 2026. Conserva autor, licencia y avisos de cambios.
