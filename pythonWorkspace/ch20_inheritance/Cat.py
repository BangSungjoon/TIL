from Animal import *

class Cat(Animal): # Animal 클래스로부터 상속 받음
    # 메소드 오버라이딩
    def sound(self):
        # 부모 클래스의 sound() 호출
        super().sound()
        print('야옹')