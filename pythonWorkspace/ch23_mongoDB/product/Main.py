from Controller import Controller

class Main:
    def __init__(self):
        self.c = Controller()

    def start(self):
         while True:
            num = input("1. 상품조회 2. 상품등록 3. 상품수정 4. 상품삭제 5. 상품검색 6. 종료 : ")

            if num == '1':
                self.c.select()

            elif num == '2':
                self.c.insert()

            elif num == '3':
                self.c.update()

            elif num == '4':
                self.c.delete()

            elif num == '5':
                self.c.search()

            elif num == '6':
                print("종료합니다.")
                break
            else:
                print("잘못 입력하였습니다.")

if __name__ == "__main__":
    main = Main()
    main.start()