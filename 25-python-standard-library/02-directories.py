from pathlib import Path

path = Path("../24-modules/01-sales-module-exercise/ecommerce")
# print(path.exists())
# path.mkdir()
# path.rmdir()

# print(path.iterder())
paths = [p for p in path.iterdir() if p.is_dir()]
py_files = [p for p in path.glob("*.py")]
print(paths)
print(py_files)


# searching recursively
py_files2 = [p for p in path.rglob("*.py")]
print('p2', py_files2)