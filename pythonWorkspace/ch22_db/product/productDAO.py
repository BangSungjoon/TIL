import pymysql

# 실제 작업 처리하는 클래스 
class productDAO:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self):
        # DB 연결 
        self.conn = pymysql.connect(host='localhost', 
                                port=3306, 
                                db='sqldb4',
                                user='root', 
                                passwd='1234',
                                charset='utf8')
        self.cursor = self.conn.cursor()

    def disconnect(self):
        # DB 접속 종료
        self.cursor.close()
        self.conn.close()

    def select(self):
        # 제품조회 
        # 제품정보출력 : select 문 수행

        # 1. DB 연결
        # 2. select 문 수행
        # 3. 결과 출력
        # 4. DB 접속 종료
        self.connect()
        sql = "select * from product"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()

        for re in result:
            for r in re:
                print(r, end=" ")
            print()

        self.disconnect()
        print("제품 정보 조회 완료")

    def insert(self, product):
         # 제품등록 
         # DB에 저장 : insert 문 수행
        
        # 1. DB 연결
        # 2. insert 문 수행
        # 3. DB 접속 종료
        try:
            self.connect()            
            sql = "insert into product (prdNo, prdName, prdPrice, prdMaker, prdColor, ctgNo) values(%s, %s, %s, %s, %s, %s)"
            values = (product.get_prdNo(), product.get_prdName(), product.get_prdPrice(), product.get_prdMaker(), product.get_prdColor(), product.get_ctgNo())
            self.cursor.execute(sql, values)        
            self.conn.commit()
            print("제품 등록 완료")  
        except:
            print("insert error")
        
        self.disconnect()

    def update(self, product):
        # 제품수정
        # 수정된 데이터 DB 저장 : update 문 수행
        try:
            self.connect()            
            sql = "update product set prdName = %s, prdPrice = %s, prdMaker = %s, prdColor = %s, ctgNo = %s where prdNo = %s"
            values = (product.get_prdName(), product.get_prdPrice(), product.get_prdMaker(), product.get_prdColor(), product.get_ctgNo(), product.get_prdNo())
            self.cursor.execute(sql, values)        
            self.conn.commit()
            
        except:
            print("update error")
        
        self.disconnect()  
        print("제품 정보 수정 완료") 

    def delete(self, prdNo):
        # 제품 정보 삭제
        # DB에서 제품번호 해당되는 데이터 삭제 : delete 문 수행
        try:
            self.connect()            
            sql = "delete from product WHERE prdNo=%s"
            self.cursor.execute(sql, prdNo)        
            self.conn.commit()
            
        except:
            print("delete error")
        
        self.disconnect()  
        print("제품 정보 삭제 완료") 
        print() 

    def search(self, prdName):
        # 제품 검색하고 결과 출력
        try:
            self.connect()            
            sql = "select * from product WHERE prdName like '%" + prdName + "%'"
            
            self.cursor.execute(sql)        
            result = self.cursor.fetchall()

            for re in result:
                for r in re:
                    print(r, end=' ')
                print()
            
        except:
            print("search error")

        self.disconnect()
        print('\n제품 검색 완료')