#!/usr/bin/env python3
"""Genera la tarjeta de stats ASCII de este README con datos reales de la API.

    python3 card.py              # imprime la tarjeta
    python3 card.py --write      # la inserta en README.md entre los marcadores
    python3 card.py --no-stars   # omite el escaneo de stars (lento) y usa la caché

Requiere `gh` autenticado. Incluye repos privados en los bytes de código:
los cuenta sin exponerlos.
"""

import json
import subprocess
import sys
from collections import Counter
from datetime import date
from pathlib import Path

HERE = Path(__file__).parent
CACHE = HERE / ".stars-cache.json"
README = HERE / "README.md"
START, END = "<!-- stats:start -->", "<!-- stats:end -->"

W = 66        # ancho interior del recuadro
BAR_MAX = 40  # bloques que ocupa el porcentaje mayor
MESES = ("enero febrero marzo abril mayo junio julio agosto septiembre "
         "octubre noviembre diciembre").split()
RUIDO = {"hacktoberfest", "open-source", "awesome", "awesome-list", "github",
         "opensource", "list", "collection", "nodejs", "node",
         "agent", "agents", "ai-agent", "llms"}  # duplican ai-agents / llm

REPOS_QUERY = """
{ viewer {
    createdAt
    starredRepositories { totalCount }
    contributionsCollection {
      totalCommitContributions
      totalPullRequestContributions
      contributionCalendar { totalContributions }
    }
    repositories(first: 100, ownerAffiliations: OWNER, isFork: false) {
      totalCount
      nodes { isPrivate languages(first: 12) { edges { size node { name } } } }
    }
} }
"""


def gh(*args: str) -> str:
    return subprocess.run(["gh", *args], capture_output=True, text=True,
                          check=True).stdout


def fetch_repos() -> dict:
    return json.loads(gh("api", "graphql", "-f", f"query={REPOS_QUERY}"))["data"]["viewer"]


def fetch_stars() -> dict:
    """Escanea todos los repos con estrella. Lento (~1 min), por eso se cachea."""
    repos = json.loads(gh("api", "user/starred?per_page=100", "--paginate"))
    langs, topics = Counter(), Counter()
    for r in repos:
        if r["language"]:
            langs[r["language"]] += 1
        topics.update(r.get("topics") or [])
    for t in list(topics):
        # los nombres de lenguaje ya salen en su propio panel; el resto es ruido
        if t in RUIDO or t.replace("-", "").replace("lang", "") in {l.lower() for l in langs}:
            del topics[t]
    data = {"total": len(repos), "langs": dict(langs.most_common(12)),
            "topics": dict(topics.most_common(24))}
    CACHE.write_text(json.dumps(data, indent=2))
    return data


def pcts(counts: dict, n: int) -> list[tuple[str, float]]:
    return [(k, v / n * 100) for k, v in list(counts.items())[:6]]


# --- dibujo ---------------------------------------------------------------

def rule(title: str = "", *, top: bool = False, bottom: bool = False) -> str:
    left, right = ("╭", "╮") if top else ("╰", "╯") if bottom else ("├", "┤")
    head = f"─ {title} " if title else ""
    return left + head + "─" * (W - len(head)) + right


def row(text: str = "") -> str:
    return "│" + text.ljust(W) + "│"


ALIAS = {"Jupyter Notebook": "Jupyter", "Objective-C": "Obj-C"}


def bar(name: str, pct: float, scale: float) -> str:
    name = ALIAS.get(name, name)[:13]
    return row(f"  {name:<13}{'█' * round(pct * scale):<41}{pct:>5.1f}%  ")


def fact(big: str, small: str) -> str:
    return row(f"  {big:>21}   {small:<38} ")


def wrap(items: list[str], width: int = 62) -> list[str]:
    """Agrupa 'tema N' en líneas separadas por ' · ' sin pasar de `width`."""
    lines, cur = [], ""
    for it in items:
        nxt = f"{cur} · {it}" if cur else it
        if len(nxt) > width:
            lines.append(cur)
            cur = it
        else:
            cur = nxt
    return lines + ([cur] if cur else [])


def build(v: dict, stars: dict) -> str:
    langs = Counter()
    for r in v["repositories"]["nodes"]:
        for e in r["languages"]["edges"]:
            langs[e["node"]["name"]] += e["size"]
    total_bytes = sum(langs.values())
    construyo = pcts(dict(langs.most_common(12)), total_bytes)
    sigo = pcts(stars["langs"], stars["total"])

    scale = BAR_MAX / max(p for _, p in construyo + sigo)
    mb = total_bytes / 1_000_000
    nodes = v["repositories"]["nodes"]
    priv = sum(r["isPrivate"] for r in nodes)
    c = v["contributionsCollection"]
    hoy = date.today()
    desde = v["createdAt"][:10].split("-")

    out = [rule(f"elimorals · {MESES[hoy.month - 1]} {hoy.year}", top=True), row()]
    out += [
        fact(f"{c['contributionCalendar']['totalContributions']:,} contribuciones".replace(",", " "),
             f"{c['totalCommitContributions']} commits · "
             f"{c['totalPullRequestContributions']} pull requests"),
        fact(f"{v['repositories']['totalCount']} repositorios",
             f"{len(nodes) - priv} públicos · {priv} privados"),
        fact(f"{mb:.1f} MB de código",
             f"{construyo[0][0]} + {construyo[1][0]}, sobre todo"),
        fact(f"{stars['total']:,} repos con ★".replace(",", " "),
             f"curados desde {MESES[int(desde[1]) - 1]} de {desde[0]}"),
    ]

    out += [row(), rule(f"lo que construyo · {mb:.1f} MB en {len(nodes)} repos"), row()]
    out += [bar(n, p, scale) for n, p in construyo]

    out += [row(), rule(f"lo que sigo · {stars['total']:,} repos con estrella".replace(",", " ")), row()]
    out += [bar(n, p, scale) for n, p in sigo]

    out += [row()]
    temas = wrap([f"{t} {n}" for t, n in stars["topics"].items()][:16])
    if temas and " · " not in temas[-1]:   # evita que el último tema quede huérfano
        temas.pop()
    out += [row(f"  {ln}") for ln in temas]
    out += [row(), rule(bottom=True)]

    assert len(set(map(len, out))) == 1, "líneas desalineadas"
    return "\n".join(out)


def main() -> None:
    stars = (json.loads(CACHE.read_text()) if "--no-stars" in sys.argv and CACHE.exists()
             else fetch_stars())
    card = build(fetch_repos(), stars)
    block = f"{START}\n```\n{card}\n```\n{END}"

    if "--write" in sys.argv:
        txt = README.read_text()
        head, _, rest = txt.partition(START)
        _, _, tail = rest.partition(END)
        README.write_text(head + block + tail)
        print("README.md actualizado")
    else:
        print(card)


if __name__ == "__main__":
    main()
