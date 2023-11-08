from abc import ABCMeta, abstractmethod

class AbstractConnectionCreator(metaclass=ABCMeta):
    @abstractmethod
    def getConnection(self):pass    