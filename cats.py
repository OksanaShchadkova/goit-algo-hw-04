from pathlib import Path
from typing import List, Dict


def create_cats_file(filename: str):
    data = [
        "60b90c1c13067a15887e1ae1,Tayson,3",
        "60b90c2413067a15887e1ae2,Vika,1",
        "60b90c2e13067a15887e1ae3,Barsik,2",
        "60b90c3b13067a15887e1ae4,Simon,12",
        "60b90c4613067a15887e1ae5,Tessi,5"
    ]

    with open(filename, "w", encoding="utf-8") as fh:
        for entry in data:
            fh.write(entry + "\n")


# Створюємо файл
create_cats_file("cats.txt")


def get_cats_info(path: str | Path) -> List[Dict[str, str]]:
    """
    Повертає список словників з info про котів.
    """
    path = Path(path)
    cats: List[Dict[str, str]] = []

    try:
        with path.open("r", encoding="utf-8") as fh:
            for line in fh:
                try:
                    cat_id, name, age = line.strip().split(",")
                    cats.append({"id": cat_id, "name": name, "age": age})
                except ValueError:
                    # Якщо раптом не 3 поля — пропускаємо
                    continue
        return cats
    except FileNotFoundError:
        print(f"Файл {path} не знайдено")
        return []


# Створюємо файл
create_cats_file("cats.txt")

# Приклад використання
for cat in get_cats_info("cats.txt"):
    print(cat)
