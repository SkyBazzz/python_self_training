from pathlib import Path


task_files_path = Path("files")

for task_file_path in task_files_path.rglob("*.txt"):
    if task_file_path.is_file():
        new_task_file_path = task_file_path.with_suffix(".csv")
        task_file_path.rename(new_task_file_path)
