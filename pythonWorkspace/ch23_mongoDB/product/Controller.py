from ProductDAO import ProductDAO
from ProductVO import *

class Controller:
    def __init__(self):
        self.d = ProductDAO()

    def select(self):
        self.d.select()
    
    def insert(self):
        prdNo = input("상품번호 입력 : ")
        prdName = input("상품명 입력 : ")
        prdPrice = int(input("가격 입력 : "))
        prdMaker = input("제조회사 입력 : ")
        prdColor = input("상품색 입력 : ")
        ctgNo = int(input("카테고리번호 입력 : "))

        product = Product(prdNo, prdName, prdPrice, prdMaker, prdColor, ctgNo)
        self.d.insert(product)
    
    def update(self):
        prdNo = input("수정할 상품번호 입력 : ")
        prdName = input("상품명 입력 : ")
        prdPrice = int(input("가격 입력 : "))
        prdMaker = input("제조회사 입력 : ")
        prdColor = input("상품색 입력 : ")
        ctgNo = int(input("카테고리번호 입력 : "))
        
        product = Product(prdNo, prdName, prdPrice, prdMaker, prdColor, ctgNo)

        self.d.update(product)

    def delete(self):
        prdNo = input("삭제할 상품번호 입력 : ")

        self.d.delete(prdNo)
    
    def search(self):
        while True:
            sel = input("검색 종류 키워드 (상품명, 제조회사) : ")
            if sel == "상품명":
                prdName = input("검색할 상품명 입력 : ")
                values = {'field': 'prdName', 'value': prdName}
                break
            elif sel == "제조회사":
                prdMaker = input("검색할 제조회사 입력 : ")
                values = {'field': 'prdMaker', 'value': prdMaker}
                break
            else:
                print("잘못 입력하셨습니다.")

        self.d.search(values)