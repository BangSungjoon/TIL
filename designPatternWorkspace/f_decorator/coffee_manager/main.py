from service.SeasonCoffee import SeasonCoffee
from service.Coffee import *
from service.Sales import *
from presentation.Menu import *

def main():
    drinks = [
        Coffee("아메리카노", 10, 0, 3, 2000, 3000),
        Coffee("모카", 10, 0, 3, 3000, 4000),
        Coffee("라떼", 10, 0, 3, 4000, 5000),
        SeasonCoffee('프라푸치노',10,0,3,5000,6000,[6,7,8,9])
    ]

    Menu(Sales(), drinks).main_menu()

if __name__ == "__main__":
    main()