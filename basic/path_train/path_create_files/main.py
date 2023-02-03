from pathlib import Path

root_dir = Path("files")

for i in range(1, 6):
    file_name = f"{i}_file.txt"
    file_path = Path(file_name)
    full_file_path = root_dir.joinpath(file_path)
    Path.touch(full_file_path)
