from pathlib import Path
from typing import Tuple


def create_developers_file(filename: str):
    data = [
        "Alex Korp,3000",
        "Nikita Borisenko,2000",
        "Sitarama Raju,1000",
        "Alice Smith,3500",
        "Bob Johnson,2800",
        "Charlie Brown,4500",
        "Diana Prince,3200",
        "Ethan Hunt,2800",
        "Fiona Gallagher,4100",
        "George Costanza,2200"
    ]

    with open(filename, "w", encoding="utf-8") as fh:
        for entry in data:
            fh.write(entry + "\n")


def total_salary(path: str | Path) -> Tuple[int, float]:
    """
    Повертає (загальна_сума, середня_сума) зарплат розробників.
    """
    path = Path(path)

    try:
        with path.open("r", encoding="utf-8") as fh:
            salaries = []
            for line in fh:
                try:
                    _, amount = line.strip().split(",")
                    salaries.append(int(amount))
                except ValueError:
                    # Якщо рядок не коректний — пропускаємо
                    continue

        if not salaries:
            return 0, 0.0

        total = sum(salaries)
        average = total / len(salaries)
        return total, average

    except FileNotFoundError:
        print(f"Файл {path} не знайдено")
        return 0, 0.0


# Створюємо файл
create_developers_file("developers.txt")

# Використовуємо функцію для обробки даних
total, avg = total_salary("developers.txt")
print(f"Total: {total}, Average: {avg:.0f}")
