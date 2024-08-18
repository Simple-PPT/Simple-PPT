import importlib
from pathlib import Path

def main(files: list[Path]):
    i: int = 1
    for file in files:
        p: Path = Path("./tmp"+str(i)+".py")
        p.write_text("from tools import *\n"+file.read_text())
        importlib.import_module(p.stem)
        p.unlink()
