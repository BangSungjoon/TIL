from DrawingObject import *

class Line(DrawingObject):
    def __init__(self):
        self.__pen_color = 'red'

    # 추상 메소드 오버라이딩
    def draw(self):
        print(f'{self.__pen_color} 색상으로 선 그리기')