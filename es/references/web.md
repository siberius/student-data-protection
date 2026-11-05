# 9. Web, PWA y dispositivos compartidos [P]

<!-- Referencia generada; edita la guía independiente mantenida. -->

Secciones de origen: 9.

## 9. Web, PWA y dispositivos compartidos [P]

- El service worker solo almacena en caché una lista explícita de archivos estáticos públicos. Las API personales, resultados, HTML con datos y exportaciones usan solo red y `Cache-Control: no-store`; un fallo de red no debe devolver datos personales antiguos desde caché alternativa.
- El perfil predeterminado no guarda datos personales ni tokens duraderos en localStorage, IndexedDB o Cache Storage. Una PWA sin conexión puede mostrar una estructura pública. Una solución sin conexión con datos personales necesita diseño separado: datos mínimos, clave con acceso controlado, caducidad, borrado y prueba de pérdida del dispositivo. Guardar la clave junto al texto cifrado no proporciona separación efectiva.
- Cerrar sesión borra memoria de interfaz, formularios, almacenamiento local pertinente, cachés y otras pestañas abiertas. Usa `Clear-Site-Data` como complemento tras verificar compatibilidad e impacto en un origen compartido. Al volver por historial o bfcache, vuelve a verificar la página y oculta contenido personal hasta entonces.
- Cerrar sesión sin conexión limpia el cliente y no debe afirmar revocación satisfactoria en servidor hasta confirmarla. Al volver la conexión, completa la revocación; la caducidad de servidor limita el riesgo residual. En dispositivo compartido, no restaures una sesión personal por haber restaurado la ventana del navegador.
- No puedes garantizar eliminar capturas, extensiones, memoria del sistema operativo ni archivos ya descargados. No afirmes «todos los datos desaparecen al cerrar sesión»; describe exactamente qué almacenamiento controla la aplicación.
- Prevén XSS con escape contextual, desactivación de HTML no verificado y CSP restrictiva con nonce o hash; limita `connect-src`, `frame-ancestors`, `object-src` y `base-uri`. No admitas orígenes CORS arbitrarios ni credenciales con comodín. Añade `X-Content-Type-Options: nosniff`.
- Sin rastreadores publicitarios ni reproducción de sesiones en pantallas del alumnado. Minimiza scripts de terceros; errores y analítica deben ocultar datos. Las importaciones tienen límite de tamaño, esquema, nombres seguros y comprobaciones de contenido.
- Actualiza entorno de ejecución y dependencias, conserva archivo de bloqueo, comprueba secretos y vulnerabilidades conocidas, separa pruebas y producción. ASVS nivel 2 es el objetivo de verificación predeterminado en el ámbito pertinente, no una afirmación de certificación. [OWASP ASVS 5.0.0](https://asvs.owasp.org/).

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Edición revisada de la versión 1.1, basada en la guía original de octubre de 2026. Conserva autor, licencia y avisos de cambios.
