# Controller 클래스 
# 메뉴에서 선택한 항목에 따라 메소드 수행 
from BookDAO import BookDAO
from BookVO import Book

class Controller:
    def __init__(self):
        self.dao = BookDAO()

    def select(self):
        # 도서조회 
        # DAO 클래스의 select() 호출(DAO : 도서정보출력)
        print("\n컨트롤러의 select") 
        self.dao.select()

    def insert(self):
         # 도서등록 
         # 데이터 입력 
         # DAO 클래스의 insert() 호출하면서 데이터 전달(DAO : DB에 저장)
        print("컨트롤러의 insert") 

        bNo = input("도서 번호: ")
        bName = input("도서명: ")
        bAuthor = input("저자: ")
        bPrice = input("가격: ")
        bDate = input("날짜(1990-01-01): ")
        bStock = input("재고: ")
        pNo = input("출판사번호: ")

        # 입력한 값으로 Book 객체 초기화
        book = Book(bNo, bName, bAuthor, bPrice, bDate, bStock, pNo)
        self.dao.insert(book) # Book 객체 전달


    def update(self):
        # 도서수정
        # 수정할 데이터 입력 
        # DAO 클래스의 update() 호출하면서 데이터 전달(DAO : 수정된 데이터 DB 저장)
        print("컨트롤러의 update") 
        print("수정할 도서정보 입력 ") 
        
        bNo = input("도서 번호: ")
        bName = input("도서명: ")
        bAuthor = input("저자: ")
        bPrice = input("가격: ")
        bDate = input("날짜(1990-01-01): ")
        bStock = input("재고: ")
        pNo = input("출판사번호: ")

        book = Book(bNo, bName, bAuthor, bPrice, bDate, bStock, pNo)        
        self.dao.update(book)

    def delete(self):
        # 도서삭제
        # 삭제할 도서번호 입력 
        # DAO 클래스의 delete() 호출하면서 도서번호 전달(DAO : DB에서 도서번호 해당되는 데이터 삭제)
        print("컨트롤러의 delete")
        bNo = input('삭제할 도서 번호 입력 : ')
        self.dao.delete(bNo)

    def search(self):
        # 도서 검색하고 결과 출력
        # 검색할 도서명 입력 
        # DAO 클래스의 search() 호출하면서 도서명 전달(DAO : DB에서 도서명 해당되는 데이터 검색)
        print("컨트롤러의 search")
        bName = input('검색할 도서명 : ')
        self.dao.search(bName)