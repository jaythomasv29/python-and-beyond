from pathlib import Path
path = Path("notes.txt")

print(path.name)

# files = [p for p in path.iterdir()]

# py_files = [p for p in path.rglob('*.py')]
# print(py_files)
print(path.exists())
# path.write_text("hello world")
print(path.read_text())