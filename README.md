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
╭─ elimorals · septiembre 2026 ────────────────────────────────────╮
│                                                                  │
│   1 853 contribuciones   1534 commits · 296 pull requests        │
│        27 repositorios   12 públicos · 15 privados               │
│      26.3 MB de código   Python + TypeScript, sobre todo         │
│      5 595 repos con ★   curados desde julio de 2020             │
│                                                                  │
├─ lo que construyo · 26.3 MB en 27 repos ─────────────────────────┤
│                                                                  │
│  Python       ████████████████████████████████████████  43.6%    │
│  TypeScript   ██████████████████████████████████        36.6%    │
│  JavaScript   ███████                                    8.1%    │
│  Jupyter      ███                                        2.9%    │
│  PLpgSQL      ██                                         2.5%    │
│  Astro        ██                                         2.3%    │
│                                                                  │
├─ lo que sigo · 5 595 repos con estrella ─────────────────────────┤
│                                                                  │
│  Python       ██████████████████████████████            32.7%    │
│  TypeScript   ████████████████                          17.7%    │
│  JavaScript   ██████                                     6.3%    │
│  Go           ████                                       4.8%    │
│  Rust         ████                                       4.4%    │
│  C++          ████                                       3.9%    │
│                                                                  │
│  ai 437 · llm 392 · ai-agents 239 · mcp 238                      │
│  machine-learning 224 · claude-code 218 · react 210              │
│  deep-learning 163 · claude 160 · android 160 · cli 153          │
│  self-hosted 151 · openai 130 · docker 128 · macos 114           │
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
