import sys
import time
from pathlib import Path

import nbformat
from nbclient import NotebookClient


def main():
    sys.stdout.reconfigure(errors="backslashreplace")
    path = Path(__file__).resolve().parent / "notebooks" / "engine_fault_classification.ipynb"
    notebook = nbformat.read(path, as_version=4)
    started = time.perf_counter()

    def cell_start(cell, cell_index):
        if cell.cell_type != "code":
            return
        first_line = cell.source.strip().split("\n", 1)[0]
        print(f"[{cell_index + 1}/{len(notebook.cells)}] {first_line[:80]}", flush=True)

    def cell_executed(cell, cell_index, execute_reply):
        for output in cell.outputs:
            if output.output_type == "stream":
                print(output.text.rstrip(), flush=True)

    client = NotebookClient(
        notebook,
        resources={"metadata": {"path": str(path.parent)}},
        timeout=1200,
        on_cell_start=cell_start,
        on_cell_executed=cell_executed,
    )
    try:
        client.execute()
    finally:
        nbformat.write(notebook, path)
    print(f"Executed {path.name} in {time.perf_counter() - started:.1f}s.", flush=True)


if __name__ == "__main__":
    main()
