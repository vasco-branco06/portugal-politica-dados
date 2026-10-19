import pandas as pd

from etl import schemas


def _legislaturas(**extra):
    base = {"legislatura": ["XVI", "XVII"], "nome": ["a", "b"],
            "inicio": ["2024-03-26", "2025-06-03"], "fim": [None, None]}
    base.update(extra)
    return pd.DataFrame(base)


def test_esquema_valido():
    assert schemas.validar(_legislaturas(), "legislaturas") == []


def test_esquema_colunas_em_falta():
    df = _legislaturas().drop(columns=["nome"])
    assert any("em falta" in p for p in schemas.validar(df, "legislaturas"))


def test_esquema_chave_duplicada_e_vazia():
    dup = _legislaturas(legislatura=["XVII", "XVII"])
    assert any("duplicadas" in p for p in schemas.validar(dup, "legislaturas"))
    vazia = _legislaturas(legislatura=["XVII", None])
    assert any("vazios" in p for p in schemas.validar(vazia, "legislaturas"))


def test_tabela_desconhecida():
    assert schemas.validar(_legislaturas(), "nao_existe") == ["tabela desconhecida: nao_existe"]
