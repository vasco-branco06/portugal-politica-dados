"""Caminhos e utilitários partilhados."""

from __future__ import annotations

from datetime import date
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"

USER_AGENT = "portugal-politica-dados/0.1 (projeto de dados abertos)"


def raw_dir(fonte: str) -> Path:
    """Pasta de descarga com data, ex.: data/raw/pe/2026-10-19/."""
    d = RAW / fonte / date.today().isoformat()
    d.mkdir(parents=True, exist_ok=True)
    return d


def download(url: str, dest: Path, timeout: int = 120) -> Path:
    """Descarrega um ficheiro para dest, em blocos."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    with requests.get(url, stream=True, timeout=timeout, headers={"User-Agent": USER_AGENT}) as r:
        r.raise_for_status()
        with open(dest, "wb") as f:
            for chunk in r.iter_content(chunk_size=1 << 20):
                f.write(chunk)
    return dest


def get_json(url: str, params: dict | None = None, timeout: int = 60):
    r = requests.get(url, params=params, timeout=timeout, headers={"User-Agent": USER_AGENT})
    r.raise_for_status()
    return r.json()
