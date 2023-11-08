from service.ToppingDecorator import ToppingDecorator

class ChocoDecorator(ToppingDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)
        self.__coffee = coffee
        self.__topping_price = 500
    
    def get_price(self):
        return self.__coffee.get_price() + self.__topping_price
    
    def get_name(self):
        return self.__coffee.get_name() + '[choco]'
    
    def __str__(self):
        return self.get_name()