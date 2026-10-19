"""Séries do INE.

Usa o cliente pyptine (opcional): pip install "portugal-politica-dados[ine]"
Exemplo de uso do pyptine: INE().get_data("0004127") e export_csv.
Os códigos de indicador (7 dígitos) estão no portal do INE.
"""

from __future__ import annotations


def indicador(codigo: str):
    """Obtém um indicador do INE pelo código de 7 dígitos."""
    try:
        from pyptine import INE
    except ImportError as e:
        raise RuntimeError('Instala a extensão: pip install "portugal-politica-dados[ine]"') from e
    return INE(language="PT").get_data(codigo)
