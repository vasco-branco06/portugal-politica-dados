# Fontes de terceiros

Esta pasta guarda referências a repositórios de outras pessoas. Não copies o código deles para o teu. Se quiseres ter uma cópia local para ler, usa submódulos Git.

Antes de ligar um repositório, confirma a licença no GitHub e regista-a em `docs/FONTES.md`.

## Submódulos opcionais

Corre `sh fontes/adicionar_submodulos.sh` na raiz do repositório (depois de `git init`). Em Windows, usa o Git Bash.

| Repositório | Para quê |
|---|---|
| openar-pt/api | Perceber como a AR está organizada em base de dados |
| openar-pt/mcp | Exemplo de servidor MCP sobre a AR |

O HowTheyVote publica os dados como ficheiros de uma release, não como código. Por isso é descarregado pelo `etl`, e não ligado como submódulo.
