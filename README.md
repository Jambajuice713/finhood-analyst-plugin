# Finhood Analyst

**Tu cartera de Zesty + metodología de análisis financiero, dentro de Claude.**

Creado por Finhood Agents. Incluye 13 procedimientos para revisar carteras,
investigar compañías, analizar earnings y trabajar con valoraciones y modelos.
Funciona con la cuenta Zesty que tú conectes. El paquete no contiene credenciales,
no instala servidores Finhood ni envía datos a Finhood.

## Empieza en Claude

1. Descarga [finhood-analyst-skill.zip](dist/finhood-analyst-skill.zip).
   En GitHub abre el archivo y pulsa **Download raw file**. No subas el ZIP de
   todo el repositorio como si fuera una skill.
2. En Claude, abre **Customize / Personalizar → Skills → + → Create skill →
   Upload a skill**. Sube ese ZIP y activa **finhood-analyst**.
3. Para analizar tu cartera, abre **Settings / Ajustes → Connectors / Conectores
   → Add custom connector**. Añade `https://mcp.zestyfinance.com/mcp` y autoriza
   **tu propia cuenta** en la ventana de Zesty. Activa el conector en la conversación.
4. Abre un chat y pega:

> Usa Finhood Analyst. Comprueba mi conexión con Zesty consultando solo el estado
> del mercado estadounidense, mi saldo y mis posiciones. Luego resume mi cartera
> en USD y su concentración. Indica la fecha de los datos y lo que falta. No hagas
> previews ni operaciones y no inventes rentabilidad si no tienes los flujos.

Necesitas que tu cuenta de Claude permita skills y conectores personalizados.
En cuentas de empresa puede depender del administrador. Para investigar empresas
sin consultar tu cartera basta la skill más búsqueda web o documentos aportados.
Nunca pegues contraseñas o tokens en el chat.

## Qué puedes pedir

| Quiero… | Prueba este prompt |
|---|---|
| Entender mi cartera | «Usa Finhood Analyst para revisar mi cartera Zesty y sus concentraciones». |
| Investigar una empresa | «Usa Finhood Analyst: analiza MSFT desde sus últimos filings; cita fuentes y distingue hechos de supuestos». |
| Analizar resultados | «Usa Finhood Analyst para evaluar los últimos earnings de NVDA y qué cambia en la tesis». |
| Comparar empresas | «Usa Finhood Analyst: compara tres compañías de este sector con múltiplos calculados sobre definiciones consistentes». |
| Valorar | «Usa Finhood Analyst para construir un DCF con supuestos explícitos y sensibilidad». |
| Revisar una planilla | «Usa Finhood Analyst para auditar este modelo adjunto y señalar fórmulas o supuestos que no cuadran». |

## Del análisis a una orden

Después de analizar una compañía puedes pedir preparar una compra indicando
el ticker, importe o cantidad y tipo de orden. Claude debe comprobar las
condiciones actuales y mostrar una vista previa antes de pedir aprobación.
«Quiero comprar» no equivale a aprobar detalles que aún no has visto.

Zesty ofrece tarjetas interactivas en clientes compatibles: tú pulsas Confirmar.
Cuando no se renderiza una tarjeta, puede haber una vista previa en texto y una
confirmación en el chat, si el cliente permite operar. En esa ruta, la herramienta
de confirmación envía la orden: no presupongas otra ventana posterior.
Si el cliente restringe operaciones, completa la compra en la app de Zesty.
La disponibilidad real de este flujo en Claude aún requiere una prueba allí.

## Qué incluye

Una skill de entrada, **Finhood Analyst**, carga solo el procedimiento necesario:
portfolio-review, position-sizing, morning-note, earnings-analysis,
earnings-preview, dcf-model, comps-analysis, 3-statement-model, model-update,
audit-xls, sector-overview, competitive-analysis e idea-generation.
También incluye un brief de cierre, cuatro roles analíticos, políticas y esquemas
para exportaciones privadas. No necesitas instalar trece skills por separado.

## Cuenta, privacidad y alcance

- Análisis de acciones y ETF estadounidenses en USD; los activos fuera de ese
  alcance se identifican. Las propuestas se entregan como texto.
- El análisis es de solo lectura. Una solicitud expresa de compra o venta abre
  un flujo separado: detalles elegidos por ti, vista previa y aprobación posterior
  de esa orden exacta. Solo funciona si el cliente lo permite. No hay trading
  automático, cambio de moneda, transferencias ni cancelaciones.
- La skill contiene instrucciones: no cambia permisos del conector ni garantiza
  que el cliente muestre una tarjeta interactiva.
- Zesty y Claude procesan la información según sus propios servicios. Finhood
  Analyst no incorpora un servidor, telemetría ni una cuenta compartida.
- No hay un perfil de inversión prefijado. Los límites se acuerdan contigo;
  cualquier umbral ilustrativo se identifica como ejemplo.
- Un chat inicial funciona sin memoria persistente. Los snapshots son opcionales
  y privados. El paquete no instala tareas programadas ni publica información.
- La búsqueda web aporta filings y noticias; no se garantiza consenso de mercado,
  históricos por acción ni métricas que necesiten datos ausentes.

## Cowork y Claude Code

La skill ZIP es la ruta principal. También hay un
[plugin ZIP](dist/finhood-analyst-plugin.zip) para clientes que permitan subir
plugins. Instala **una de las dos variantes**, para evitar duplicar instrucciones.
El conector Zesty se autoriza por separado con tu cuenta en ambas variantes.
La guía técnica está en [docs/CLAUDE.md](docs/CLAUDE.md).

## Estado de esta versión

**0.2.1 — candidata a publicación.** Estructura y controles estáticos comprobados;
la prueba de importación en una cuenta Claude y la comprobación del MCP en vivo
se registran por separado en [docs/VALIDATION.md](docs/VALIDATION.md). No se afirma
una certificación de Claude, Zesty o CFA Institute.

## Fuentes y licencia

Licencia [MIT](LICENSE). Referencias metodológicas y documentación oficial en
[docs/SOURCES.md](docs/SOURCES.md). Las marcas corresponden a sus titulares;
este es un proyecto independiente de Finhood Agents. Revisa los resultados antes
de usarlos para una decisión de inversión.
