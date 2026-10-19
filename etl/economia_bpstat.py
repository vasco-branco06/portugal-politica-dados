"""Séries do Banco de Portugal via BPstat.

API aberta e sem chave. Documentação: https://bpstat.bportugal.pt/data/docs
Base usada em exemplos públicos: https://bpstat.bportugal.pt/data/v1
"""

from __future__ import annotations

BASE = "https://bpstat.bportugal.pt/data/v1"
DOCS = "https://bpstat.bportugal.pt/data/docs"


def serie(serie_id: int):
    """TODO: obter uma série por identificador e devolver um DataFrame com
    colunas fonte, serie_id, nome, data, frequencia, valor, unidade.

    A resposta vem em JSON-stat. Ler a documentação para o formato exato
    e a forma de listar séries disponíveis.
    """
    raise NotImplementedError(f"Ver {DOCS}")
