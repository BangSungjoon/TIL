# controllerpd 클래스 
# 메뉴에서 선택한 항목에 따라 메소드 수행 
from productDAO import productDAO
from productVO import productVO

class controllerpd:
    def __init__(self):
        self.dao = productDAO()

    def select(self):
        # 제품조회 
        # DAO 클래스의 select() 호출(DAO : 제품정보출력)
        print("\n컨트롤러의 select") 
        self.dao.select()

    def insert(self):
         # 제품등록 
         # 데이터 입력 
         # DAO 클래스의 insert() 호출하면서 데이터 전달(DAO : DB에 저장)
        print("컨트롤러의 insert") 

        prdNo = input("제품 번호: ")
        prdName = input("제품명: ")
        prdPrice = input("가격: ")
        prdMaker = input('제조회사: ')
        prdColor = input("제품 색상: ")
        ctgNo = input("카테고리 번호: ")

        # 입력한 값으로 product 객체 초기화
        product = productVO(prdNo, prdName, prdPrice, prdMaker, prdColor, ctgNo)
        self.dao.insert(product) # product 객체 전달


    def update(self):
        # 제품 정보 수정
        # 수정할 데이터 입력 
        # DAO 클래스의 update() 호출하면서 데이터 전달(DAO : 수정된 데이터 DB 저장)
        print("컨트롤러의 update") 
        print("수정할 제품정보 입력 ") 
        
        prdNo = input("제품 번호: ")
        prdName = input("제품명: ")
        prdPrice = input('제품 가격: ')
        prdMaker = input("제조회사: ")
        prdColor = input("제품 색상: ")
        ctgNo = input("카테고리 번호: ")

        product = productVO(prdNo, prdName, prdPrice, prdMaker, prdColor, ctgNo)        
        self.dao.update(product)

    def delete(self):
        # 제품 삭제
        # 삭제할 제품번호 입력 
        # DAO 클래스의 delete() 호출하면서 제품번호 전달(DAO : DB에서 도서번호 해당되는 데이터 삭제)
        print("컨트롤러의 delete")
        prdNo = input('삭제할 제품 번호 입력 : ')
        self.dao.delete(prdNo)

    def search(self):
        # 제품 검색하고 결과 출력
        # 검색할 제품명 입력 
        # DAO 클래스의 search() 호출하면서 제품명 전달(DAO : DB에서 제품명 해당되는 데이터 검색)
        print("컨트롤러의 search")
        prdName = input('검색할 제품명 : ')
        self.dao.search(prdName)