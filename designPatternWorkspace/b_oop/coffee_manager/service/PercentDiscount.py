from service.Order import *
class PercentDiscount:

    @staticmethod
    def cal_discount(order):
        discount = 0
        if order.get_order_price() >= 10000:
            discount = int(order.get_order_price() * 0.1)

        return discount