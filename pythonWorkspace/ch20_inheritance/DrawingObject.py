# 추상 클래스 정의
from abc import *

class DrawingObject(metaclass=ABCMeta):
    def __init__(self):
        self.__pen_color = ''

    # 추상 메소드
    @abstractmethod
    def draw(self):
        pass