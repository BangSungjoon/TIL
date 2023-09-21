# 생성자를 포함하는 클래스 정의
 
class Rectangle:
    # 생성자 : 객체 생성 시 자동 호출됨
    # 기능 : 인스턴스 변수를 초기화하는 역할
    def __init__(self):
        self.width = 0
        self.height = 0

    # 가로길이, 세로길이 입력 받아서 인스턴스 변수에 값 저장하는 메소드
    def input(self):
        self.width = int(input('가로 길이 입력 : '))
        self.height = int(input('세로 길이 입력 : '))

    # 사각형의 정보를 출력하는 메소드
    def show_rect_info(self):
        print('--------------------------------')
        print('가로 길이 : ', self.width)
        print('세로 길이 : ', self.height)
        print('면적 : ', self.width * self.height)

r = Rectangle() # 객체 생성 시 생성자 자동 호출. 변수값 초기화
r.input()
r.show_rect_info()