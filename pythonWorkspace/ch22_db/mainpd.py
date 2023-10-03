from controllerpd import controllerpd

class Main:
    def __init__(self):
        self.c = controllerpd()

    def start(self):
        print()
        # 메뉴 출력
        # 1.전체제품조회 2.제품등록 3.제품수정 4.제품삭제 5.검색 6.종료
        # 선택한 번호에 따라 controllerpd 클래스가 메소드 호출

        while True:
            num = input("\n1.전체제품조회 2.제품등록 3.제품수정 4.제품삭제 5.검색 6.종료 : ")

            if num == '1':
               # 컨트롤러 클래스의 select() 호출
               self.c.select()
            elif num == '2':
                # 컨트롤러 클래스의 insert() 호출
                self.c.insert()
            elif num == '3':
                # 컨트롤러 클래스의 insert() 호출
                self.c.update()
            elif num == '4':
                # 컨트롤러 클래스의 insert() 호출
                self.c.delete()
            elif num == '5':
                # 컨트롤러 클래스의 insert() 호출
                self.c.search()
            elif num == '6':
                # 컨트롤러 클래스의 insert() 호출
                print("종료합니다") 
                break
            else:
                print("잘못 입력하였습니다")  

# 현재 모듈이 시작 모듈 
if __name__ == "__main__": # 스크립트 파일이 메인 프로그램으로 사용될 때와 모듈로 사용될 때를 구분하기 위한 용도
    print("메인입니다")
    # start() 메소드 실행하면서 시작
    main = Main()
    main.start()