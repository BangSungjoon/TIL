import pymysql

# 실제 작업 처리하는 클래스 
class BookDAO:
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
        # 도서조회 
        # 도서정보출력 : select 문 수행

        # 1. DB 연결
        # 2. select 문 수행
        # 3. 결과 출력
        # 4. DB 접속 종료
        self.connect()
        sql = "select * from book"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()

        for re in result:
            for r in re:
                print(r, end=" ")
            print()

        self.disconnect()
        print("도서 정보 조회 완료")

    def insert(self, book):
         # 도서등록 
         # DB에 저장 : insert 문 수행
        
        # 1. DB 연결
        # 2. insert 문 수행
        # 3. DB 접속 종료
        try:
            self.connect()            
            sql = "insert into book (bookNo, bookName, bookAuthor, bookPrice, bookDate, bookStock, pubNo) values(%s, %s, %s, %s, %s, %s, %s)"
            values = (book.get_bNo(), book.get_bName(), book.get_bAuthor(), book.get_bPrice(), book.get_bDate(), book.get_bStock(), book.get_pNo())
            self.cursor.execute(sql, values)        
            self.conn.commit()
            print("도서 등록 완료")  
        except:
            print("insert error")
        
        self.disconnect()

    def update(self, book):
        # 도서수정
        # 수정된 데이터 DB 저장 : update 문 수행
        try:
            self.connect()            
            sql = "update book set bookName = %s, bookAuthor = %s, bookPrice = %s, bookDate = %s, bookStock = %s, pubNo = %s where bookNo = %s"
            values = (book.get_bName(), book.get_bAuthor(), book.get_bPrice(), book.get_bDate(), book.get_bStock(), book.get_pNo(), book.get_bNo())
            self.cursor.execute(sql, values)        
            self.conn.commit()
            
        except:
            print("update error")
        
        self.disconnect()  
        print("도서 정보 수정 완료") 

    def delete(self, bNo):
        # 도서삭제
        # DB에서 도서번호 해당되는 데이터 삭제 : delete 문 수행
        try:
            self.connect()            
            sql = "delete from book WHERE bookNo=%s"
            self.cursor.execute(sql, bNo)        
            self.conn.commit()
            
        except:
            print("delete error")
        
        self.disconnect()  
        print("도서 정보 삭제 완료") 
        print() 

    def search(self, bName):
        # 도서 검색하고 결과 출력
        try:
            self.connect()            
            sql = "select * from book WHERE bookName like '%" + bName + "%'"
            
            self.cursor.execute(sql)        
            result = self.cursor.fetchall()

            for re in result:
                for r in re:
                    print(r, end=' ')
                print()
            
        except:
            print("search error")

        self.disconnect()
        print('\n도서 검색 완료')