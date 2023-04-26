from abc import ABC
from abc import abstractmethod


class Step(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def process(self, data, inputs):  # inputs 可用 dictionary 的方式打包參數
        pass


class StepException(Exception):  # Exception 為 python 内建的 method
    pass
