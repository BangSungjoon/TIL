from pymongo import MongoClient
from datetime import datetime

# 실제 작업 처리하는 클래스 
class BookDAO:
    def __init__(self):
        self.conn = None
        self.db = None

    def connect(self):
        # DB 연결 
        self.conn = MongoClient(host='localhost' , port=27017)
        self.db = self.conn.new_db

    def disconnect(self):
        # DB 접속 종료
        self.conn.close()

    def select(self):
        # 도서조회 
        # 도서정보출력 : select 문 수행

        # 1. DB 연결
        # 2. select 문 수행
        # 3. 결과 출력
        # 4. DB 접속 종료
        self.connect()
        result = self.db.book.find()

        for book in result:
            print(
            f"{book['bookNo']} {book['bookName']} {book['bookAuthor']} "
            f"{book['bookPrice']} {book['bookDate'].strftime('%Y-%m-%d')} {book['bookStock']} "
            f"{book['publisher']['pubNo']} {book['publisher']['pubName']}"
            )

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
            book_data = {
                'bookNo': book.get_bNo(),
                'bookName': book.get_bName(),
                'bookAuthor': book.get_bAuthor(),
                'bookPrice': book.get_bPrice(),
                'bookDate': book.get_bDate(),
                'bookStock': book.get_bStock(),
                'publisher': {'pubNo': book.get_pNo(), 'pubName': book.get_pName()}
            }
            self.db.book.insert_one(book_data)
            print("도서 등록 완료") 
        except:
            print("insert error")
        
        self.disconnect()

    def update(self, book):
        # 도서수정
        # 수정된 데이터 DB 저장 : update 문 수행
        try:
            self.connect()
            filter_bookNo = {'bookNo': book.get_bNo()}
            update_data = {
                '$set': {
                    'bookName': book.get_bName(),
                    'bookAuthor': book.get_bAuthor(),
                    'bookPrice': book.get_bPrice(),
                    'bookDate': book.get_bDate(),
                    'bookStock': book.get_bStock(),
                    'publisher': {'pubNo': book.get_pNo(), 'pubName': book.get_pName()}
                }
            }
            self.db.book.update_one(filter_bookNo, update_data)
            print("도서 정보 수정 완료")
        except:
            print("update error")
        
        self.disconnect()  

    def delete(self, bNo):
        # 도서삭제
        # DB에서 도서번호 해당되는 데이터 삭제 : delete 문 수행
        try:
            self.connect()
            del_bNo = {'bookNo': bNo}
            result = self.db.book.delete_one(del_bNo)
            
            if result.deleted_count == 1:
                print(f"도서 정보 삭제 완료 (도서번호: {bNo})")
            else:
                print(f"도서 정보를 찾을 수 없습니다 (도서번호: {bNo})")
        except:
            print("delete error")
        
        self.disconnect()  
        print() 

    def search(self, bName):
        # 도서 검색하고 결과 출력
        try:
            self.connect()            
            filter_query = {'bookName': {'$regex': bName, '$options': 'i'}}
            result = self.db.book.find(filter_query)

            for book in result:
                print(
                    f"{book['bookNo']} {book['bookName']} {book['bookAuthor']} "
                    f"{book['bookPrice']} {book['bookDate'].strftime('%Y-%m-%d')} {book['bookStock']} "
                    f"{book['publisher']['pubNo']} {book['publisher']['pubName']}"
                )    
        except:
            print("search error")

        self.disconnect()
        print('\n도서 검색 완료')