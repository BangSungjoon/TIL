from service.Account import Account


class Purchase:
    def __init__(self, coffee, purchase_cnt):
        self.__coffee = coffee
        self.__purchase_cnt = purchase_cnt
        self.__budget = coffee.get_cost() * purchase_cnt
        
    def execute(self):
        account = Account.get_instance()
        if account.regist_expences(self.__budget):
            self.__coffee.add_stock(self.__purchase_cnt)
            return True

        return False
        