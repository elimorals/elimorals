```
███████╗██╗     ██╗███╗   ███╗ ██████╗ ██████╗  █████╗ ██╗     ███████╗
██╔════╝██║     ██║████╗ ████║██╔═══██╗██╔══██╗██╔══██╗██║     ██╔════╝
█████╗  ██║     ██║██╔████╔██║██║   ██║██████╔╝███████║██║     ███████╗
██╔══╝  ██║     ██║██║╚██╔╝██║██║   ██║██╔══██╗██╔══██║██║     ╚════██║
███████╗███████╗██║██║ ╚═╝ ██║╚██████╔╝██║  ██║██║  ██║███████╗███████║
╚══════╝╚══════╝╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝

  AI engineer · agentes en producción · MCP · RAG · fine-tuning local
  Fundador técnico en @nexcar-ai · México
```

Construyo agentes que llegan a producción, no demos. Servidores MCP, RAG híbrido
y modelos afinados en local. Escribo casi todo en español porque el ecosistema
hispanohablante de AI engineering está desatendido y me interesa cerrar esa brecha.

### En qué estoy trabajando

**[jw-agent-toolkit](https://github.com/elimorals/jw-agent-toolkit)** · `Python`
Monorepo de 12 paquetes: servidor MCP con **129 herramientas**, 28 endpoints REST,
RAG híbrido (BM25 + vectorial + RRF) y fine-tuning local con alineamiento
(Unsloth/MLX, DPO/ORPO, Constitutional AI).
**131k LoC · 2 716 tests** · [jw-agent-toolkit.vercel.app](https://jw-agent-toolkit.vercel.app)

**[Skills_MX](https://github.com/elimorals/Skills_MX)** · `Python`
**83 servidores MCP** para el entorno burocrático mexicano: SAT, IMSS, INFONAVIT
y trámites de gobierno. Automatización de lo que en México todavía se hace a mano.
**1 667 tests** · [skills-mexico.vercel.app](https://skills-mexico.vercel.app)

**[comercio-exterior](https://github.com/elimorals/comercio-exterior)** · `Python`
Orquestador multi-agente para aduanas y comercio exterior: sub-agentes,
Critic + RefineLoop, memoria en 4 capas y framework de evaluación.

### 5 433 repos con estrella, y las herramientas para no ahogarme en ellos

Llevo años coleccionando repositorios. Llegó un punto en que la colección dejó de
ser útil por su propio tamaño, así que construí las herramientas para domarla:

**[Github-star-X](https://github.com/elimorals/Github-star-X)** · `Python`
Guarda automáticamente en GitHub los repos que descubro vía stars desde una cuenta
de X. El pipeline de captura.

**[StarGraph](https://github.com/elimorals/Github_graph_obsidian)** · `TypeScript` · `Python`
Analiza esos repos con estrella y genera un grafo de conocimiento navegable:
perfiles técnicos extraídos con Claude, embeddings en Pinecone y grafo en
Cytoscape.js sobre FastAPI + Next.js 15. La capa de sentido.

**[Contenido_automatizado](https://github.com/elimorals/Contenido_automatizado)** · `Python`
Pipeline de creación de contenido automatizado con agentes de IA, de la idea a
la publicación.

### Stats

<!-- stats:start -->
```
╭─ elimorals · octubre 2026 ───────────────────────────────────────╮
│                                                                  │
│   2 477 contribuciones   2010 commits · 442 pull requests        │
│        31 repositorios   12 públicos · 19 privados               │
│      31.1 MB de código   TypeScript + Python, sobre todo         │
│      5 677 repos con ★   curados desde julio de 2020             │
│                                                                  │
├─ lo que construyo · 31.1 MB en 31 repos ─────────────────────────┤
│                                                                  │
│  TypeScript   ████████████████████████████████████████  41.0%    │
│  Python       ███████████████████████████████████████   40.2%    │
│  JavaScript   ███████                                    7.0%    │
│  PLpgSQL      ████                                       4.0%    │
│  Jupyter      ██                                         2.4%    │
│  Astro        ██                                         2.0%    │
│                                                                  │
├─ lo que sigo · 5 677 repos con estrella ─────────────────────────┤
│                                                                  │
│  Python       ████████████████████████████████          32.6%    │
│  TypeScript   █████████████████                         17.8%    │
│  JavaScript   ██████                                     6.2%    │
│  Go           █████                                      5.2%    │
│  Rust         ████                                       4.4%    │
│  C++          ████                                       3.9%    │
│                                                                  │
│  ai 443 · llm 400 · ai-agents 252 · mcp 245                      │
│  machine-learning 225 · claude-code 224 · react 215              │
│  android 166 · deep-learning 162 · cli 159 · claude 159          │
│  self-hosted 156 · docker 135 · openai 129 · macos 119           │
│                                                                  │
╰──────────────────────────────────────────────────────────────────╯
```
<!-- stats:end -->

<sub>Bytes de código de mis 26 repos, privados incluidos · temas de mi colección
de repos con estrella · generado desde la API con
<a href="https://github.com/elimorals/elimorals/blob/main/card.py">card.py</a></sub>

### Cómo trabajo

`Python` · `TypeScript` · `MCP` · `RAG` · `LLMs locales` · `FastAPI` · `Next.js`

CI con `ruff` + `mypy --strict` + `pytest` + `bandit`. Conventional commits.
Roadmap por fases.

Me interesan los agentes **verificables**: los míos devuelven citas rastreables
en vez de texto plausible, y la lógica crítica corre sin LLM en el camino.

### Contacto

[LinkedIn](https://www.linkedin.com/in/elias-rashid-morales-mendoza/) ·
[X](https://x.com/elimoralsmendox) ·
[elimoralsmendox@gmail.com](mailto:elimoralsmendox@gmail.com)
