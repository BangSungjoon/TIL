from ProductVO import *
import pymysql
class ProductDAO:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234')
        self.cursor = self.conn.cursor()
        sql = "USE sqldb4"
        self.cursor.execute(sql)
    
    def disconnect(self):
        self.cursor.close()
        self.conn.close()

    def select(self):
        try:
            self.connect()
            sql = "SELECT * FROM product"
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            print("상품 정보 조회 완료")
        except:
            print("selece error")
        
        for row in result:
            for col in row:
                print(col, end = ' ')
            print()

        self.disconnect()
    
    def insert(self, product):

        self.connect()            
        sql = "INSERT INTO product (prdNo, prdName, prdPrice, prdMaker, prdColor, ctgNo) VALUES(%s, %s, %s, %s, %s, %s)"
        values = (product.get_pNo(), product.get_pName(), product.get_pPrice(), product.get_pMaker(), product.get_pColor(), product.get_cNo())
        self.cursor.execute(sql, values)        
        self.conn.commit()
        print("상품 등록 완료")


        self.disconnect()

    def update(self, product):
        try:
            self.connect()
            self.connect()            
            sql = "UPDATE product SET prdName = %s, prdPrice = %s, prdMaker = %s, prdColor = %s, ctgNo = %s where prdNo = %s"
            values = (product.get_pName(), product.get_pPrice(), product.get_pMaker(), product.get_pColor(), product.get_cNo(), product.get_pNo())
            self.cursor.execute(sql, values)        
            self.conn.commit()
            print("상품 정보 수정 완료")
        except:
            print("update error")

        self.disconnect()

    def delete(self, pNo):
        try:
            self.connect()
            sql = "DELETE FROM product WHERE prdNo =" + pNo
            self.cursor.execute(sql)
            self.conn.commit()
            print("상품 정보 삭제 완료")
        except:
            print("delete error")

        self.disconnect()
    
    def search(self, values):
        try:
            self.connect()
            keyword_column = values[0]
            keyword_value = values[1]
            keyword_value = f"%{keyword_value}%"
            sql = f"SELECT * FROM product WHERE {keyword_column} LIKE %s"
            self.cursor.execute(sql, (keyword_value,))
            result = self.cursor.fetchall()
            print("상품 정보 검색 완료")
            for row in result:
                for col in row:
                    print(col, end=' ')
                print()
        except Exception:
            print("search error")

        self.disconnect()