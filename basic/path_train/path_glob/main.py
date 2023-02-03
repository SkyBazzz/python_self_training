from pathlib import Path


rename_files_paths = Path("../path_glob")
# finds paths according to Regex
files_paths = rename_files_paths.glob("**/*")
for file_path in files_paths:
    if file_path.is_file():
        print(file_path.parts)
        print(file_path.parent)
        print(list(file_path.parents))
