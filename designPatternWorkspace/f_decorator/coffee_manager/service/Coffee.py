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
        if self._stock < self._safety_stock:
            self.__add_safety_stock()
    
    def add_stock(self, cnt):
        self.__add_stock(cnt)

    def __add_stock(self, cnt):
        self._stock += cnt
    
    def __deduct_stock(self, order_cnt):
        self._stock -= order_cnt
    
    def __add_total_sales_cnt(self, order_cnt):
        self._total_sales_cnt += order_cnt
        
    def __add_safety_stock(self):
        print('[system:log] 재고가 부족해 안전재고를 확보합니다.')
        purchase = Purchase(self, self._safety_stock * 2)
        
        if purchase.execute():
            print('[system:log] 안전재고 확보에 성공했습니다.')
        else:
            print('[system:log] 안전재고 확보에 실패했습니다.')
    
    def get_name(self):
        return self._name

    def get_stock(self):
        return self._stock

    def get_total_sales_cnt(self):
        return self._total_sales_cnt

    def get_safety_stock(self):
        return self._safety_stock

    def get_cost(self):
        return self._cost

    def get_price(self):
        return self._price

    def __str__(self):
        return (
            "Coffee [name="
            + self._name
            + ", stock="
            + str(self._stock)
            + ", totalSalesCnt="
            + str(self._total_sales_cnt)
            + ", safetyStock="
            + str(self._safety_stock)
            + ", cost="
            + str(self._cost)
            + ", price="
            + str(self._price)
            + "]"
        )