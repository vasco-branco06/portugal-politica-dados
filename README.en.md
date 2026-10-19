# Portugal Politics and Data

Open data on parliamentary activity (Portugal and Europe), legislation and the Portuguese economy, cleaned, linked together and ready for analysis or model training.

Versão em português: [README.md](README.md)

> Status: skeleton (v0). Structure, sources and data dictionary are defined. The extractors are starting points and still need to be tested against the live sources.

## Planned content

1. Portuguese Parliament (AR) votes, by party, legislature and initiative.
2. European Parliament votes, with Portuguese MEPs identifiable.
3. Economic indicators (INE, Banco de Portugal, Eurostat) aligned by date.
4. Cross-links between the three layers.
5. Later: legislation (Diário da República) and case law, subject to confirmed reuse terms.

The project links to existing work (openAR, HowTheyVote, BPstat, INE and others) instead of copying it. See [docs/FONTES.md](docs/FONTES.md).

## Cloning with submodules

```
git clone --recurse-submodules https://github.com/vasco-branco06/portugal-politica-dados.git
```

If you already cloned without submodules:

```
git submodule update --init --recursive
```

## Quick start

```
python -m venv .venv
pip install -e ".[dev]"
python -m etl.cli --help
pytest
```

## See also

- [awesome-portugal-data](https://github.com/rgllm/awesome-portugal-data): list of open data repositories in Portugal (GPL-3.0, link only).

## Licenses

Code: MIT. Data: each source keeps its own license, see [DATA_LICENSE.md](DATA_LICENSE.md).
