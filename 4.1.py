# TODO импортировать необходимые молули
import json
from csv import DictReader
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    lst = []
    with open(INPUT_FILENAME, 'r', newline="") as csv_file:
        rd = DictReader(csv_file)
        for rww in rd:
            lst.append(rww)
    with open(OUTPUT_FILENAME, 'w') as json_file:
        json.dump(obj=lst, fp=json_file, indent=4)




if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
