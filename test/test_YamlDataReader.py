# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.YamlDataReader import YamlDataReader


class TestYamlDataReader:
    @pytest.fixture()
    def yaml_text_and_data(self) -> tuple[str, DataType]:
        yaml_text = (
            "- Иванов Иван Иванович:\n"
            "    математика: 67\n"
            "    литература: 100\n"
            "    программирование: 91\n"
            "- Петров Петр Петрович:\n"
            "    математика: 78\n"
            "    химия: 87\n"
            "    социология: 61\n"
        )
        expected: DataType = {
            "Иванов Иван Иванович": [
                ("математика", 67),
                ("литература", 100),
                ("программирование", 91),
            ],
            "Петров Петр Петрович": [
                ("математика", 78),
                ("химия", 87),
                ("социология", 61),
            ],
        }
        return yaml_text, expected

    @pytest.fixture()
    def filepath_and_data(
        self,
        yaml_text_and_data: tuple[str, DataType],
        tmpdir
    ) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("students.yaml")
        p.write_text(yaml_text_and_data[0], encoding="utf-8")
        return str(p), yaml_text_and_data[1]

    def test_read_yaml(
        self,
        filepath_and_data: tuple[str, DataType]
    ) -> None:
        content = YamlDataReader().read(filepath_and_data[0])
        assert content == filepath_and_data[1]
