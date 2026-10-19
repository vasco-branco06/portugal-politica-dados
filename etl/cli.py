"""Linha de comandos: python -m etl.cli --help"""

from __future__ import annotations

import argparse
import json

from . import ar_votacoes, pe_votacoes


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="etl", description="Portugal Política e Dados")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("pe-votacoes", help="Descarrega o export do HowTheyVote (Parlamento Europeu)")

    ar = sub.add_parser("ar-legislatura", help="Mostra os totais de uma legislatura (openAR)")
    ar.add_argument("leg", help="ex.: XVII")

    args = p.parse_args(argv)

    if args.cmd == "pe-votacoes":
        obtidos = pe_votacoes.descarregar()
        print(f"Descarregados: {obtidos}")
    elif args.cmd == "ar-legislatura":
        print(json.dumps(ar_votacoes.legislatura(args.leg), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
