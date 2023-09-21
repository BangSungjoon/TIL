# 메소드 매개변수

class Person:
    def __init__(self, name, age): # 생성자
        # 생성자에 매개변수가 있다는 것은 
        # 인스턴스 변수 = 변수
        self.name = name
        self.age = age

    # 인스턴스 변수 값 설정 (변경)
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    # 인스턴스 변수 값 반환
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
# 인스턴스 생성
p1 = Person('홍길동', 20) # 객체 생성과 동시에 name, age 값 2개를 전달해야함
# 왜? : 생성자에 매개변수로 지정되어 있으므로
# 전달 안 하면 오류 발생
p2 = Person('이몽룡', 30)

print('이름 : ', p1.get_name(), ', 나이 : ', p1.get_age())
print('이름 : ', p2.get_name(), ', 나이 : ', p2.get_age())

# 인스턴스 변수의 값 변경 : setter 사용
p1.set_age(25)
p2.set_age(35)

print('이름 : ', p1.get_name(), ', 나이 : ', p1.get_age())
print('이름 : ', p2.get_name(), ', 나이 : ', p2.get_age())