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
╭─ elimorals · agosto 2026 ────────────────────────────────────────╮
│                                                                  │
│   1 464 contribuciones   1277 commits · 165 pull requests        │
│        26 repositorios   12 públicos · 14 privados               │
│      25.1 MB de código   Python + TypeScript, sobre todo         │
│      5 537 repos con ★   curados desde julio de 2020             │
│                                                                  │
├─ lo que construyo · 25.1 MB en 26 repos ─────────────────────────┤
│                                                                  │
│  Python       ████████████████████████████████████████  45.6%    │
│  TypeScript   ███████████████████████████████           34.8%    │
│  JavaScript   ███████                                    8.3%    │
│  Jupyter      ███                                        3.0%    │
│  Astro        ██                                         2.5%    │
│  PLpgSQL      ██                                         1.9%    │
│                                                                  │
├─ lo que sigo · 5 537 repos con estrella ─────────────────────────┤
│                                                                  │
│  Python       █████████████████████████████             32.8%    │
│  TypeScript   ███████████████                           17.6%    │
│  JavaScript   █████                                      6.2%    │
│  Go           ████                                       4.9%    │
│  Rust         ████                                       4.3%    │
│  C++          ████                                       4.0%    │
│                                                                  │
│  ai 434 · llm 387 · ai-agents 231 · mcp 230                      │
│  machine-learning 223 · claude-code 214 · react 210              │
│  deep-learning 163 · claude 160 · android 159 · cli 151          │
│  self-hosted 150 · openai 130 · docker 128 · macos 111           │
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
