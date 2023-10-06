# 데이터 클래스
class Book:
    def __init__(self, bNo, bName, bAuthor, bPrice, bDate, bStock,pNo):
        # 객체 생성하면서 초기화 
        # self.bNo = bNo
        # self.bName = bName
        # self.bAuthor = bAuthor
        # self.bPrice = bPrice
        # self.bDate = bDate
        # self.bStock = bStock
        # self.pNo = pNo
        # 현재 데이터가 모두 노출되어 있음
        # Book 클래스 외부에서 접근 가능
        # 예 : BookDAO 클래스에서 book 객체를 통해서 멤버변수 name에 접근 (book.bName)

        # private으로 설정해서 데이터 보호(숨김 : 데이터 은닉)
        # private 변수는 외부에서 접근 불가
        # 같은 멤버 메소드인 getXXX()가 반환해주면 받아서 사용
        self.__bNo = bNo
        self.__bName = bName
        self.__bAuthor = bAuthor
        self.__bPrice = bPrice
        self.__bDate = bDate
        self.__bStock = bStock
        self.__pNo = pNo

    def get_bNo(self):
        return self.__bNo
    
    def get_bName(self):
        return self.__bName
    
    def get_bPrice(self):
        return self.__bPrice
    
    def get_bAuthor(self):
        return self.__bAuthor
    
    def get_bDate(self):
        return self.__bDate
    
    def get_bStock(self):
        return self.__bStock
    
    def get_pNo(self):
        return self.__pNo
    