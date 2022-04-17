from pathlib import Path
Path("/usr/local/bin") # absolute path
Path()

path = Path("../24-modules/01-sales-module-exercise/ecommerce/__init__.py")
print(path)
print(path.name)
print(path.is_file())
print(path.is_dir())
print(path.stem)
print(path.suffix)
print(path.parent)