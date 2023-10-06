from ProductDAO import ProductDAO
from ProductVO import *

class Controller:
    def __init__(self):
        self.d = ProductDAO()

    def select(self):
        self.d.select()
    
    def insert(self):
        pNo = input("상품번호 입력 : ")
        pName = input("상품명 입력 : ")
        pPrice = input("가격 입력 : ")
        pMaker = input("상표 입력 : ")
        pColor = input("상품색 입력 : ")
        cNo = input("카테고리번호 입력 : ")
        product = Product(pNo, pName, pPrice, pMaker, pColor, cNo)

        self.d.insert(product)
    
    def update(self):
        pNo = input("수정할 상품번호 입력 : ")
        pName = input("상품명 입력 : ")
        pPrice = input("가격 입력 : ")
        pMaker = input("상표 입력 : ")
        pColor = input("상품색 입력 : ")
        cNo = input("카테고리번호 입력 : ")
        
        product = Product(pNo, pName, pPrice, pMaker, pColor, cNo)

        self.d.update(product)

    def delete(self):
        pNo = input("삭제할 상품번호 입력 : ")

        self.d.delete(pNo)
    
    def search(self):
        while True:
            sel = input("검색 종류 키워드 (상품명, 제조회사) : ")
            if sel == "상품명":
                pName = input("검색할 상품명 입력 : ")
                values = ('prdName', pName)
                break
            elif sel == "제조회사":
                pMaker = input("검색할 제조회사 입력 : ")
                values = ('prdMaker', pMaker)
                break
            else:
                print("잘못 입력하셨습니다.")

        self.d.search(values)