"""Junta as tabelas processadas e valida. Ainda por implementar.

Ordem prevista:
1. votacoes_ar + votos_partido_ar
2. votacoes_pe + votos_eurodeputado_pe
3. ponte_partidos_pe_ar
4. indicadores_economicos
5. validações (sem duplicados, datas válidas, sentidos válidos) e escrita em Parquet
"""

from __future__ import annotations

SENTIDOS_VALIDOS = {"favor", "contra", "abstencao", "ausente"}


def validar_sentidos(valores) -> list:
    """Devolve os valores que não pertencem ao conjunto válido."""
    return [v for v in valores if v not in SENTIDOS_VALIDOS]


def construir():
    raise NotImplementedError("Implementar depois de confirmar as fontes (fase 1 do roadmap).")
