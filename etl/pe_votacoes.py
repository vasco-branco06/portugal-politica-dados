"""Votações do Parlamento Europeu a partir do dataset HowTheyVote.eu.

Fonte: https://github.com/HowTheyVote/data (CSV gzip, atualizado semanalmente,
só votações nominais, desde a 9.ª legislatura).
Confirmar a licença no site do HowTheyVote antes de republicar.
"""

from __future__ import annotations

import requests

from .utils import USER_AGENT, download, raw_dir

BASE = "https://github.com/HowTheyVote/data/releases/latest/download"

# votes.csv.gz está confirmado na documentação do projeto.
# Os restantes nomes são prováveis e têm de ser confirmados na página do export.
FICHEIROS = [
    "votes.csv.gz",
    "member_votes.csv.gz",
    "members.csv.gz",
    "groups.csv.gz",
    "group_memberships.csv.gz",
]


def descarregar() -> list[str]:
    """Descarrega os ficheiros do export. Ignora os que não existirem (404)."""
    destino = raw_dir("pe")
    obtidos = []
    for nome in FICHEIROS:
        url = f"{BASE}/{nome}"
        try:
            download(url, destino / nome)
            obtidos.append(nome)
        except requests.HTTPError as e:
            status = e.response.status_code if e.response is not None else "?"
            print(f"[pe] {nome}: ignorado (HTTP {status})")
    return obtidos


def filtrar_portugueses(member_votes, members):
    """TODO: filtrar eurodeputados com país Portugal e juntar ao grupo político.

    Depende dos nomes das colunas no export. Confirmar com os ficheiros descarregados.
    """
    raise NotImplementedError("Confirmar colunas do export do HowTheyVote primeiro.")
