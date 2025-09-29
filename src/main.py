# -*- coding: utf-8 -*-
import argparse
import sys
from CalcRating import CalcRating
from TextDataReader import TextDataReader
from YamlDataReader import YamlDataReader
from QuartileCalculator import QuartileCalculator


def get_path_from_arguments(args) -> tuple[str, bool]:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True, help="Path to datafile")
    parser.add_argument("--yaml", action="store_true", help="Use YAML reader")
    parsed = parser.parse_args(args)
    return parsed.path, parsed.yaml


def main() -> None:
    path, use_yaml = get_path_from_arguments(sys.argv[1:])

    reader = YamlDataReader() if use_yaml else TextDataReader()
    students = reader.read(path)
    print("Students:", students)

    rating = CalcRating(students).calc()
    print("Rating:", rating)

    # Вариант 8: вывести студентов второй квартиль
    q = QuartileCalculator(rating)
    print("2nd quartile students:", q.second_quartile_students())


if __name__ == "__main__":
    main()
