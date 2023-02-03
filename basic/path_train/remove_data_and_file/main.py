from pathlib import Path

working_dir = Path("input")

for path in working_dir.glob("*.txt"):
    with open(path, "wb") as deleted_file:
        deleted_file.write(b"")
        path.unlink()
