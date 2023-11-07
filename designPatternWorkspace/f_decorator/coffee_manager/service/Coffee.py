from service.Purchase import Purchase

class Coffee:
    def __init__(self, name, stock, sales_cnt, safety_stock, cost, price):
        self._name = name
        self._price = price
        self._cost = cost
        self._stock = stock
        self._safety_stock = safety_stock
        self._total_sales_cnt = sales_cnt
        
    def offer(self, order_cnt):
        # 제공해야하는 수량만큼 재고 차감
        self.__deduct_stock(order_cnt)
        
        # 누적판매량 추가
        self.__add_total_sales_cnt(order_cnt)
        
        # 재고가 안전재고 미만으로 내려가면 안전재고 확보
        if self.__stock < self.__safety_stock:
            self.__add_safety_stock()
    
    def add_stock(self, cnt):
        self.__add_stock(cnt)

    def __add_stock(self, cnt):
        self.__stock += cnt
    
    def __deduct_stock(self, order_cnt):
        self.__stock -= order_cnt
    
    def __add_total_sales_cnt(self, order_cnt):
        self.__total_sales_cnt += order_cnt
        
    def __add_safety_stock(self):
        print('[system:log] 재고가 부족해 안전재고를 확보합니다.')
        purchase = Purchase(self, self.__safety_stock * 2)
        
        if purchase.execute():
            print('[system:log] 안전재고 확보에 성공했습니다.')
        else:
            print('[system:log] 안전재고 확보에 실패했습니다.')
    
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_stock(self):
        return self.__stock

    def get_safety_stock(self):
        return self.__safety_stock


    def get_cost(self):
        return self.__cost

    def get_price(self):
        return self.__price

    def __str__(self):
        return (
            "Coffee [name="
            + self.__name
            + ", stock="
            + str(self.__stock)
            + ", totalSalesCnt="
            + str(self.__total_sales_cnt)
            + ", safetyStock="
            + str(self.__safety_stock)
            + ", cost="
            + str(self.__cost)
            + ", price="
            + str(self.__price)
            + "]"
        )