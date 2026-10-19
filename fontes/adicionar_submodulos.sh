#!/bin/sh
# Adiciona repositórios de terceiros como submódulos Git, só para leitura.
# Confirma as licenças antes de usar o conteúdo e regista-as em docs/FONTES.md.
set -e
git submodule add https://github.com/openar-pt/api fontes/openar-api
git submodule add https://github.com/openar-pt/mcp fontes/openar-mcp
git submodule update --init
