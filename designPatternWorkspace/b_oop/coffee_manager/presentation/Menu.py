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
        order_cnt = int(input(" * 판매량 : "))

        if input_code < 0 or input_code >= len(self.drinks):
            print("정확한 상품번호를 선택해 주세요.")
            return

        self.register_order(input_code, order_cnt)

    def register_order(self, input_code, order_cnt):
        order = Order.create_order(self.drinks[input_code], order_cnt)
        if order is None:
            print('주문량이 상품 재고보다 많습니다.')
            return
        
        payment = self.sales.take_order(order)
        

    def order_result(self, payment):
        order = payment.get_order()
        print(f"\n 제품명 : {order.get_coffee().get_name()}")
        print(f" 판매가 : {order.get_coffee().get_price()}")
        print(f" 판매수량 : {order.get_order_cnt()}")
        print(f" 결제금액 : {payment.get_pay_price()}")
        print(f" 남은 재고 : {order.get_coffee().get_stock()}")
        print(order)
