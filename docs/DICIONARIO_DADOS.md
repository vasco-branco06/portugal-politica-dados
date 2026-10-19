# Dicionário de dados (rascunho v0)

Convenções: nomes em minúsculas e sem acentos, datas em ISO 8601, chaves como texto.

## partidos
| coluna | tipo | descrição |
|---|---|---|
| partido_id | texto | sigla normalizada (ex.: PS, PSD) |
| nome | texto | nome completo |
| grupo_pe | texto | grupo político europeu habitual, se existir |

## legislaturas
| coluna | tipo | descrição |
|---|---|---|
| legislatura | texto | Constituinte, I a XVII |
| inicio | data | início |
| fim | data | fim, vazio se em curso |

## iniciativas_ar
| coluna | tipo | descrição |
|---|---|---|
| iniciativa_id | texto | identificador estável |
| legislatura | texto | |
| tipo | texto | projeto de lei, proposta de lei, etc. |
| titulo | texto | |
| autores | texto | partidos ou Governo |
| data_entrada | data | |

## votacoes_ar
| coluna | tipo | descrição |
|---|---|---|
| votacao_id | texto | identificador estável |
| iniciativa_id | texto | liga a iniciativas_ar |
| data | data | |
| resultado | texto | aprovado, rejeitado |
| fase | texto | generalidade, especialidade, final global |

## votos_partido_ar
| coluna | tipo | descrição |
|---|---|---|
| votacao_id | texto | liga a votacoes_ar |
| partido_id | texto | liga a partidos |
| sentido | texto | favor, contra, abstencao, ausente |

## votacoes_pe
| coluna | tipo | descrição |
|---|---|---|
| vote_id | texto | identificador do HowTheyVote |
| data | data | |
| titulo | texto | |
| resultado | texto | |

## votos_eurodeputado_pe
| coluna | tipo | descrição |
|---|---|---|
| vote_id | texto | liga a votacoes_pe |
| member_id | texto | eurodeputado |
| pais | texto | |
| grupo | texto | grupo político europeu |
| sentido | texto | favor, contra, abstencao, ausente |

## ponte_partidos_pe_ar
| coluna | tipo | descrição |
|---|---|---|
| partido_id | texto | partido português |
| grupo_pe | texto | grupo europeu |
| legislatura_pe | texto | legislatura europeia em que a ligação vale |

## indicadores_economicos
| coluna | tipo | descrição |
|---|---|---|
| fonte | texto | bpstat, ine, eurostat |
| serie_id | texto | identificador na fonte |
| nome | texto | |
| data | data | início do período |
| frequencia | texto | mensal, trimestral, anual |
| valor | número | |
| unidade | texto | |
