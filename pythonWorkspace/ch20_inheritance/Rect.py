from DrawingObject import *

class Rect(DrawingObject):
    def __init__(self):
        self.__pen_color = 'green'

    # 추상 메소드 오버라이딩
    def draw(self):
        print(f'{self.__pen_color} 색상으로 사각형 그리기')