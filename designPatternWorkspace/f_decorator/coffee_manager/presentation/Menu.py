from service.ChocoDecorator import ChocoDecorator
from service.ShotDecorator import ShotDecorator
from service.Account import *
from service.Coffee import *
from service.Order import *
from service.Payment import *
from service.Sales import *

class Menu:
    def __init__(self, sales, drinks):
        self.account = Account()
        self.sales = sales
        self.drinks = drinks

    def main_menu(self):
        while True:
            print("\n=========Menu=========")
            print("판매등록(1)")
            print("현황(2)")
            print("종료(3)")
            input_menu = int(input("입력 : "))

            if input_menu == 1:
                self.coffee_menu()
            elif input_menu == 2:
                self.statistics()
            elif input_menu == 3:
                print(" * 종료합니다.")
                return
            else:
                print(" * 잘못된 번호를 입력하셨습니다.")

    def statistics(self):
        print("\n=========statistics========= ")
        for drink in self.drinks:
            print(
                f"{drink.get_name()} | 재고 : {drink.get_stock()} | 판매량 : {drink.get_total_sales_cnt()}"
            )

        print(
            f"잔고 : {self.account.get_balance()} | 매출 : {self.account.get_sales_volumn()} | 지출 : {self.account.get_expenses()}"
        )

    def coffee_menu(self):
        print("\n=========List========= ")
        for i, drink in enumerate(self.drinks):
            print(f"{drink.get_name()} ({i})")

        input_code = int(input("\n * 판매한 커피코드 : "))
        toppings = self.add_topping()
        order_cnt = int(input(" * 판매량 : "))

        if input_code < 0 or input_code >= len(self.drinks):
            print("정확한 상품번호를 선택해 주세요.")
            return

        self.register_order(input_code, toppings, order_cnt)

    def add_topping(self):
        toppings = []
        while True:
            print("\n * 추가할 옵션 : ")
            print(" * 0. 자바칩 추가")
            print(" * 1. 샷 추가")
            print(" * 2. 토핑 추가 완료")
            print(" 입력 : " , end="")
            
            input_option = int(input())
            
            if input_option < 0 or input_option > 2 :
                print(' *  옵션을 잘못 선택하셨습니다.')
                continue
            
            if input_option == 2:
                break      
        
            toppings.append(input_option)
            
        return toppings

    def register_order(self, input_code, toppings, order_cnt):
        coffee = self.drinks[input_code]
        decors = {0:ChocoDecorator, 1:ShotDecorator}

        for i in toppings:
            coffee = decors.get(i)(coffee)
        
        order = Order.create_order(coffee, order_cnt)
        if order.status.is_fail():
            print(order.status.desc)
            return
        
        payment = self.sales.take_order(order)
        self.order_result(payment)
        

    def order_result(self, payment):
        order = payment.get_order()
        print(f"\n 제품명 : {order.get_coffee().get_name()}")
        print(f" 판매가 : {order.get_coffee().get_price()}")
        print(f" 판매수량 : {order.get_order_cnt()}")
        print(f" 결제금액 : {payment.get_pay_price()}")
        print(f" 남은 재고 : {order.get_coffee().get_stock()}")
        print(order)
