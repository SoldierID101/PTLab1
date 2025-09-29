# -*- coding: utf-8 -*-
from src.QuartileCalculator import QuartileCalculator
from src.CalcRating import CalcRating
from src.Types import DataType


def test_second_quartile_students() -> None:
    # Дадим 4 студента, чтобы квартильные границы были корректны
    data: DataType = {
        "A": [("s1", 60), ("s2", 60)],   # среднее = 60
        "B": [("s1", 70), ("s2", 70)],   # среднее = 70  -> Q2
        "C": [("s1", 80), ("s2", 80)],   # среднее = 80  -> Q3
        "D": [("s1", 90), ("s2", 90)],   # среднее = 90  -> Q4
    }
    ratings = CalcRating(data).calc()
    q = QuartileCalculator(ratings)
    # Во вторую квартиль попадают значения (q1, q2] — здесь это только B
    assert q.second_quartile_students() == ["B"]
