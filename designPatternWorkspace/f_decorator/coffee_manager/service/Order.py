from datetime import datetime

from service.OrderStatus import OrderStatus

class Order:
    
    def __init__(self, coffee, order_cnt):
        self.__coffee = coffee 
        self.__order_cnt = order_cnt
        self.__order_time = datetime.now()
        self.__order_price = coffee.get_price() * order_cnt
        self.__order_title = f'{coffee.get_name()} [{order_cnt}잔]'
        self.status = OrderStatus.PREPARE
        
    @staticmethod
    def create_order(coffee, order_cnt):
        order = Order(coffee, order_cnt)
        order.status = OrderStatus.check_order_status(order)        
        return order
    
    def execute(self):
        self.__coffee.offer(self.__order_cnt)
    
    def get_coffee(self):
        return self.__coffee

    def set_coffee(self, coffee):
        self.__coffee = coffee

    def get_order_cnt(self):
        return self.__order_cnt

    def set_order_cnt(self, order_cnt):
        self.__order_cnt = order_cnt

    def get_order_time(self):
        return self.__order_time

    def set_order_time(self, order_time):
        self.__order_time = order_time

    def get_order_price(self):
        return self.__order_price

    def set_order_price(self, order_price):
        self.__order_price = order_price

    def get_order_title(self):
        return self.__order_title

    def set_order_title(self, order_title):
        self.__order_title = order_title

    def __str__(self):
        return f"Order [coffee={self.__coffee}, orderCnt={self.__order_cnt}, orderTime={self.__order_time}, " \
               f"orderPrice={self.__order_price}, orderTitle={self.__order_title}]"