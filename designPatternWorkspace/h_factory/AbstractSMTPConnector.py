from abc import ABCMeta, abstractmethod

class AbstractSMTPConnector(metaclass=ABCMeta):
    @abstractmethod
    def connect(self):
        pass