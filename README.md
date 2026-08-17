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
│   1 044 contribuciones   962 commits · 60 pull requests          │
│        26 repositorios   12 públicos · 14 privados               │
│      24.5 MB de código   Python + TypeScript, sobre todo         │
│      5 438 repos con ★   curados desde julio de 2020             │
│                                                                  │
├─ lo que construyo · 24.5 MB en 26 repos ─────────────────────────┤
│                                                                  │
│  Python       ████████████████████████████████████████  45.0%    │
│  TypeScript   ███████████████████████████████           35.3%    │
│  JavaScript   ███████                                    8.4%    │
│  Jupyter      ███                                        3.1%    │
│  Astro        ██                                         2.5%    │
│  PLpgSQL      ██                                         1.7%    │
│                                                                  │
├─ lo que sigo · 5 438 repos con estrella ─────────────────────────┤
│                                                                  │
│  Python       █████████████████████████████             33.0%    │
│  TypeScript   ████████████████                          17.5%    │
│  JavaScript   ██████                                     6.3%    │
│  Go           ████                                       4.7%    │
│  C++          ████                                       4.1%    │
│  Rust         ████                                       4.1%    │
│                                                                  │
│  ai 426 · llm 371 · machine-learning 223 · mcp 221               │
│  ai-agents 220 · react 207 · claude-code 206                     │
│  deep-learning 162 · claude 158 · android 157 · cli 147          │
│  self-hosted 144 · docker 127 · openai 126 · macos 109           │
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
