# -*- coding: utf-8 -*-
from typing import Dict, List
from statistics import quantiles


class QuartileCalculator:
    """
    Принимает на вход словарь { ФИО: рейтинг } и позволяет получить студентов,
    попавших в заданную квартиль. Для 2-й квартиль используем правило:
    q1 < rating <= q2 (верхняя граница включительно).
    """

    def __init__(self, ratings: Dict[str, float]) -> None:
        self.ratings = ratings

    def second_quartile_students(self) -> List[str]:
        values = list(self.ratings.values())
        if not values:
            return []

        # Получим границы квартилей (Q1, Q2, Q3)
        q1, q2, _q3 = quantiles(values, n=4, method="inclusive")

        return sorted(
            [name for name, r in self.ratings.items() if (r > q1 and r <= q2)]
        )
