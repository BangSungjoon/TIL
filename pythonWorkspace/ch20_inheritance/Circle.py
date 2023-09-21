from DrawingObject import *

class Circle(DrawingObject):
    def __init__(self):
        self.__pen_color = 'blue'

    # 추상 메소드 오버라이딩
    def draw(self):
        print(f'{self.__pen_color} 색상으로 원 그리기')