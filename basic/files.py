import tempfile


temp_file = tempfile.NamedTemporaryFile()
try:
    temp_file.write(b"Hello world!")
    temp_file.seek(0)

    print(temp_file.read())
finally:
    temp_file.close()

with tempfile.TemporaryDirectory() as tmp_dir:
    print(tmp_dir)
