from pathlib import Path

root_dir = Path("source")
file_paths = root_dir.iterdir()

for single_path in file_paths:
    # str.partition() is better than Path.stem in case > one suffix like example.tar.gz
    new_file_name = f"new_{single_path.stem}{single_path.suffix}"
    new_filepath = single_path.with_name(new_file_name)
    single_path.rename(new_filepath)
