class Car:
    def set_car(self): # 메소드의 첫 번째 매개변수는 반드시 self로 지정
        self.num = '01가1234'
        self.index = '아반떼'
        self.co = '현대'
        self.age = 2023
        self.amount = 1600

    def show_car_info(self):
        print(f'차량 번호 : {self.num}')
        print(f'차종 : {self.index}')
        print(f'제조사 : {self.co}')
        print(f'연식 : {self.age}')
        print(f'배기량 : {self.amount}')

car1 = Car() # 객체 생성
car1.set_car()
car1.show_car_info()