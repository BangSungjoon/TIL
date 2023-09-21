from Cat import *

c = Cat()
c.show()
c.sound() # 자식 클래스에서 오버라이딩된 sound가 나온다

print(Cat.mro())
# [<class 'Cat.Cat'>, <class 'Animal.Animal'>, <class 'object'>]
# 내 클래스, 부모 클래스, 최상위 클래스 object