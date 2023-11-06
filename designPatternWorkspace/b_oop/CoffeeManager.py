from datetime import datetime

class Coffee:
    def __init__(self, name, price, cost, stock, safety_stock, sales_cnt):
        self.name = name
        self.price = price
        self.cost = cost
        self.stock = stock
        self.safety_stock = safety_stock
        self.sales_cnt = sales_cnt


def main():
    balance = 100000  # 잔고 100000
    sales_price = 0  # 매출
    expenses = 0  # 지출

    americano = Coffee("아메리카노", 3000, 2000, 10, 3, 0)  # 인스턴스화
    moca = Coffee("모카", 4000, 3000, 10, 3, 0)
    latte = Coffee("라떼", 5000, 4000, 10, 3, 0)
    
    # 만약 시즌 음료가 11종류이고 11종류마다 시즌기간이 다 다르다면 어떻게 확장할까
    drinks = [americano, moca, latte]

    while True:
        print("\n=========Menu=========")
        print("판매등록(1)")
        print("현황(2)")
        print("종료(3)")
        input_menu = int(input("입력 : "))

        if input_menu == 1:
            # 음료 메뉴판
            for i, drink in enumerate(drinks):
                print(f"{drink.name}({i})")

            input_code = int(input("\n * 판매한 커피코드 : "))
            order_cnt = int(input(" * 판매량 : "))

            if input_code < 0 or input_code >= len(drinks):
                print("정확한 상품번호를 선택해 주세요.")
                continue
            
            if order_cnt > drinks[input_code].stock:
                # 주문량이 재고보다 많으면 주문을 취소한다.
                print("재고가 부족해 주문을 취소합니다.")
                continue
            

            # 주문량이 재고보다 적거나 같으면 판매 수량만큼 재고를 차감하고,
            # 잔고에 판매 금액을 반영한다.
            drinks[input_code].stock -= order_cnt
            balance += drinks[input_code].price * order_cnt
            sales_price += drinks[input_code].price * order_cnt
            drinks[input_code].sales_cnt += order_cnt

            # 커피 재고가 안전재고 미만이 되면 안전재고의 두 배 만큼 매입한다.
            if drinks[input_code].stock < drinks[input_code].safety_stock:
                if balance > drinks[input_code].safety_stock * 2 * drinks[input_code].cost:
                    drinks[input_code].stock += drinks[input_code].safety_stock * 2
                    balance -= drinks[input_code].safety_stock * 2 * drinks[input_code].cost
                    # 지출등록
                    expenses += drinks[input_code].safety_stock * 2 * drinks[input_code].cost
                    print(" [system:log] 안전재고를 확보하였습니다.")
                else:
                    # 잔고가 부족해 매입이 불가능하면 안전재고 매입을 취소한다.
                    print(" [system:log] 잔고가 부족해 안전재고 확보에 실패하였습니다.")

            print("\n 제품명 : 아메리카노")
            print(" 판매가 :", drinks[input_code].price)
            print(" 판매수량 :", order_cnt)
            print(" 결제금액 :", drinks[input_code].price * order_cnt)
            print(" 남은 재고 :", drinks[input_code].stock)

        elif input_menu == 2:
            for drink in drinks:
                print(f"{drink.name} | 재고 : {drink.stock} | 판매량 : {drink.sales_cnt}")

            print("잔고 :", balance, "| 매출 :", sales_price, "| 지출 :", expenses)

        elif input_menu == 3:
            print("프로그램을 종료합니다.")
            break

        else:
            print("알맞은 번호를 입력하세요.")

if __name__ == "__main__":
    main()