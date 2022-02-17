import os

print(os.path.splitext("/temp/test.txt.pdf"))

print(os.path.dirname(__file__))
print(os.pardir)
print(os.path.join(os.path.dirname(__file__), os.pardir))
