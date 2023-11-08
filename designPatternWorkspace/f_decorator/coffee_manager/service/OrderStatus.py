from enum import Enum

from service.SeasonCoffee import SeasonCoffee

class OrderStatus(Enum):
    PREPARE = (-1, '주문 생성을 준비중입니다.')
    OK = (0, '주문 생성 성공')
    FAIL_CAUSE_SOLDOUT = (1, '품절로 인한 주문 실패')
    FAIL_CAUSE_SEASON = (2, '시즌 상품은 비시즌에 주문이 불가능합니다')
    END = (4, '주문 완료')
    
    def __init__(self, code, desc):
        self.code = code
        self.desc = desc
    
    @staticmethod
    def check_order_status(order):
        coffee = order.get_coffee()
        order_cnt = order.get_order_cnt()
        
        if order_cnt > coffee.get_stock():
            return OrderStatus.FAIL_CAUSE_SOLDOUT
        
        if isinstance(coffee.get_origin(), SeasonCoffee) \
                and not coffee.get_origin().is_season():
            return OrderStatus.FAIL_CAUSE_SEASON
        
        return OrderStatus.OK
        
    def is_ok(self):
        return self == OrderStatus.OK
    
    def is_end(self):
        return self == OrderStatus.END
    
    def is_fail(self):
        return self in [OrderStatus.FAIL_CAUSE_SEASON
                        , OrderStatus.FAIL_CAUSE_SOLDOUT]