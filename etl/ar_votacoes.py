"""Votações da Assembleia da República via openAR.

Fonte: https://api.openar.pt (código em https://github.com/openar-pt/api).
Confirmado no README do openAR: GET /legislaturas, GET /legislaturas/{leg},
listagens com page (padrão 1) e limit (padrão 50, máximo 200).
Ainda por confirmar: o caminho exato das votações e a forma da resposta.
Ver a documentação em https://api.openar.pt.
"""

from __future__ import annotations

from typing import Iterator

from .utils import get_json

BASE = "https://api.openar.pt"

# TODO: confirmar este caminho na documentação da API.
VOTACOES_PATH = "/votacoes"


def legislaturas() -> list:
    return get_json(f"{BASE}/legislaturas")


def legislatura(leg: str) -> dict:
    """Ex.: legislatura('XVII'). Devolve totais de iniciativas, deputados e votações."""
    return get_json(f"{BASE}/legislaturas/{leg}")


def iter_paginas(path: str, params: dict | None = None, limit: int = 200) -> Iterator[dict]:
    """Percorre uma listagem paginada e devolve cada item.

    Aceita respostas que sejam uma lista, ou um objeto com a lista em 'data' ou 'items'.
    Confirmar a forma real da resposta e ajustar.
    """
    page = 1
    while True:
        p = dict(params or {})
        p.update({"page": page, "limit": limit})
        resp = get_json(f"{BASE}{path}", params=p)
        if isinstance(resp, list):
            itens = resp
        else:
            itens = resp.get("data") or resp.get("items") or []
        if not itens:
            break
        yield from itens
        if len(itens) < limit:
            break
        page += 1


def votacoes(leg: str) -> list[dict]:
    """TODO: confirmar o nome do parâmetro de legislatura e normalizar para o dicionário de dados."""
    return list(iter_paginas(VOTACOES_PATH, {"legislatura": leg}))
