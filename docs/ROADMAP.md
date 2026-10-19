# Roadmap

Ritmo previsto: 2 a 3 horas por dia útil. Estimativas, não promessas.

## Fase 0: esqueleto (concluída com este repositório)
- [x] Estrutura, documentação, fontes, dicionário de dados
- [x] Pacote `etl` com comandos iniciais

## Fase 1: fontes confirmadas (semana 1)
- [ ] Ler as licenças de cada fonte e preencher `docs/FONTES.md`
- [ ] Abrir `api.openar.pt` e confirmar os endpoints de votações e a forma da resposta
- [ ] Confirmar os ficheiros do export do HowTheyVote
- [ ] Confirmar se o voto na AR vem só por partido

## Fase 2: votações (semanas 2 a 4)
- [ ] `votacoes_ar` e `votos_partido_ar` em Parquet
- [ ] `votacoes_pe` e `votos_eurodeputado_pe`, com os eurodeputados portugueses
- [ ] `ponte_partidos_pe_ar`
- [ ] Testes de qualidade (sem duplicados, datas válidas, sentidos válidos)

## Fase 3: economia (semanas 5 a 8)
- [ ] Escolher 20 a 30 séries-chave (PIB, inflação, desemprego, juros, dívida)
- [ ] `indicadores_economicos` com frequência indicada
- [ ] Primeiro cruzamento: votos por partido e indicadores antes e depois

## Fase 4: publicação
- [ ] Cartão do dataset (licença, citação, limitações)
- [ ] Publicar no Hugging Face
- [ ] GitHub Actions para atualizar semanalmente

## Fase 5: legislação e jurisprudência
- [ ] Verificar termos do DGSI e anonimização
- [ ] Decidir se se liga ao portuguese-law-mcp ou se se constrói à parte
