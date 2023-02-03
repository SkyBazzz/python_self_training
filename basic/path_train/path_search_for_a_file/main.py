from pathlib import Path


search_dir = Path("../../path_train")
search_element = "4"

for path in search_dir.rglob("*"):
    if search_element in path.stem:
        print(path.resolve())
        print(path.absolute())
