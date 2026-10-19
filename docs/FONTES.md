# Fontes

Estado da licença: **por confirmar** significa que ainda não li os termos de reutilização. Nada daqui é republicado até estar confirmado.

As linhas do openAR, do HowTheyVote e do Hugging Face foram verificadas a 2026-10-19.

## Parlamento português (AR)

| Fonte | O que dá | Formato | Licença | Notas |
|---|---|---|---|---|
| Dados abertos da AR (parlamento.pt) | Iniciativas, deputados, votações | XML, JSON | por confirmar | Fonte oficial. https://www.parlamento.pt/Cidadania/Paginas/DadosAbertos.aspx |
| openAR API (openar-pt/api) | Os dados da AR normalizados em PostgreSQL, via API REST | JSON | MIT, declarada no README (sem ficheiro LICENSE) | Legislaturas Constituinte a XVII. Repositório arquivado no GitHub (só leitura), verificado a 2026-10-19. https://github.com/openar-pt/api e https://api.openar.pt |
| openAR MCP (openar-pt/mcp) | Servidor MCP sobre a openAR | MCP | MIT, declarada no README e no package.json (sem ficheiro LICENSE) | Repositório ativo, última alteração a 2026-05-25. https://github.com/openar-pt/mcp |
| Faltas no Parlamento (labs.tretas.org) | Presenças dos deputados em plenário | HTML | por confirmar | Confirmar se ainda está ativo |

## Parlamento Europeu

| Fonte | O que dá | Formato | Licença | Notas |
|---|---|---|---|---|
| HowTheyVote.eu (HowTheyVote/data) | Votações nominais, eurodeputados, grupos | CSV (gzip) | por confirmar | O repositório não tem ficheiro de licença. O README remete para https://howtheyvote.eu/about, que fala de licença aberta com atribuição obrigatória mas não a nomeia. Só votações nominais, desde a 9.ª legislatura. Dados nos releases (ficheiros csv.gz), não no código. https://github.com/HowTheyVote/data |
| Portal de dados abertos do PE | Resultados de votações e outros | vários | por confirmar | Fonte oficial |
| Registo de votos do Conselho da UE | Votos dos Estados-Membros | vários | por confirmar | Fonte oficial |

## Economia

| Fonte | O que dá | Formato | Licença | Notas |
|---|---|---|---|---|
| BPstat (Banco de Portugal) | Mais de 70 000 séries económicas e financeiras | JSON-stat | por confirmar | API aberta, sem chave. https://bpstat.bportugal.pt/data/docs |
| INE | Estatísticas nacionais | JSON | por confirmar | API do INE. Clientes: pyptine (Python, MIT), ineptR (R) |
| Pordata | Indicadores Portugal e Europa | HTML/CSV | por confirmar | Agrega INE, Eurostat e outros |
| Eurostat | Indicadores comparáveis da UE | vários | por confirmar | |

## Legislação e jurisprudência (fase seguinte)

| Fonte | O que dá | Formato | Licença | Notas |
|---|---|---|---|---|
| Diário da República (diariodarepublica.pt) | Texto oficial dos atos | HTML, PDF, dados abertos | textos oficiais isentos de direitos de autor (art. 8.º CDADC), confirmar | Acesso universal e gratuito |
| portuguese-law-mcp (Ansvar-Systems) | Legislação em SQLite, via MCP | MCP, SQLite | Apache-2.0 | Referido como cobrindo cerca de 1 130 diplomas |
| teex-pt/leis-pt-consolidada | Leis consolidadas | Hugging Face | CC0-1.0 (metadados do dataset) | Já existe, evitar duplicar. https://huggingface.co/datasets/teex-pt/leis-pt-consolidada |
| PORTULAN/parlamento-pt | Transcrições de debates em português europeu | Hugging Face | por confirmar | Os metadados indicam apenas "other", sem os termos. O identificador ParlamentoPT/ParlamentoPT não existe no Hugging Face. https://huggingface.co/datasets/PORTULAN/parlamento-pt |
| DGSI (dgsi.pt) | Jurisprudência dos tribunais | HTML | por confirmar | Verificar termos de reutilização e anonimização antes de recolher |

## Listas e catálogos

| Fonte | Licença | Notas |
|---|---|---|
| rgllm/awesome-portugal-data | GPL-3.0 | Só ligar. Copiar conteúdo obrigaria o nosso a GPL. https://github.com/rgllm/awesome-portugal-data |
| devpt-org/public-data-portugal | por confirmar | Lista com portais como o Base |
| dados.gov.pt | varia por dataset | Catálogo central de dados abertos |
