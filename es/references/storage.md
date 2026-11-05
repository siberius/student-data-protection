# 8. CSV y SQLite [P]

<!-- Referencia generada; edita la guía independiente mantenida. -->

Secciones de origen: 8.

## 8. CSV y SQLite [P]

### 8.1 SQLite como almacén transaccional

- SQLite es aceptable; SQLite ordinario no cifra por sí solo. La aplicación accede en servidor, no mediante descarga pública de la base. Para varias instancias y alta concurrencia, elige una base adecuada a la arquitectura; no compartas el archivo sin control en una unidad de red.
- Perfil predeterminado: cargas personales cifradas con AES-256-GCM en aplicación y disco o volumen cifrado. Las extensiones de cifrado tienen algoritmos propios; no afirmes que SQLCipher implica automáticamente AES-GCM. Índices, relaciones y recuentos sin cifrar pueden seguir siendo metadatos personales.
- Solo la cuenta del servicio accede al directorio y base; en Unix, aproximadamente directorio `0700`, archivos `0600`, ACL equivalente en otros sistemas. Sin directorio público web, ruta estática, bucket público, carpeta personal sincronizada ni repositorio.
- Consultas parametrizadas; nombres dinámicos de campos solo de lista permitida. Activa claves foráneas en cada conexión y restringe también por centro las relaciones importantes. Protege transaccionalmente envíos, invitaciones de un uso y auditoría de cambios. Gestiona base bloqueada, disco lleno y escritura incompleta.
- Incluye `-wal`, `-shm`, diario, temporales, volcados y archivos de fallo o intercambio en protección y conservación. Copia mediante [SQLite Online Backup API](https://sqlite.org/backup.html) consistente o instantánea verificada, no copia ciega del archivo principal activo sin WAL.
- Gestiona supresión a nivel de datos y copias. `secure_delete`, checkpoint o `VACUUM` pueden ayudar, pero no garantizan borrado físico en SSD, instantáneas y copias antiguas. En FTS y otras extensiones, verifica copias residuales. [SQLite PRAGMA secure_delete](https://sqlite.org/pragma.html#pragma_secure_delete).

### 8.2 CSV como exportación o almacenamiento limitado

Usa como almacén oficial una base transaccional adecuada y CSV como exportación controlada; SQLite sirve para despliegues pequeños definidos. Si el proyecto necesita CSV como almacén principal, implementa escritor único, bloqueo, validación de esquema, revisiones y sustitución atómica tras escritura y sincronización satisfactorias. Ante fallo, permanece la última versión completa. CSV por sí solo no aporta transacciones, papeles ni cifrado.

Archiva CSV en servidor dentro de contenedor AES-GCM autenticado, no cambiando la extensión. Construye texto en claro en memoria; temporales solo en espacio cifrado protegido con limpieza automática. Un ZIP ordinario con contraseña no sustituye este perfil.

Permite exportar solo a un papel con permiso explícito, dentro de centro, personas y categorías correspondientes. Incluye solo columnas necesarias, nunca tokens de sesión ni identificadores de dispositivo sin finalidad documentada. Audita creación y descarga. El endpoint vuelve a verificar sesión y permisos, devuelve `Cache-Control: no-store` y `Content-Disposition: attachment`; todo enlace es breve y limitado, no URL pública permanente.

Usa una biblioteca CSV que entrecomille correctamente delimitadores, comillas y saltos de línea. Proteger contra inyección de fórmulas es un paso separado: en exportaciones para lectura humana en hojas de cálculo, trata texto que comience por `=`, `+`, `-`, `@`, caracteres de control y variantes de evasión. Interpreta columnas numéricas como números, no cadenas arbitrarias. Apóstrofo y entrecomillado no garantizan universalmente seguridad tras guardar y reabrir en Excel. Define el procedimiento de importación admitido y prueba Excel y LibreOffice; si no puede garantizarse seguridad, ofrece un formato con celdas explícitamente textuales para lectura humana y rechaza la exportación arriesgada. No modifiques los datos originales por la exportación. [OWASP CSV Injection](https://owasp.org/www-community/attacks/CSV_Injection).

Un CSV descargado y abierto es una copia sin cifrar en el dispositivo receptor. Informa sobre almacenamiento seguro y plazo de eliminación; cerrar sesión no lo borra. Si necesitas transferir un archivo cifrado fuera de la aplicación, utiliza un canal seguro gestionado o contenedor adecuado con entrega separada del secreto.

© 2026 Luděk Sušický. [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Edición revisada de la versión 1.1, basada en la guía original de octubre de 2026. Conserva autor, licencia y avisos de cambios.
