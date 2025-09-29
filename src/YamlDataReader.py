# -*- coding: utf-8 -*-
from typing import Dict, List, Tuple
import yaml  # type: ignore
from Types import DataType
from DataReader import DataReader


class YamlDataReader(DataReader):
    """
    Ожидаемый формат YAML (список студентов):
    - Иванов Иван Иванович:
        математика: 67
        литература: 100
        программирование: 91
    - Петров Петр Петрович:
        математика: 78
        химия: 87
        социология: 61
    """

    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, "r", encoding="utf-8") as f:
            loaded = yaml.safe_load(f)

        # loaded — это список словарей { "ФИО": { "предмет": балл, ... } }
        self.students = {}
        if not isinstance(loaded, list):
            return self.students

        for item in loaded:
            if not isinstance(item, dict):
                continue
            for full_name, subjects in item.items():
                subj_list: List[Tuple[str, int]] = []
                if isinstance(subjects, dict):
                    for subj, score in subjects.items():
                        subj_list.append((str(subj), int(score)))
                self.students[str(full_name)] = subj_list

        return self.students
