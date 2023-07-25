import csv
import json
import random
from typing import List, Dict, Union


def save_to_json(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        with open("results.json", "w") as jsonfile:
            json.dump({"args": args, "result": result}, jsonfile, indent=2)

        return result

    return wrapper


def equation_roots(a: Union[int, float], b: Union[int, float], c: Union[int, float]) -> List[Union[int, float]]:
    roots = []
    disc = b ** 2 - 4 * a * c
    roots.append((-b + disc ** 0.5) / (2 * a))
    roots.append((-b - disc ** 0.5) / (2 * a))
    return roots


def gen_rnd_num(file_path: str, num_rows: int) -> None:
    with open(file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        for _ in range(num_rows):
            row = [random.randint(1, 100) for _ in range(3)]
            csv_writer.writerow(row)


@save_to_json
def process_csv_data(file_path: str) -> Dict[str, List[str]]:
    results = {}
    with open(file_path, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            try:
                a, b, c = map(float, row)
                roots = equation_roots(a, b, c)
                roots_as_str = [str(root) for root in roots]
                results[f"{a}, {b}, {c}"] = roots_as_str
                print(f"For coefficients {a}, {b}, {c}, roots are: {roots}")
            except ValueError:
                print("Invalid input. Skipping row:", row)
    return results



file_p = "random_numbers.csv"
num_rows = 102
gen_rnd_num(file_p, num_rows)


process_csv_data(file_p)
