# -*- coding: utf-8 -*-
from Types import DataType
from abc import ABC, abstractmethod

#Новый коментарий !!!!reader
class DataReader(ABC):

    @abstractmethod
    def read(self, path: str) -> DataType:
        pass
