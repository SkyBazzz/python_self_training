from pathlib import Path
import zipfile


root_dir = Path("files")
archive_path = Path("archive.zip")

with zipfile.ZipFile(archive_path, "w") as archive:
    for path in root_dir.rglob("*.txt"):
        # change the file name to be only its name and extension
        archive.write(path, arcname=path.relative_to(root_dir))
        # to delete a file after
        # path.unlink()

with zipfile.ZipFile(archive_path) as un_archive:
    un_archive.extractall("output")

# archive_path.unlink()
