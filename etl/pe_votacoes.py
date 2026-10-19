"""Votações do Parlamento Europeu a partir do dataset HowTheyVote.eu.

Fonte: https://github.com/HowTheyVote/data (CSV gzip, atualizado semanalmente,
só votações nominais, desde a 9.ª legislatura).
Licença por confirmar (o repositório não tem ficheiro de licença, ver docs/FONTES.md).
Não republicar os dados antes de a confirmar.
"""

from __future__ import annotations

import requests

from .utils import USER_AGENT, download, raw_dir

BASE = "https://github.com/HowTheyVote/data/releases/latest/download"

# Ficheiros confirmados na release de 2026-10-17 (https://github.com/HowTheyVote/data/releases).
# Colunas confirmadas nos cabeçalhos:
#   votes: id, timestamp, display_title, reference, description, procedure_reference, ...
#   member_votes: vote_id, member_id, position, country_code, group_code, group_short_label,
#                 national_party_id, national_party_short_label
#   members: id, first_name, last_name, country_code, date_of_birth, ...
#   groups: code, official_label, label, short_label
#   group_memberships: member_id, group_code, term, start_date, end_date
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
    """Votos dos eurodeputados portugueses (country_code == "PRT"), com nome.

    member_votes já traz o grupo político (group_code, group_short_label) e o partido
    nacional no momento do voto. De members só juntamos o nome.
    """
    pt = member_votes[member_votes["country_code"] == "PRT"]
    nomes = members[["id", "first_name", "last_name"]].rename(columns={"id": "member_id"})
    return pt.merge(nomes, on="member_id", how="left")
