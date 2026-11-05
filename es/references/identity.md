# 5. Autenticación, invitaciones opcionales y sesiones [P]

<!-- Referencia generada; edita la guía independiente mantenida. -->

Secciones de origen: 5, 6.

## 5. Autenticación, invitaciones opcionales y sesiones [P]

### Elección del modo de acceso

Para registros personales duraderos, comunicación e historial, utiliza una cuenta individual verificada, por ejemplo SSO escolar o clave de acceso. Ofrece recuperación segura y eliminación de cuenta; no supongas que todo estudiante necesita contraseña. Para progenitores, verifica cuenta y permiso actual respecto al menor concreto. Un formulario puntual sin cuenta solo puede aceptar un envío definido; su confirmación no debe revelar datos almacenados.

Las secciones 5.1 y 5.2 se aplican **solo si se utilizan códigos de entrada o QR**. No justifican introducirlos. La sección 5.3 se aplica a todas las sesiones web.

### 5.1 Un código de cuatro cifras solo permite entrar en la sala

Cuatro cifras ofrecen 10 000 combinaciones, unos 13,3 bits de entropía. El código NO DEBE abrir historial, lista de clase, notas, interfaz docente ni permitir apropiarse de un registro personal existente.

1. Genera el código con un generador criptográficamente seguro (CSPRNG), selección uniforme e inclusión de ceros iniciales. Limita la búsqueda a un centro o sala; impide colisiones entre códigos activos de ese ámbito. No lo derives de la hora ni del identificador docente.
2. La validez de entrada predeterminada es 10 minutos, ampliable expresamente por el docente; cerrar la admisión invalida el código. Cerrar la entrada no tiene por qué terminar sesiones ya aceptadas.
3. Antes de verificar, no expongas datos personales ni listas de actividades no públicas. Un error no debe distinguir si el código existe, caducó o pertenece a otro centro.
4. Límites predeterminados: 5 intentos fallidos por 60 segundos y sesión previa a la entrada, seguidos de pausa de 60 segundos; 100 intentos fallidos por 5 minutos e IP origen; 200 intentos fallidos por 5 minutos y espacio de entrada del centro activan limitación temporal y aviso al docente. Contadores atómicos y compartidos entre instancias. Ajusta para NAT escolar y comprueba disponibilidad; no bloquees permanentemente todo un centro sin distinguir.
5. Una sesión de navegador nueva no debe eludir todos los límites. Frente a intentos distribuidos, considera también sala de espera y confirmación docente. Los límites no sustituyen verificar la persona; un atacante en el aula puede conocer legítimamente el código.
6. Conserva brevemente el código; verifica con HMAC, secreto de servidor separado y contexto de sala. Un hash simple de cuatro cifras no resiste búsquedas exhaustivas sin conexión. No registres el código.

### 5.2 QR

- Un QR puede llevar el mismo código y tiene entonces la misma seguridad. No lo presentes como autenticación más fuerte.
- El QR preferido contiene una invitación aleatoria con al menos 128 bits de entropía, finalidad `join`, sala, caducidad y posibilidad de revocación. Una invitación compartida de clase puede reutilizarse, pero no confirma identidad.
- Una invitación individual es de un solo uso y su canje por sesión es atómico. El servidor solo guarda el hash del secreto aleatorio; los canjes simultáneos no deben crear dos sesiones.
- No pongas el token en un parámetro ordinario de consulta que termine en registros. Flujo adecuado: fragmento de URL leído solo por código propio, retirada inmediata con `history.replaceState`, envío HTTPS POST y canje por cookie. Establece `Referrer-Policy: no-referrer`. El fragmento no protege absolutamente frente a historial, extensiones o capturas; son esenciales validez corta, revocación y alcance del permiso.

### 5.3 Ciclo de vida de sesión

- El servidor emite 32 bytes aleatorios de CSPRNG; almacena hash del token, alcance, identidad verificada o sesión anónima limitada, caducidad y estado de revocación. El token no contiene nombre ni calificación.
- Cookie: `__Host-school_session`, `Secure`, `HttpOnly`, `SameSite=Lax` o `Strict` según el flujo verificado, `Path=/`, sin `Domain`. No guardes un token portador en localStorage, URL ni registros ordinarios.
- Una entrada o inicio de sesión nuevos y un cambio de permisos crean token nuevo y revocan el anterior. El servidor no acepta tokens elegidos por el cliente.
- Inactividad predeterminada del estudiante: 30 minutos; máximo absoluto: 4 horas o fin de actividad puntual. Para docente: 15 minutos de inactividad y 8 horas absolutas; documenta ajustes disponibles para trabajo prolongado y accesibilidad. Las consultas automáticas periódicas no amplían la inactividad.
- Cerrar sesión implica revocación en servidor, caducidad de cookie y limpieza local. Ante cambio de contraseña, retirada de papel o incidente, un administrador puede revocar todas las sesiones relacionadas.
- Tras cerrar sesión, no se vuelve a registros personales por nombre o identificador de dispositivo. Permite recuperación solo con nueva verificación y transferencia segura del permiso.
- Protege escrituras mediante token CSRF y comprobación de origen; GET no cambia estado. `SameSite` es complementario. WebSocket verifica Origin, sesión y permisos de cada sala y termina el acceso tras revocación.

Fundamento: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html), [OWASP ASVS 5.0.0](https://asvs.owasp.org/). Los límites temporales y numéricos son decisiones del perfil, no valores legales.

## 6. Papeles, permisos e integridad de registros [P]

| Papel | Alcance permitido |
|---|---|
| Sin autenticar | Contenido público y posibles envíos limitados; sin lectura de registros personales. |
| Participante puntual | Solo actividad o envío permitidos actualmente; sin historial ni registros ajenos. |
| Estudiante verificado | Datos propios y funciones del alumnado; historial solo dentro de finalidad y permiso. Editar el perfil no modifica datos confirmados oficialmente. |
| Representante legal verificado | Solo datos del menor concreto para quien tenga permiso actual verificado; nunca toda la clase automáticamente. |
| Docente o personal del centro | Solo personas, clases, procesos y categorías de datos asignados y necesarios para su trabajo. |
| Personal especializado | Información más sensible solo con autorización explícita; el papel docente no abre por sí solo datos de orientación o salud. |
| Administrador del centro | Gestión de pertenencia al centro y permisos; no acceso automático a todo contenido. |
| Soporte operativo | Diagnóstico técnico sin contenido del alumnado; acceso excepcional limitado temporalmente, justificado y auditado. |
| Integración o cuenta de servicio | Solo operaciones y datos específicos necesarios para la integración aprobada. |
| DPD o auditor | Registros y auditoría definidos; no derecho automático a modificar registros escolares. |

Comprueba permisos en servidor para toda operación y objeto, incluidas listas, recuentos, búsqueda, adjuntos, exportaciones, WebSocket y tareas en segundo plano. Deriva `school_id`, papel y titularidad del contexto verificado. Si el cliente determina por quién actúa, verifica la relación correspondiente. Deniega por defecto. Un UUID o botón oculto no es autorización.

Cambiar centro o clase, la salida de un empleado, eliminar una cuenta o cambiar representación debe actualizar accesos, incluidas sesiones activas, enlaces compartidos e integraciones. No deduzcas el permiso parental solo por apellido coincidente o conocimiento de fecha de nacimiento. Revisa periódicamente pertenencias y papeles privilegiados.

El personal con acceso a datos del alumnado y los administradores tienen cuenta individual mediante SSO o autenticación segura; el perfil exige MFA, preferiblemente clave de acceso. La recuperación no debe eludir MFA. Guarda las contraseñas propias de forma unidireccional con implementación mantenida de Argon2id, nunca AES; ajusta parámetros a recomendaciones actuales y rendimiento del alojamiento.

El servidor valida todas las entradas. Titularidad, aprobación, asistencia, notas y otros datos oficiales tienen transiciones permitidas y papeles designados. Las escrituras importantes son transaccionales; una clave de idempotencia vinculada a usuario y operación evita duplicados. Cambios simultáneos sobre la misma versión producen conflicto controlado, no sobrescritura silenciosa. Corregir datos importantes registra autor, motivo y versión anterior en historial protegido con conservación propia.

**Si la aplicación evalúa:** el servidor calcula o confirma la puntuación; el resultado del cliente no es oficial; la clave de respuestas no se publica anticipadamente. **Si acepta solicitudes o asistencia:** el envío del usuario se distingue del registro aprobado; el usuario no puede fijar su propio estado de aprobación.

© 2026 Luděk Sušický. [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Edición revisada de la versión 1.1, basada en la guía original de octubre de 2026. Conserva autor, licencia y avisos de cambios.
