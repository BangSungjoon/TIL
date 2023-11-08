from abc import ABCMeta, abstractmethod


class Developer(metaclass=ABCMeta):
    @abstractmethod
    def develop(self): pass