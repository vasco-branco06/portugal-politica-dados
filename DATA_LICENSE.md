# Licenças dos dados

O código deste repositório é MIT (ver `LICENSE`). Os dados não herdam essa licença: cada fonte mantém a sua.

Cada dataset publicado tem de indicar:

- a fonte original e o link;
- a licença da fonte;
- as transformações feitas;
- como citar.

Estado atual: nenhum dataset foi publicado. Onde diz "por confirmar", os dados não são republicados.

## Licença por fonte

Verificação feita a 2026-10-19. A tabela completa está em [docs/FONTES.md](docs/FONTES.md).

| Fonte | Origem da informação | Licença | Notas |
|---|---|---|---|
| HowTheyVote (votações do Parlamento Europeu) | https://howtheyvote.eu/data | ODbL (base de dados) e DbCL (conteúdos) | Pede atribuição. Bases derivadas publicadas têm de manter a ODbL. Fotografias de eurodeputados e resumos de votações não estão cobertos pela DbCL |
| openAR (dados da Assembleia da República) | README de https://github.com/openar-pt/api | MIT, declarada no README | Não há ficheiro LICENSE. Os dados vêm da Assembleia da República, cujos termos de reutilização estão por confirmar |
| teex-pt/leis-pt-consolidada | metadados em https://huggingface.co/datasets/teex-pt/leis-pt-consolidada | CC0-1.0 | |
| PORTULAN/parlamento-pt | metadados em https://huggingface.co/datasets/PORTULAN/parlamento-pt | por confirmar | Os metadados indicam só "other" |
| BPstat, INE, Eurostat, Pordata, Diário da República, DGSI | sítios oficiais | por confirmar | Termos de reutilização ainda não lidos |

## Código de terceiros ligado

Os submódulos em `fontes/` são repositórios de outras pessoas, com as suas licenças: `openar-pt/api` e `openar-pt/mcp` (MIT, declarada no README), `HowTheyVote/data` (só documentação) e `rgllm/awesome-portugal-data` (GPL-3.0). Nada deles é copiado para o código ou para os dados deste projeto.

Nota sobre a GPL-3.0: o `rgllm/awesome-portugal-data` é GPL-3.0 e está ligado como submódulo, sem copiar o seu texto. O `etl/catalogo.py` extrai apenas nome, URL e categoria de cada entrada e gera um índice de ligações em `docs/CATALOGO.md`. As descrições da lista original não são reproduzidas.
