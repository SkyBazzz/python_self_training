from pathlib import Path


root_path = Path("input")

#  you can also replace text, merge data by cutting first element from readlines() or whatever you'd like to
for index, path in enumerate(root_path.iterdir(), start=1):
    with open(f"{path}", mode="r", encoding="utf-8") as data:
        context = data.read()
    with open(f"output/reformatted-file-{index}.txt", mode="w", encoding="utf-8") as data:
        data.write(context[:-2])
