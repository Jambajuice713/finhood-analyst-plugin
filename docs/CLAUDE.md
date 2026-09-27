# Instalación y comprobación

## Claude web / desktop

Sigue los cuatro pasos del README. La skill ZIP tiene una carpeta raíz llamada
`finhood-analyst`, con `SKILL.md` y todas sus referencias dentro. Subir un enlace
GitHub al chat permite consultarlo si hay acceso; no equivale a instalar la skill.
No es necesario conectar GitHub para usar el ZIP.

Si no aparece la opción de importar, verifica el plan y los permisos de tu
organización. Si Claude no usa la skill, comprueba que esté activa y escribe
explícitamente «Usa Finhood Analyst». Si puede leer documentos pero no usar el
conector, activa Zesty en esa conversación y revisa su autenticación.

## Pegar el enlace del repositorio

El enlace sirve para descubrir el proyecto y leer instrucciones si Claude tiene
acceso. No instala ni garantiza que cargue todos los archivos. Instala una de las
dos variantes siguientes para reutilizar la skill en conversaciones posteriores.
Puedes comenzar diciendo «Explícame el README y ayúdame a instalar Finhood Analyst».
El conector Zesty se conecta por separado con tu propia cuenta.

## Plugin

En la sección de plugins de Claude, usa la opción de subir un plugin personalizado
si tu cuenta la ofrece. Sube `dist/finhood-analyst-plugin.zip`. Incluye el manifiesto
`.claude-plugin/plugin.json` y la skill, sin credenciales ni configuración MCP.
Activa Zesty por separado. La interfaz de plugins puede variar según cuenta.

## Claude Code

Con el repositorio descargado y Claude Code instalado, desde su raíz:

```sh
claude --plugin-dir .
```

El plugin expone la skill `finhood-analyst`; invócala por su nombre o mediante
el menú `/`. Para conectar Zesty, la guía oficial publica:

```sh
claude mcp add --transport http zesty https://mcp.zestyfinance.com/mcp
```

Autentícate mediante `/mcp`. Usa una cuenta propia. No hay variables secretas que
añadir a este repositorio. Esta receta está basada en documentación oficial;
el registro de pruebas indica si se ha ejecutado realmente en Claude.

## Prueba mínima después de importar

1. Solicita comprobar la conexión: reloj de mercado, saldo y posiciones US.
2. Revisa en la actividad de Claude que abrió la skill y usó consultas reales.
3. Contrasta saldo/posiciones con la aplicación Zesty para la misma hora y moneda.
4. Pide un research de empresa: verifica fuentes, fecha y skill utilizada.
5. Si falta historial o hay aportes sin hora/valorización, debe declarar que la
   rentabilidad exacta no está disponible.

El flujo de compra es una comprobación separada: verifica primero que aparezcan
las herramientas de preview y que el cliente permita usarlas. Usa una vista previa
solo cuando realmente quieras preparar esa orden; no confirmes una compra como
prueba de instalación. La tarjeta con botones depende del soporte MCP Apps del
cliente. Una vista previa en texto no debe describirse como una ventana gráfica.

No copies respuestas con datos personales a GitHub. Para reportar un fallo basta
la versión, herramienta, nombres de campos y mensaje de error redactado.

## Reconstruir los paquetes

```sh
python3 -m pip install -r requirements-dev.txt
python3 scripts/build.py
python3 scripts/validate.py
```

El proceso de build usa una lista de archivos permitidos y no incluye estado,
credenciales, archivos locales ni historial Git. Ambos ZIP se generan desde la
misma skill canónica. No se requiere API ni conexión de red para construirlos.
