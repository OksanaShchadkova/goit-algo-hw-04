import sys
from pathlib import Path


def walk(path: Path, prefix: str = "") -> None:
    items = sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
    for i, p in enumerate(items):
        if p.is_dir():
            print(f"{prefix}{p.name}/")  # Додаємо слеш для директорій
            # Передаємо новий префікс для піддиректорій
            walk(p, prefix + f"{p.name}/")
        else:
            print(f"{prefix}{p.name}")  # Виводимо файли


def main():
    if len(sys.argv) != 2:
        print("Usage: python tree_view.py <directory>")
        sys.exit(1)

    root = Path(sys.argv[1])
    if not root.exists() or not root.is_dir():
        print("Шлях не існує або це не директорія")
        sys.exit(1)

    walk(root)


if __name__ == "__main__":
    main()
