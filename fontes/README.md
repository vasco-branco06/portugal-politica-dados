# Fontes de terceiros

Esta pasta guarda cópias de leitura de repositórios de outras pessoas, como submódulos Git. Não copies o código deles para o teu. Cada submódulo aponta para um commit exato do repositório original, por isso a origem não se perde.

Antes de ligar um repositório, confirma a licença no GitHub e regista-a em `docs/FONTES.md`.

## Submódulos

Corre `sh fontes/adicionar_submodulos.sh` na raiz do repositório (depois de `git init`). Em Windows, usa o Git Bash. O script pode ser corrido mais de uma vez.

Para clonar já com tudo: `git clone --recurse-submodules <url>`. Para quem já clonou: `git submodule update --init --recursive`.

## Fontes ligadas

Verificação feita a 2026-10-19.

| Repositório | URL | Licença | Tipo de ligação | Verificado | O que nos dá |
|---|---|---|---|---|---|
| rgllm/awesome-portugal-data | https://github.com/rgllm/awesome-portugal-data | GPL-3.0 (API do GitHub) | Submódulo (`fontes/awesome-portugal-data`). O `etl/catalogo.py` só lê dela nome, URL e categoria | 2026-10-19 | Lista de repositórios e APIs de dados abertos de Portugal |
| openar-pt/api | https://github.com/openar-pt/api | MIT, declarada no README (sem ficheiro LICENSE) | Submódulo (`fontes/openar-api`). Repositório arquivado, só leitura | 2026-10-19 | Rotas e esquema reais da API da AR, incluindo `/v1/votacoes` |
| openar-pt/mcp | https://github.com/openar-pt/mcp | MIT, declarada no README e no package.json (sem ficheiro LICENSE) | Submódulo (`fontes/openar-mcp`) | 2026-10-19 | Exemplo de servidor MCP sobre a AR |
| HowTheyVote/data | https://github.com/HowTheyVote/data | ODbL para a base de dados, DbCL para os conteúdos (lido em https://howtheyvote.eu/data). O repositório não tem ficheiro de licença | Submódulo (`fontes/howtheyvote-data`, só tem README) e dependência: o `etl` descarrega os ficheiros dos releases | 2026-10-19 | Votações nominais do Parlamento Europeu, eurodeputados e grupos |
| teex-pt/leis-pt-consolidada | https://huggingface.co/datasets/teex-pt/leis-pt-consolidada | CC0-1.0 (metadados do dataset) | Hiperligação | 2026-10-19 | Leis consolidadas |
| PORTULAN/parlamento-pt | https://huggingface.co/datasets/PORTULAN/parlamento-pt | Por confirmar: os metadados indicam só "other" | Hiperligação | 2026-10-19 | Transcrições de debates parlamentares |

O HowTheyVote publica os dados como ficheiros de um release, não como código. O export completo pesa mais de 100 MB e o repositório tem 145 KB e só o README, por isso o submódulo serve para ler a documentação e os dados vêm do `etl`.

O `openar-pt/api` está arquivado: não recebe atualizações. Mantém-se como submódulo só para leitura.

O catálogo gerado a partir da lista está em [docs/CATALOGO.md](../docs/CATALOGO.md).
