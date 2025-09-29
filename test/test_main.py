# -*- coding: utf-8 -*-
from src.main import get_path_from_arguments
import pytest


@pytest.fixture()
def correct_arguments_string() -> tuple[list[str], tuple[str, bool]]:
    return ["-p", "/home/user/file.txt"], ("/home/user/file.txt", False)


@pytest.fixture()
def noncorrect_arguments_string() -> list[str]:
    return ["/home/user/file.txt"]


def test_get_path_from_correct_arguments(
    correct_arguments_string: tuple[list[str], tuple[str, bool]]
) -> None:
    path, is_yaml = get_path_from_arguments(correct_arguments_string[0])
    assert (path, is_yaml) == correct_arguments_string[1]


def test_get_path_from_noncorrect_arguments(
    noncorrect_arguments_string: list[str]
) -> None:
    with pytest.raises(SystemExit) as e:
        get_path_from_arguments(noncorrect_arguments_string[0])
    assert e.type == SystemExit
