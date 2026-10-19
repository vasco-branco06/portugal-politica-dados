#!/bin/sh
# Adiciona repositórios de terceiros como submódulos Git, só para leitura.
# Confirma as licenças antes de usar o conteúdo e regista-as em docs/FONTES.md.
# Podes correr o script mais de uma vez: ignora os submódulos que já existem.
set -e

adicionar() {
    url="$1"
    destino="$2"
    if git config -f .gitmodules --get "submodule.$destino.url" >/dev/null 2>&1; then
        echo "já existe: $destino"
    else
        git submodule add "$url" "$destino"
    fi
}

adicionar https://github.com/rgllm/awesome-portugal-data fontes/awesome-portugal-data
adicionar https://github.com/openar-pt/api fontes/openar-api
adicionar https://github.com/openar-pt/mcp fontes/openar-mcp
adicionar https://github.com/HowTheyVote/data fontes/howtheyvote-data

git submodule update --init
