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

## Licenças

- Código: MIT (ver `LICENSE`).
- Dados: cada fonte tem a sua licença. Ver [DATA_LICENSE.md](DATA_LICENSE.md) e a coluna de licença em [docs/FONTES.md](docs/FONTES.md). Nada é republicado sem a licença confirmada.

## Contribuir

Ver [CONTRIBUTING.md](CONTRIBUTING.md).
