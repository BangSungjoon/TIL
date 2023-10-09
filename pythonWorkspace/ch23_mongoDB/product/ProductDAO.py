from pymongo import MongoClient
from datetime import datetime

class ProductDAO:
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
        try:
            self.connect()
            result = self.db.product.find({
                'prdNo': {'$exists': True},
                'prdName': {'$exists': True},
                'prdPrice': {'$exists': True}
            })

            for product in result:
                print(
                f"{product['prdNo']} {product['prdName']} {product['prdPrice']} "
                f"{product['prdMaker']} {product['prdColor']} {product['ctgNo']}"
                )
        except:
            print("selece error")

        self.disconnect()
        print("상품 정보 조회 완료")
    
    def insert(self, product):
        try:
            self.connect()
            product_data = {
                'prdNo': product.get_pNo(),
                'prdName': product.get_pName(),
                'prdPrice': product.get_pPrice(),
                'prdMaker': product.get_pMaker(),
                'prdColor': product.get_pColor(),
                'ctgNo': product.get_cNo()
            }
            self.db.product.insert_one(product_data)
            print("상품 등록 완료") 
        except:
            print("insert error")
        
        self.disconnect()
        
        

    def update(self, product):
        try:
            self.connect()
            filter_prdNo = {'prdNo': product.get_pNo()}
            update_data = {
                '$set': {
                    'prdName': product.get_pName(),
                    'prdPrice': product.get_pPrice(),
                    'prdMaker': product.get_pMaker(),
                    'prdColor': product.get_pColor(),
                    'ctgNo': product.get_cNo()
                }
            }
            self.db.product.update_one(filter_prdNo, update_data)
            print("상품 정보 수정 완료")
        except:
            print("update error")
        
        self.disconnect()  

    def delete(self, prdNo):
        try:
            self.connect()
            del_pNo = {'prdNo': prdNo}
            result = self.db.product.delete_one(del_pNo)
            
            if result.deleted_count == 1:
                print(f"상품 정보 삭제 완료 (상품번호: {prdNo})")
            else:
                print(f"상품 정보를 찾을 수 없습니다 (상품번호: {prdNo})")
        except:
            print("delete error")
        
        self.disconnect()  
        print()
    
    def search(self, values):
        try:
            self.connect()            
    
            filter_query = {values['field']: {'$regex': values['value'], '$options': 'i'}}
            result = self.db.product.find(filter_query)

            for product in result:
                print(
                f"{product['prdNo']} {product['prdName']} {product['prdPrice']} "
                f"{product['prdMaker']} {product['prdColor']} {product['ctgNo']}"
                )  
        except Exception as e:
            print("search error:", e)

        self.disconnect()
        print('\n도서 검색 완료')