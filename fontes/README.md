# Fontes de terceiros

Esta pasta guarda referências a repositórios de outras pessoas. Não copies o código deles para o teu. Se quiseres ter uma cópia local para ler, usa submódulos Git.

Antes de ligar um repositório, confirma a licença no GitHub e regista-a em `docs/FONTES.md`.

## Submódulos

Corre `sh fontes/adicionar_submodulos.sh` na raiz do repositório (depois de `git init`). Em Windows, usa o Git Bash.

## Fontes ligadas

Verificação feita a 2026-10-19.

| Repositório | URL | Licença confirmada | Tipo de ligação | Verificado | O que nos dá |
|---|---|---|---|---|---|
| openar-pt/api | https://github.com/openar-pt/api | MIT, declarada no README (sem ficheiro LICENSE) | Submódulo (`fontes/openar-api`). Repositório arquivado, só leitura | 2026-10-19 | Como a AR está organizada em base de dados e na API |
| openar-pt/mcp | https://github.com/openar-pt/mcp | MIT, declarada no README e no package.json (sem ficheiro LICENSE) | Submódulo (`fontes/openar-mcp`) | 2026-10-19 | Exemplo de servidor MCP sobre a AR |
| HowTheyVote/data | https://github.com/HowTheyVote/data | Por confirmar: sem ficheiro de licença, o site fala de licença aberta com atribuição sem a nomear | Dependência: o `etl` descarrega os ficheiros dos releases | 2026-10-19 | Votações nominais do Parlamento Europeu, eurodeputados e grupos |
| rgllm/awesome-portugal-data | https://github.com/rgllm/awesome-portugal-data | GPL-3.0 | Hiperligação (não é submódulo, nada é copiado) | 2026-10-19 | Lista de repositórios de dados abertos de Portugal |
| teex-pt/leis-pt-consolidada | https://huggingface.co/datasets/teex-pt/leis-pt-consolidada | CC0-1.0 (metadados do dataset) | Hiperligação | 2026-10-19 | Leis consolidadas |
| PORTULAN/parlamento-pt | https://huggingface.co/datasets/PORTULAN/parlamento-pt | Por confirmar: os metadados indicam só "other" | Hiperligação | 2026-10-19 | Transcrições de debates parlamentares |

O HowTheyVote publica os dados como ficheiros de um release, não como código. O repositório tem apenas 144 KB e o export completo pesa mais de 100 MB, por isso é descarregado pelo `etl` e não ligado como submódulo.

O `openar-pt/api` está arquivado: não recebe atualizações. Mantém-se como submódulo só para leitura.
