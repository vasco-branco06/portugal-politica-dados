"""Votações da Assembleia da República via openAR.

Fonte: https://api.openar.pt (código em https://github.com/openar-pt/api).
Confirmado no código do openAR (src/api/routes/votacoes.ts) e numa chamada real a 2026-10-19:
- todas as rotas têm o prefixo /v1 (sem ele a API responde 404);
- GET /v1/legislaturas devolve uma lista com id, nome, dataInicio, dataFim, arId, siglaAntiga;
- GET /v1/votacoes aceita legislatura, resultado, unanime, iniciativa, tipo, grupo,
  a_favor, contra, abstencao, data_inicio, data_fim, sort, page (padrão 1) e limit
  (padrão 50, máximo 200);
- a resposta é {data, total, page, limit}. Cada item de data tem id, iniciativaId,
  iniciativaTitulo, iniciativaNumero, iniciativaTipo, legislaturaId, data, resultado,
  unanime, reuniao, tipoReuniao, descricao, aFavor, contra, abstencao, ausencias
  (as quatro últimas são listas de siglas de partidos).
Limite do serviço: 100 pedidos por minuto por IP.
"""

from __future__ import annotations

from typing import Iterator

from .utils import get_json

BASE = "https://api.openar.pt/v1"

VOTACOES_PATH = "/votacoes"


def legislaturas() -> list:
    return get_json(f"{BASE}/legislaturas")


def legislatura(leg: str) -> dict:
    """Ex.: legislatura('XVII'). Devolve totais de iniciativas, deputados e votações."""
    return get_json(f"{BASE}/legislaturas/{leg}")


def iter_paginas(path: str, params: dict | None = None, limit: int = 200) -> Iterator[dict]:
    """Percorre uma listagem paginada e devolve cada item.

    As listagens do openAR respondem {data, total, page, limit}. Aceita também uma lista simples.
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
    """Todas as votações de uma legislatura, como vêm do openAR (ex.: votacoes('XVII')).

    Ainda não normaliza para o dicionário de dados: aFavor, contra, abstencao e ausencias
    vêm como listas de siglas e têm de ser expandidas em votos_partido_ar.
    """
    return list(iter_paginas(VOTACOES_PATH, {"legislatura": leg}))
