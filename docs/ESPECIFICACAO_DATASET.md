# Especificação do dataset unificado

Documento de desenho para a próxima fase. Descreve o que vai ser construído, não o que já existe. Nada aqui está implementado, exceto onde indicado.

Estado dos factos: os campos das tabelas confirmadas foram lidos nas fontes reais a 2026-10-19 (ver [DICIONARIO_DADOS.md](DICIONARIO_DADOS.md)). O que não está confirmado diz "por confirmar".

## 1. Objetivo

Um dataset único, em Parquet, que junta três camadas ligadas entre si:

1. votações da Assembleia da República (AR), por partido;
2. votações do Parlamento Europeu (PE), com os eurodeputados portugueses identificáveis;
3. indicadores económicos portugueses, alinhados por data.

Cada linha tem de poder ser seguida até à fonte original, à data de descarga e à licença.

## 2. Arquitetura

### Fluxo

```
Fontes externas              Extração (etl/)             Camadas em disco
---------------------        -------------------         -------------------------
openAR  /v1/legislaturas  -> ar_votacoes.py          -> data/raw/ar/<data>/
openAR  /v1/votacoes      -> ar_votacoes.py          -> data/raw/ar/<data>/
HowTheyVote releases      -> pe_votacoes.py          -> data/raw/pe/<data>/
BPstat (JSON-stat)        -> economia_bpstat.py      -> data/raw/bpstat/<data>/
INE (pyptine)             -> economia_ine.py         -> data/raw/ine/<data>/
                                    |
                                    v
                          normalização + validação   -> data/processed/<tabela>.parquet
                                    |
                                    v
                          build_dataset.py           -> data/published/<tabela>.parquet
                                                        + manifesto + cartão do dataset
```

### Camadas

| Camada | Pasta | Conteúdo | Vai para o Git |
|---|---|---|---|
| raw | `data/raw/<fonte>/<data>/` | descarga original sem alterações | não |
| processed | `data/processed/` | tabelas limpas com os nomes do dicionário | não |
| published | `data/published/` | processed validado, com manifesto e licenças | não (publica-se no Hugging Face) |

### Módulos

| Módulo | Papel | Estado |
|---|---|---|
| `etl/ar_votacoes.py` | cliente do openAR (`/v1`) | feito, falta normalizar |
| `etl/pe_votacoes.py` | descarga do HowTheyVote e filtro dos eurodeputados portugueses | feito, falta normalizar |
| `etl/economia_bpstat.py` | séries do BPstat | por implementar |
| `etl/economia_ine.py` | séries do INE via pyptine | por implementar |
| `etl/catalogo.py` | índice de fontes | feito |
| `etl/schemas.py` | esquemas e validação | feito |
| `etl/pipeline.py` | corre todos os passos de extração | por criar |
| `etl/build_dataset.py` | junta, valida e escreve o dataset | por implementar |

### Ligações entre camadas

- AR e PE: tabela `ponte_partidos_pe_ar`, que associa cada partido português ao grupo político europeu em que os seus eurodeputados se sentam, por legislatura europeia. Por construir e por confirmar contra os dados.
- Política e economia: a data da votação, alinhada com séries mensais, trimestrais ou anuais. O alinhamento tem de indicar a frequência da série.

## 3. Esquemas das tabelas

Convenções: nomes de colunas em minúsculas e sem acentos, datas em ISO 8601, chaves como texto, valores em falta como nulos (nunca texto vazio).

### legislaturas (fonte: openAR `GET /v1/legislaturas`)
Chave: `legislatura`.

| coluna | tipo | origem |
|---|---|---|
| legislatura | texto | id |
| nome | texto | nome |
| inicio | data | dataInicio |
| fim | data | dataFim, nulo se em curso |

### votacoes_ar (fonte: openAR `GET /v1/votacoes`)
Chave composta: `(iniciativa_id, votacao_id)`. O id da votação só é único dentro da iniciativa.

| coluna | tipo | origem |
|---|---|---|
| votacao_id | texto | id |
| iniciativa_id | texto | iniciativaId |
| iniciativa_titulo | texto | iniciativaTitulo |
| iniciativa_numero | texto | iniciativaNumero |
| iniciativa_tipo | texto | iniciativaTipo |
| legislatura | texto | legislaturaId |
| data | data | data |
| resultado | texto | resultado (Aprovado, Rejeitado, Prejudicado) |
| unanime | booleano | unanime |
| reuniao | texto | reuniao |
| tipo_reuniao | texto | tipoReuniao |
| descricao | texto | descricao, pode ser nulo |

### votos_partido_ar (derivada de votacoes_ar)
Chave: `(iniciativa_id, votacao_id, partido_id)`. Cada sigla das listas `aFavor`, `contra`, `abstencao` e `ausencias` passa a uma linha.

| coluna | tipo | regra |
|---|---|---|
| iniciativa_id | texto | liga a votacoes_ar |
| votacao_id | texto | liga a votacoes_ar |
| partido_id | texto | sigla da lista |
| sentido | texto | favor, contra, abstencao ou ausente |

### votacoes_pe (fonte: HowTheyVote `votes.csv.gz`)
Chave: `vote_id`.

| coluna | tipo | origem |
|---|---|---|
| vote_id | texto | id |
| data | data | timestamp (só a data) |
| titulo | texto | display_title |
| referencia | texto | reference |
| descricao | texto | description |
| procedimento_ref | texto | procedure_reference |
| votos_favor | inteiro | count_for |
| votos_contra | inteiro | count_against |
| votos_abstencao | inteiro | count_abstention |
| votos_ausentes | inteiro | count_did_not_vote |
| resultado | texto | result (ADOPTED, REJECTED, nulo em muitas linhas) |

### votos_eurodeputado_pe (fonte: HowTheyVote `member_votes.csv.gz`)
Chave: `(vote_id, member_id)`. Só linhas com `country_code == "PRT"`.

| coluna | tipo | origem |
|---|---|---|
| vote_id | texto | vote_id |
| member_id | texto | member_id |
| sentido | texto | position (FOR, AGAINST, ABSTENTION, DID_NOT_VOTE) |
| pais | texto | country_code |
| grupo | texto | group_code |
| grupo_sigla | texto | group_short_label |
| partido_nacional_id | texto | national_party_id |
| partido_nacional | texto | national_party_short_label |

### eurodeputados_pe (fonte: HowTheyVote `members.csv.gz`)
Chave: `member_id`. Só nome e país. Contactos e redes sociais não são recolhidos.

| coluna | tipo | origem |
|---|---|---|
| member_id | texto | id |
| nome | texto | first_name |
| apelido | texto | last_name |
| pais | texto | country_code |

### Por definir
- `partidos`, `iniciativas_ar`, `ponte_partidos_pe_ar` e `indicadores_economicos`: rascunhos em [DICIONARIO_DADOS.md](DICIONARIO_DADOS.md), sem campos confirmados. `indicadores_economicos` terá fonte, série, nome, data, frequência, valor e unidade.
- Séries económicas: escolher 20 a 30 séries-chave (PIB, inflação, desemprego, juros, dívida) e confirmar os identificadores no BPstat e no INE.

## 4. Regras do dataset

### Qualidade (validadas antes de escrever)
1. Todas as colunas do esquema presentes e nenhuma a mais.
2. Chave primária sem valores vazios e sem duplicados.
3. Datas em ISO 8601 e dentro de um intervalo plausível.
4. `sentido` em `votos_partido_ar` só pode ser favor, contra, abstencao ou ausente.
5. `sentido` em `votos_eurodeputado_pe` só pode ser FOR, AGAINST, ABSTENTION ou DID_NOT_VOTE. Valor novo é erro, não é ignorado.
6. Integridade entre tabelas: toda a linha de `votos_partido_ar` liga a uma `votacoes_ar`, e toda a de `votos_eurodeputado_pe` liga a uma `votacoes_pe`.
7. Contagens coerentes: em `votacoes_pe`, os totais batem com o número de linhas de votos quando existem todos os votos.
8. Uma tabela que falha a validação não é escrita em `published`.

### Identificadores e nomes
- Cada tabela tem chave própria, que não depende da ordem de descarga.
- Os nomes de tabelas e colunas seguem o dicionário. Mudar um nome é uma alteração de versão.
- Os campos originais não são alterados. As conversões (por exemplo, `timestamp` para `data`) ficam documentadas na coluna "origem".

### Reprodutibilidade
- A descarga fica em `data/raw/<fonte>/<data>/` e nunca é editada.
- O mesmo `raw` tem de dar o mesmo `processed`.
- O manifesto regista, por tabela: fonte, URL, data de descarga, número de linhas, versão do esquema e licença.
- Respeitar o limite do openAR: 100 pedidos por minuto por IP.
- O `member_votes` do HowTheyVote pesa cerca de 100 MB: ler por partes.

### Licenças e publicação
- O código é MIT. Os dados mantêm a licença de cada fonte, ver [../DATA_LICENSE.md](../DATA_LICENSE.md).
- HowTheyVote é ODbL (base de dados) e DbCL (conteúdos). Se o dataset incluir dados dele, o dataset publicado tem de ser ODbL e dar atribuição. Fotografias e resumos de votações não estão cobertos e não se recolhem.
- Os dados da AR via openAR, o INE, o BPstat, o Eurostat e o Pordata têm licença por confirmar. Enquanto estiver por confirmar, o dataset não se publica.
- O dataset publicado leva um cartão com: fontes e links, licença de cada fonte, transformações feitas, como citar e limitações.
- Do `rgllm/awesome-portugal-data` (GPL-3.0) só se usam nome, URL e categoria no catálogo. Nada do seu texto entra no dataset.

### Limites conhecidos
- Na AR o voto vem por partido. Votos individuais de deputados por confirmar.
- O PE só publica votos individuais nas votações nominais.
- As séries económicas têm frequências diferentes. O alinhamento por data tem de indicar a frequência.
- O repositório `openar-pt/api` está arquivado: o serviço pode mudar ou deixar de existir sem aviso.

## 5. Ordem de construção prevista

1. `etl/pipeline.py` com um passo por fonte e a mesma interface.
2. Normalização da AR (legislaturas, votações, expansão das listas de partidos).
3. Normalização do PE, lendo o `member_votes` por partes.
4. Extratores do BPstat e do INE e escolha das séries.
5. `ponte_partidos_pe_ar`.
6. `build_dataset.construir()`, manifesto e cartão do dataset.
7. Comandos `extrair-tudo` e `construir-dataset` no CLI.
8. Confirmar as licenças em falta e só então publicar.
