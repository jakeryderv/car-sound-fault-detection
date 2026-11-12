# Engine fault detection from sound

Industry AI Challenge, Team 2 (Jeffrey Gregory and Jake Van Slyke)

- [Industry project report (PDF)](report/report.pdf)
- [Executed notebook with experiments and results](notebooks/engine_fault_classification.ipynb)
- [Team findings slides (Canvas PDF)](presentation/engine-fault-findings.pdf)

## Run the notebook

Use Python 3.12+, uv, and an NVIDIA GPU for the full experiment. The environment uses PyTorch with CUDA 12.8. Run these commands from the repository root, then select **Run All** in JupyterLab.

```bash
uv sync --locked
uv run jupyter lab notebooks/engine_fault_classification.ipynb
```

The first run downloads the KweriMoto recordings and model weights. The notebook writes its tables, plots, and feature caches to `results/`.
