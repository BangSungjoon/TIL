from service.Account import Account
from service.PercentDiscount import *

class Payment:
    def __init__(self, order):
        self.__order = order
        self.__pay_price = order.get_order_price()
        
    def execute(self):
        account = Account.get_instance()
        self.__pay_price -= PercentDiscount.cal_discount(self.__order)
        account.regist_sales(self.__pay_price)
        
    def get_order(self):
        return self.__order

    def set_order(self, order):
        self.__order = order

    def get_pay_price(self):
        return self.__pay_price

    def set_pay_price(self, pay_price):
        self.__pay_price = pay_price