# 클래스 변수 : 모든 객체가 공용으로 사용하는 변수
# 클래스명.변수

class Calculation:
    total = 0 # 클래스 변수

    def __init__(self, num):
        self.__num = num
        self.add_to_total()

    # z클래스 변수 total에 인스턴스 변수의 __num 값 더하기
    def add_to_total(self):
        Calculation.total += self.__num

    def show(self):
        print('num : ', self.__num)
        print('total : ', Calculation.total)

c1 = Calculation(10)
c1.show()

c2 = Calculation(20)
c2.show()

print(Calculation.total)