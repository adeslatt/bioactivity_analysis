import nbformat

try:
    with open("../docs/notebooks/tutorial.ipynb", "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
    print("Notebook is valid.")
except Exception as e:
    print(f"Error: {e}")
