class Book:
    nation = 'Korea'

    def __init__(self, no, name, author, money, amount, com):
        self.__no = no
        self.__name = name
        self.__author = author
        self.__money = money
        self.__amount = amount
        self.__com = com

    def show_book_info(self):
        print('도서번호 : ', self.__no)
        print('도서명 : ', self.__name)
        print('저자 : ', self.__author)
        print('출간된 나라 : ', Book.nation)
        print()