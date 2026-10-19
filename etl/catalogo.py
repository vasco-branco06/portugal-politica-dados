"""Catálogo de fontes: índice de ligações com metadados.

Lê a lista em fontes/awesome-portugal-data (GPL-3.0) e extrai só nome, URL e categoria.
Não copia as descrições da lista. Junta ainda as fontes diretas do projeto.
Gera data/processed/catalogo_fontes.csv e docs/CATALOGO.md.

Uso: python -m etl.catalogo
"""

from __future__ import annotations

import csv
import os
import re
from datetime import date
from urllib.parse import urlparse

import requests

from .utils import PROCESSED, ROOT, USER_AGENT

LISTA = ROOT / "fontes" / "awesome-portugal-data" / "README.md"
CSV_SAIDA = PROCESSED / "catalogo_fontes.csv"
MD_SAIDA = ROOT / "docs" / "CATALOGO.md"

POR_CONFIRMAR = "por confirmar"
CAMPOS = ["nome", "url", "categoria", "origem", "licenca", "motivo", "verificado"]

LIGACAO = re.compile(r"\[([^\]]+)\]\((\S+?)\)")
GITHUB_REPO = re.compile(r"^/([^/]+)/([^/#?]+?)(?:\.git)?/?$")

# Fontes diretas. A licença só é preenchida quando foi confirmada a partir da própria fonte.
# Verificação feita em 2026-10-19: URLs a responder e licença lida quando existia.
FONTES_DIRETAS = [
    {"nome": "BPstat (Banco de Portugal)", "url": "https://bpstat.bportugal.pt/data/v1",
     "categoria": "Economia", "licenca": POR_CONFIRMAR,
     "motivo": "termos de reutilização da API não lidos"},
    {"nome": "INE: cliente pyptine", "url": "https://github.com/randsley/pyptine",
     "categoria": "Economia", "licenca": "MIT",
     "motivo": "licença do cliente; os dados do INE têm os seus próprios termos, por confirmar"},
    {"nome": "Eurostat", "url": "https://ec.europa.eu/eurostat",
     "categoria": "Economia", "licenca": POR_CONFIRMAR,
     "motivo": "política de reutilização não lida"},
    {"nome": "Pordata", "url": "https://www.pordata.pt",
     "categoria": "Economia", "licenca": POR_CONFIRMAR,
     "motivo": "termos de utilização não lidos"},
    {"nome": "Diário da República", "url": "https://diariodarepublica.pt",
     "categoria": "Legislação", "licenca": POR_CONFIRMAR,
     "motivo": "enquadramento legal dos textos oficiais por confirmar"},
    {"nome": "DGSI (jurisprudência)", "url": "https://www.dgsi.pt",
     "categoria": "Legislação", "licenca": POR_CONFIRMAR,
     "motivo": "termos de reutilização e anonimização não lidos"},
    {"nome": "PORTULAN/parlamento-pt (Hugging Face)",
     "url": "https://huggingface.co/datasets/PORTULAN/parlamento-pt",
     "categoria": "Parlamento", "licenca": POR_CONFIRMAR,
     "motivo": "metadados indicam apenas 'other'"},
    {"nome": "teex-pt/leis-pt-consolidada (Hugging Face)",
     "url": "https://huggingface.co/datasets/teex-pt/leis-pt-consolidada",
     "categoria": "Legislação", "licenca": "CC0-1.0",
     "motivo": "lida nos metadados do dataset"},
]


def url_valido(url: str) -> bool:
    """Aceita só http e https com host."""
    p = urlparse(url.strip())
    return p.scheme in ("http", "https") and bool(p.netloc)


def ler_entradas(markdown: str) -> list[dict]:
    """Extrai nome, URL e categoria das linhas de tabela. Ignora tudo o resto."""
    categoria = ""
    entradas = []
    for linha in markdown.splitlines():
        if linha.startswith("## "):
            categoria = linha[3:].strip()
            continue
        if not linha.startswith("|"):
            continue
        primeira_celula = linha.strip("|").split("|")[0]
        m = LIGACAO.search(primeira_celula)
        if not m:
            continue
        nome, url = m.group(1).strip(), m.group(2).strip()
        if not url_valido(url):
            continue
        entradas.append({"nome": nome, "url": url, "categoria": categoria})
    return entradas


def repo_github(url: str) -> str | None:
    """Devolve 'dono/repo' se o URL for de um repositório do GitHub."""
    p = urlparse(url)
    if p.netloc.lower() not in ("github.com", "www.github.com"):
        return None
    m = GITHUB_REPO.match(p.path)
    return f"{m.group(1)}/{m.group(2)}" if m else None


def licenca_github(dono_repo: str, sessao=requests) -> tuple[str, str]:
    """Licença SPDX segundo a API do GitHub, ou ('por confirmar', motivo)."""
    headers = {"User-Agent": USER_AGENT, "Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    try:
        r = sessao.get(f"https://api.github.com/repos/{dono_repo}", headers=headers, timeout=30)
    except requests.RequestException as e:
        return POR_CONFIRMAR, f"falha de rede: {type(e).__name__}"
    if r.status_code != 200:
        return POR_CONFIRMAR, f"API do GitHub respondeu {r.status_code}"
    licenca = (r.json().get("license") or {}).get("spdx_id")
    if not licenca or licenca == "NOASSERTION":
        return POR_CONFIRMAR, "o repositório não declara licença reconhecida"
    return licenca, "lida na API do GitHub"


def construir(entradas: list[dict], sessao=requests, hoje: str | None = None) -> list[dict]:
    """Junta lista e fontes diretas e preenche a licença dos repositórios do GitHub."""
    hoje = hoje or date.today().isoformat()
    linhas = []
    for e in entradas:
        licenca, motivo = POR_CONFIRMAR, "não é um repositório do GitHub"
        repo = repo_github(e["url"])
        if repo:
            licenca, motivo = licenca_github(repo, sessao)
        linhas.append({**e, "origem": "awesome-portugal-data", "licenca": licenca,
                       "motivo": motivo, "verificado": hoje})
    for d in FONTES_DIRETAS:
        linhas.append({**d, "origem": "fonte direta", "verificado": hoje})
    return linhas


def escrever_csv(linhas: list[dict], destino=CSV_SAIDA) -> None:
    destino.parent.mkdir(parents=True, exist_ok=True)
    with open(destino, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        w.writeheader()
        w.writerows(linhas)


def _celula(texto: str) -> str:
    return texto.replace("|", "/")


def escrever_md(linhas: list[dict], destino=MD_SAIDA) -> None:
    topo = [
        "# Catálogo de fontes",
        "",
        "Índice de ligações gerado por `python -m etl.catalogo`. Não edites à mão.",
        "As entradas com origem `awesome-portugal-data` vêm do índice de "
        "[rgllm/awesome-portugal-data](https://github.com/rgllm/awesome-portugal-data) (GPL-3.0). "
        "Aqui só se guardam nome, ligação e categoria.",
        "A licença é a do repositório, lida na API do GitHub. Onde não foi possível, diz "
        "\"por confirmar\" e o motivo. A licença dos dados de cada serviço tem de ser lida no próprio sítio.",
        "",
        "| Nome | Categoria | Origem | Licença | Motivo | Verificado |",
        "|---|---|---|---|---|---|",
    ]
    corpo = [
        f"| [{_celula(l['nome'])}]({l['url']}) | {_celula(l['categoria'])} | {l['origem']} "
        f"| {l['licenca']} | {_celula(l['motivo'])} | {l['verificado']} |"
        for l in linhas
    ]
    destino.write_text("\n".join(topo + corpo) + "\n", encoding="utf-8")


def main() -> int:
    entradas = ler_entradas(LISTA.read_text(encoding="utf-8"))
    linhas = construir(entradas)
    escrever_csv(linhas)
    escrever_md(linhas)
    por_confirmar = sum(1 for l in linhas if l["licenca"] == POR_CONFIRMAR)
    print(f"{len(linhas)} entradas, {por_confirmar} com licença por confirmar")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
