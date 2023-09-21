class Calculator:
    # 생성자 : 객체 생성 시 자동 호출됨
    # 기능 : 인스턴스 변수를 초기화하는 역할
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def input(self):
        self.num1 = int(input('숫자1 입력 : '))
        self.num2 = int(input('숫자2 입력 : '))

    def add(self):
        print('덧셈 : ', self.num1 + self.num2)
    
    def multiply(self):
        print('곱셈 : ', self.num1 * self.num2)

r = Calculator()
r.input()
r.add()
r.multiply()