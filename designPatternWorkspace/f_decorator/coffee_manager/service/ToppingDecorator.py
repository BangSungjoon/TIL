from service.Coffee import Coffee

class ToppingDecorator(Coffee):
    def __init__(self, coffee):
        super().__init__(
            coffee._name
            , coffee._price
            , coffee._cost
            , coffee._stock
            , coffee._safety_stock
            , coffee._total_sales_cnt)
        
        self.__coffee = coffee
        
    def get_origin(self):
        if isinstance(self.__coffee, ToppingDecorator):
            return self.__coffee.get_origin()
        else : 
            return self.__coffee
        
    def offer(self, order_cnt):
        self.__coffee.offer(order_cnt)
        
    def add_stock(self, cnt):
        self.__coffee.add_stock(cnt)
    
    def get_stock(self):
        return self.__coffee.get_stock()

    def get_total_sales_cnt(self):
        return self.__coffee.get_total_sales_cnt()