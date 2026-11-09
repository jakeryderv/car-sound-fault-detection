# car-sound-fault-detection

Can a pre-trained audio model flag engines that need inspection from a short recording?
Industry AI Challenge project (Team 2): AST (Audio Spectrogram Transformer) adapted to the
[KweriMoto Engine Sounds](https://huggingface.co/datasets/rayyyyy007/kwerimoto-engine-sounds) dataset
(`healthy` / `engine_knock` / `misfire`).

- `notebooks/engine_fault_classification.ipynb` — executed notebook: data and leakage checks, benchmark,
  baseline, three controlled experiments, source-shortcut analyses
- `results/` — experiment log, analysis tables and figures written by the notebook
- `report/report.qmd` → `report/report.pdf` — draft project report

## Reproduce

Requires [uv](https://docs.astral.sh/uv/) and an NVIDIA GPU (PyTorch is pinned to the CUDA 12.8 build, needed for
RTX 50-series cards). The notebook downloads the dataset (~280 MB) into `data/` on first run.

```bash
uv sync
uv run jupyter lab notebooks/engine_fault_classification.ipynb      # or run headless:
(cd notebooks && uv run jupyter nbconvert --to notebook --execute --inplace engine_fault_classification.ipynb)
uv run quarto render report/report.qmd                                # needs Quarto >= 1.4
```

A full notebook run takes ~4 minutes on an RTX 5070 Ti laptop GPU.
