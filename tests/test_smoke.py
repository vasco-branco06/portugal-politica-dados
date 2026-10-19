from etl import ar_votacoes, build_dataset, cli, pe_votacoes, utils


def test_caminhos_existem():
    assert utils.ROOT.exists()
    assert utils.RAW.parent.name == "data"


def test_pe_ficheiros_incluem_votes():
    assert "votes.csv.gz" in pe_votacoes.FICHEIROS


def test_validar_sentidos():
    assert build_dataset.validar_sentidos(["favor", "contra"]) == []
    assert build_dataset.validar_sentidos(["favor", "talvez"]) == ["talvez"]


def test_iter_paginas_para_numa_pagina_curta(monkeypatch):
    chamadas = []

    def falso(url, params=None, timeout=60):
        chamadas.append(params["page"])
        return [{"id": 1}, {"id": 2}]

    monkeypatch.setattr(ar_votacoes, "get_json", falso)
    itens = list(ar_votacoes.iter_paginas("/x", limit=200))
    assert len(itens) == 2
    assert chamadas == [1]


def test_cli_tem_comandos():
    try:
        cli.main(["--help"])
    except SystemExit as e:
        assert e.code == 0
