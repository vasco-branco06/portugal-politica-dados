# Dicionário de dados (v0)

Convenções: nomes em minúsculas e sem acentos, datas em ISO 8601, chaves como texto.

Estado: as tabelas marcadas **confirmada** têm campos lidos nas fontes reais a 2026-10-19 (código do openAR e chamadas à API; cabeçalhos e valores dos ficheiros do HowTheyVote). As marcadas **rascunho** ainda não foram confirmadas contra nenhuma fonte.

## legislaturas (confirmada, fonte: openAR GET /v1/legislaturas)
| coluna | tipo | origem no openAR | descrição |
|---|---|---|---|
| legislatura | texto | id | Constituinte, I a XVII |
| nome | texto | nome | ex.: "XVII Legislatura" |
| inicio | data | dataInicio | início |
| fim | data | dataFim | fim, vazio se em curso |

## votacoes_ar (confirmada, fonte: openAR GET /v1/votacoes)
| coluna | tipo | origem no openAR | descrição |
|---|---|---|---|
| votacao_id | texto | id | só é único dentro da iniciativa; a chave é (iniciativa_id, votacao_id) |
| iniciativa_id | texto | iniciativaId | identificador da iniciativa |
| iniciativa_titulo | texto | iniciativaTitulo | |
| iniciativa_numero | texto | iniciativaNumero | |
| iniciativa_tipo | texto | iniciativaTipo | código do tipo de iniciativa, ex.: P |
| legislatura | texto | legislaturaId | liga a legislaturas |
| data | data | data | |
| resultado | texto | resultado | Aprovado, Rejeitado ou Prejudicado |
| unanime | booleano | unanime | |
| reuniao | texto | reuniao | número da reunião |
| tipo_reuniao | texto | tipoReuniao | ex.: RP |
| descricao | texto | descricao | pode vir vazio |

## votos_partido_ar (confirmada, derivada de votacoes_ar)
O openAR devolve, em cada votação, quatro listas de siglas: aFavor, contra, abstencao e ausencias. Cada sigla de cada lista passa a uma linha.
| coluna | tipo | descrição |
|---|---|---|
| iniciativa_id | texto | liga a votacoes_ar |
| votacao_id | texto | liga a votacoes_ar |
| partido_id | texto | sigla vinda da lista, ex.: PS, PSD, CH |
| sentido | texto | favor (aFavor), contra, abstencao ou ausente (ausencias) |

## votacoes_pe (confirmada, fonte: HowTheyVote votes.csv.gz)
| coluna | tipo | origem no HowTheyVote | descrição |
|---|---|---|---|
| vote_id | texto | id | |
| data | data | timestamp | o timestamp original tem data e hora |
| titulo | texto | display_title | |
| referencia | texto | reference | pode vir vazio |
| descricao | texto | description | pode vir vazio |
| procedimento_ref | texto | procedure_reference | pode vir vazio |
| votos_favor | inteiro | count_for | |
| votos_contra | inteiro | count_against | |
| votos_abstencao | inteiro | count_abstention | |
| votos_ausentes | inteiro | count_did_not_vote | |
| resultado | texto | result | valores vistos: ADOPTED, REJECTED; vazio em muitas linhas |

## votos_eurodeputado_pe (confirmada, fonte: HowTheyVote member_votes.csv.gz)
| coluna | tipo | origem no HowTheyVote | descrição |
|---|---|---|---|
| vote_id | texto | vote_id | liga a votacoes_pe |
| member_id | texto | member_id | liga a members.csv.gz (id) |
| sentido | texto | position | valores vistos: FOR, AGAINST, ABSTENTION, DID_NOT_VOTE |
| pais | texto | country_code | código de 3 letras, Portugal é PRT |
| grupo | texto | group_code | ex.: GUE_NGL, RENEW |
| grupo_sigla | texto | group_short_label | ex.: The Left, Renew |
| partido_nacional_id | texto | national_party_id | |
| partido_nacional | texto | national_party_short_label | ex.: BE, PCP |

## eurodeputados_pe (confirmada, fonte: HowTheyVote members.csv.gz)
Só os campos usados pelo projeto. O ficheiro tem também contactos e redes sociais, que não são recolhidos.
| coluna | tipo | origem no HowTheyVote | descrição |
|---|---|---|---|
| member_id | texto | id | |
| nome | texto | first_name | |
| apelido | texto | last_name | |
| pais | texto | country_code | |

## partidos (rascunho)
| coluna | tipo | descrição |
|---|---|---|
| partido_id | texto | sigla normalizada (ex.: PS, PSD) |
| nome | texto | nome completo |
| grupo_pe | texto | grupo político europeu habitual, se existir |

## iniciativas_ar (rascunho)
O openAR tem estes dados em GET /v1/iniciativas. Os campos ainda não foram confirmados um a um.
| coluna | tipo | descrição |
|---|---|---|
| iniciativa_id | texto | identificador estável |
| legislatura | texto | |
| tipo | texto | projeto de lei, proposta de lei, etc. |
| titulo | texto | |
| autores | texto | partidos ou Governo |
| data_entrada | data | |

## ponte_partidos_pe_ar (rascunho)
| coluna | tipo | descrição |
|---|---|---|
| partido_id | texto | partido português |
| grupo_pe | texto | grupo europeu |
| legislatura_pe | texto | legislatura europeia em que a ligação vale |

## indicadores_economicos (rascunho)
| coluna | tipo | descrição |
|---|---|---|
| fonte | texto | bpstat, ine, eurostat |
| serie_id | texto | identificador na fonte |
| nome | texto | |
| data | data | início do período |
| frequencia | texto | mensal, trimestral, anual |
| valor | número | |
| unidade | texto | |
