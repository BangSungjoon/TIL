from Line import *
from Circle import *
from Rect import *

line = Line()
line.draw()

circle = Circle()
circle.draw()

rect = Rect()
rect.draw()  # 오버라이딩 된 메소드 호출

# 추상 클래스는 인스턴스(객체) 생성 불가
# d = DrawingObject()
# TypeError: Can't instantiate abstract class DrawingObject with abstract method draw