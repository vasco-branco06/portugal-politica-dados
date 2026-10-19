from etl import catalogo

LISTA = """\
# Titulo

## Portugal

| API | Descricao |
| --- | --- |
| [Portal X](https://exemplo.pt/api) | texto que nao deve ser copiado |
| [Repo Y](https://github.com/dono/repo-y.git) | outro texto |
| [Mau](ftp://exemplo.pt) | url invalido |
| sem ligacao | nada |

## Norte

| [Portal Z](http://norte.pt) | texto |
"""


def test_ler_entradas_extrai_nome_url_e_categoria():
    entradas = catalogo.ler_entradas(LISTA)
    assert entradas == [
        {"nome": "Portal X", "url": "https://exemplo.pt/api", "categoria": "Portugal"},
        {"nome": "Repo Y", "url": "https://github.com/dono/repo-y.git", "categoria": "Portugal"},
        {"nome": "Portal Z", "url": "http://norte.pt", "categoria": "Norte"},
    ]


def test_url_invalido_e_ignorado():
    assert not catalogo.url_valido("ftp://exemplo.pt")
    assert not catalogo.url_valido("não é um url")
    assert not catalogo.url_valido("https://")
    assert catalogo.url_valido("https://exemplo.pt")


def test_repo_github():
    assert catalogo.repo_github("https://github.com/dono/repo-y.git") == "dono/repo-y"
    assert catalogo.repo_github("https://github.com/dono") is None
    assert catalogo.repo_github("https://exemplo.pt/dono/repo") is None


class _Resp:
    def __init__(self, status, corpo=None):
        self.status_code = status
        self._corpo = corpo or {}

    def json(self):
        return self._corpo


class _Sessao:
    def __init__(self, resp):
        self.resp = resp

    def get(self, *args, **kwargs):
        return self.resp


def test_licenca_github_le_spdx():
    s = _Sessao(_Resp(200, {"license": {"spdx_id": "MIT"}}))
    assert catalogo.licenca_github("a/b", s)[0] == "MIT"


def test_licenca_em_falta_fica_por_confirmar():
    assert catalogo.licenca_github("a/b", _Sessao(_Resp(200, {"license": None})))[0] == "por confirmar"
    assert catalogo.licenca_github("a/b", _Sessao(_Resp(404)))[0] == "por confirmar"


def test_construir_junta_fontes_diretas():
    entradas = [{"nome": "Portal X", "url": "https://exemplo.pt", "categoria": "Portugal"}]
    linhas = catalogo.construir(entradas, hoje="2026-10-19")
    assert linhas[0]["licenca"] == "por confirmar"
    assert linhas[0]["origem"] == "awesome-portugal-data"
    assert len(linhas) == 1 + len(catalogo.FONTES_DIRETAS)
