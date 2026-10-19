# Arquitetura

## Fluxo de dados

```
Fontes externas            ETL (este repo)              Saída
-----------------          ----------------------       ------------------------
openAR API (AR)      -->   etl/ar_votacoes.py     -->   data/processed/*.parquet
HowTheyVote (PE)     -->   etl/pe_votacoes.py     -->        |
BPstat / INE         -->   etl/economia_*.py      -->        v
                           etl/build_dataset.py   -->   datasets publicados
                           (junta e valida)              (Hugging Face, gratuito)
```

## Camadas

1. **raw**: o que foi descarregado, sem alterações, em `data/raw/<fonte>/<data>/`. Serve para reproduzir e auditar.
2. **processed**: tabelas limpas, com nomes de colunas e identificadores estáveis, em Parquet. Ver [DICIONARIO_DADOS.md](DICIONARIO_DADOS.md).
3. **published**: versões dos processed com metadados, licença e citação, prontas a publicar.

## Decisões

- **Não copiar código de terceiros.** Ligar por referência (submódulos opcionais em `fontes/`) ou por dependência. Evita problemas de licença, sobretudo com GPL.
- **Parquet** como formato principal: pequeno, tipado e lido por pandas, DuckDB e Hugging Face.
- **Identificadores estáveis**: cada tabela tem uma chave própria que não depende da ordem de descarga.
- **Licença por fonte**: cada dataset publicado indica a licença e a origem de cada coluna relevante.
- **Reprodutível**: `python -m etl.cli <comando>` volta a gerar tudo a partir das fontes.
- **Custo zero**: GitHub (código e Actions), Hugging Face (datasets). Supabase só se for preciso uma API.

## Ligação entre camadas

A ponte entre Portugal e Europa é a tabela `ponte_partidos_pe_ar`, que associa cada partido português ao grupo político europeu em que os seus eurodeputados se sentam, por legislatura europeia. A ponte com a economia é a data da votação, usada para alinhar com séries mensais ou trimestrais.

## Limites conhecidos

- Na AR o voto é registado sobretudo por partido. Votos individuais de deputados só existem em casos pontuais. Confirmar nos ficheiros reais.
- O PE só publica votos individuais nas votações nominais.
- As séries económicas têm frequências diferentes (mensal, trimestral, anual). O alinhamento tem de indicar a frequência.
