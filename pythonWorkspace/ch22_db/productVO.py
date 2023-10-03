# 데이터 클래스
class productVO:
    def __init__(self, prdNo, prdName, prdPrice, prdMaker, prdColor, ctgNo):
        # 객체 생성하면서 초기화 
        # 현재 데이터가 모두 노출되어 있음
        # product 클래스 외부에서 접근 가능
        # 예 : productDAO 클래스에서 product 객체를 통해서 멤버변수 name에 접근 (product.prdName)

        # private으로 설정해서 데이터 보호(숨김 : 데이터 은닉)
        # private 변수는 외부에서 접근 불가
        # 같은 멤버 메소드인 getXXX()가 반환해주면 받아서 사용
        self.__prdNo = prdNo
        self.__prdName = prdName
        self.__prdMaker = prdMaker
        self.__prdPrice = prdPrice
        self.__prdColor = prdColor
        self.__ctgNo = ctgNo

    def get_prdNo(self):
        return self.__prdNo
    
    def get_prdName(self):
        return self.__prdName
    
    def get_prdMaker(self):
        return self.__prdMaker
    
    def get_prdPrice(self):
        return self.__prdPrice
    
    def get_prdColor(self):
        return self.__prdColor
    
    def get_ctgNo(self):
        return self.__ctgNo