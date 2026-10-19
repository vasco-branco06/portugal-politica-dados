# Portugal Política e Dados

Dados abertos sobre a atividade parlamentar (Portugal e Europa), legislação e economia portuguesa, limpos, ligados entre si e prontos a usar em análise ou para treinar modelos.

English version: [README.en.md](README.en.md)

> Estado: esqueleto (v0). A estrutura, as fontes e o dicionário de dados estão definidos. Os extratores são pontos de partida e precisam de ser testados contra as fontes reais.

## O que este projeto vai ter

1. **Votações do Parlamento português (AR)**, por partido, legislatura e iniciativa.
2. **Votações do Parlamento Europeu**, com os eurodeputados portugueses identificáveis.
3. **Indicadores económicos** (INE, Banco de Portugal, Eurostat) alinhados por data.
4. **Cruzamentos** entre as três camadas, por exemplo como cada partido votou uma lei e o que aconteceu aos indicadores depois.
5. Numa fase seguinte: **legislação** (Diário da República) e **jurisprudência**, sujeitas à confirmação dos termos de reutilização.

Este repositório liga-se a projetos que já existem (openAR, HowTheyVote, BPstat, INE e outros) em vez de os copiar. A lista está em [docs/FONTES.md](docs/FONTES.md).

## Estrutura

```
portugal-politica-dados/
  docs/          arquitetura, fontes, dicionário de dados, roadmap
  fontes/        referências a repositórios de terceiros (submódulos opcionais)
  etl/           código que descarrega e limpa os dados
  data/raw/      descargas originais (não vão para o Git)
  data/processed/ tabelas limpas em Parquet (não vão para o Git)
  datasets/      descrição dos datasets publicados
  tests/         testes
```

## Clonar com submódulos

```
git clone --recurse-submodules https://github.com/vasco-branco06/portugal-politica-dados.git
```

Para quem já clonou sem submódulos:

```
git submodule update --init --recursive
```

## Como começar

Requer Python 3.10 ou superior.

```
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS/Linux
pip install -e ".[dev]"
python -m etl.cli --help
python -m etl.cli pe-votacoes
pytest
```

## Fontes

Repositórios ligados em `fontes/` (submódulos Git). Detalhe em [fontes/README.md](fontes/README.md), [docs/FONTES.md](docs/FONTES.md) e [docs/CATALOGO.md](docs/CATALOGO.md).

| Repositório | Licença | Ligação |
|---|---|---|
| [rgllm/awesome-portugal-data](https://github.com/rgllm/awesome-portugal-data) | GPL-3.0 | submódulo, só se extraem nome, URL e categoria |
| [openar-pt/api](https://github.com/openar-pt/api) | MIT (declarada no README) | submódulo, arquivado |
| [openar-pt/mcp](https://github.com/openar-pt/mcp) | MIT (declarada no README) | submódulo |
| [HowTheyVote/data](https://github.com/HowTheyVote/data) | ODbL e DbCL (segundo o site) | submódulo e releases |

## Licenças

- Código: MIT (ver `LICENSE`).
- Dados: cada fonte tem a sua licença. Ver [DATA_LICENSE.md](DATA_LICENSE.md) e a coluna de licença em [docs/FONTES.md](docs/FONTES.md). Nada é republicado sem a licença confirmada.

## Contribuir

Ver [CONTRIBUTING.md](CONTRIBUTING.md).
