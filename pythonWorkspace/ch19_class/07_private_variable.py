class BankAccount:
    def __init__(self):
        self.__balance = 0 # private 변수 : 숨겨짐
        self.__input = 0
        self.__output = 0

    def show_balance(self):
        print('현재 잔액은 ', self.__balance)

    def deposit(self):
        inputmoney = int(input('예금액 입력 : ')) # 지역변수로 사용가능
        self.__balance += inputmoney

    def withdraw(self):
        output = int(input('출금액 입력 : '))
        if self.__balance - output >= 0:
            print('현재 잔액은 ', self.__balance - output)
        else:
            print('잔액이 부족합니다')
            print('현재 잔액은 ', self.__balance)

money = BankAccount()
money.show_balance()
money.deposit()
money.withdraw()