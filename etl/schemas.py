"""Esquemas das tabelas processadas.

Só as tabelas confirmadas em docs/DICIONARIO_DADOS.md. Tipos: texto, data, inteiro, booleano.
Cada tabela indica as colunas, a chave primária e a fonte de origem.
"""

from __future__ import annotations

ESQUEMAS = {
    "legislaturas": {
        "colunas": {"legislatura": "texto", "nome": "texto", "inicio": "data", "fim": "data"},
        "chave": ["legislatura"],
        "fonte": "openAR",
    },
    "votacoes_ar": {
        "colunas": {
            "votacao_id": "texto", "iniciativa_id": "texto", "iniciativa_titulo": "texto",
            "iniciativa_numero": "texto", "iniciativa_tipo": "texto", "legislatura": "texto",
            "data": "data", "resultado": "texto", "unanime": "booleano", "reuniao": "texto",
            "tipo_reuniao": "texto", "descricao": "texto",
        },
        "chave": ["iniciativa_id", "votacao_id"],
        "fonte": "openAR",
    },
    "votos_partido_ar": {
        "colunas": {
            "iniciativa_id": "texto", "votacao_id": "texto", "partido_id": "texto",
            "sentido": "texto",
        },
        "chave": ["iniciativa_id", "votacao_id", "partido_id"],
        "fonte": "openAR",
    },
    "votacoes_pe": {
        "colunas": {
            "vote_id": "texto", "data": "data", "titulo": "texto", "referencia": "texto",
            "descricao": "texto", "procedimento_ref": "texto", "votos_favor": "inteiro",
            "votos_contra": "inteiro", "votos_abstencao": "inteiro",
            "votos_ausentes": "inteiro", "resultado": "texto",
        },
        "chave": ["vote_id"],
        "fonte": "HowTheyVote",
    },
    "votos_eurodeputado_pe": {
        "colunas": {
            "vote_id": "texto", "member_id": "texto", "sentido": "texto", "pais": "texto",
            "grupo": "texto", "grupo_sigla": "texto", "partido_nacional_id": "texto",
            "partido_nacional": "texto",
        },
        "chave": ["vote_id", "member_id"],
        "fonte": "HowTheyVote",
    },
    "eurodeputados_pe": {
        "colunas": {"member_id": "texto", "nome": "texto", "apelido": "texto", "pais": "texto"},
        "chave": ["member_id"],
        "fonte": "HowTheyVote",
    },
}


def validar(df, tabela: str) -> list[str]:
    """Devolve a lista de problemas de df face ao esquema. Lista vazia quer dizer válida."""
    if tabela not in ESQUEMAS:
        return [f"tabela desconhecida: {tabela}"]
    esquema = ESQUEMAS[tabela]
    problemas = []
    em_falta = [c for c in esquema["colunas"] if c not in df.columns]
    a_mais = [c for c in df.columns if c not in esquema["colunas"]]
    if em_falta:
        problemas.append(f"colunas em falta: {em_falta}")
    if a_mais:
        problemas.append(f"colunas fora do esquema: {a_mais}")
    if em_falta:
        return problemas
    chave = esquema["chave"]
    if df[chave].isna().any().any():
        problemas.append(f"valores vazios na chave {chave}")
    if df.duplicated(subset=chave).any():
        problemas.append(f"chaves duplicadas em {chave}")
    return problemas
