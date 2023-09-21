class Donation:
    total = 0 # 클래스 변수 총 기부금

    def __init__(self, num, name):
        self.__num = num
        self.__name = name
        self.add_donation()

    def add_donation(self):
        Donation.total += self.__num

    def show_donation_info(self):
        print('-----------------------------')
        print('성명 : ', self.__name)
        print('기부금 : ', self.__num)
        self.show_total_donation()
    
    def show_total_donation(self):
        print('총 기부금 : ', Donation.total)

p1 = Donation(10000, '홍길동')
p1.show_donation_info()

p2 = Donation(20000, '이몽룡')
p2.show_donation_info()

p3 = Donation(30000, '성춘향')
p3.show_donation_info()