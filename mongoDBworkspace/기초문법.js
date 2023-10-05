use('new_db')

db.product.find({"prdNo":"15"})

// 프로젝션 : 보여줄 필드 선택
// 1: 출력
db.product.find({"prdNo":"15"}, {prdNo:1, prdName:1})

// show collections : shell 명령어 사용 못함 (오류)
// 모든 컬렉션 출력
db.getCollectionNames()

// 컬렉션 생성
db.createCollection('book2')

// 도큐먼트 생성1 : insertMany()
db.product.insertMany([
    {'prdNo': "17",
    "prdName": "알뜰 냉장고",
    "prdPrice": 50000},
    {"prdNo": "18",
    "prdName": "알뜰 TV",
    "prdPrice": 150000}
])

prd1 = {
    "prdNo": "17",
    "prdName": "알뜰 냉장고2",
    "prdPrice": 50000
}

prd2 = {
    'prdNo': '20',
    'prdName': '알뜰 냉장고3',
    'prdPrice': 50000
}

db.product.insertMany([prd1, prd2])

use('new_db')
db.product.find({'prdNo':'15'}, {prdNo:1, prdName:'엄준식'})

use('new_db')
db.product.updateOne(
    {'prdNo':'10'},
    {"$set": 
        {"prdPrice":777}}
)

db.product.find({'prdNo':'10'})

use('new_db')
// 여러 행 수정
db.book.updateMany({"publisher.pubNo": "3"},
    {"$set":
        {"publisher.pubName": "정보출판"}
    }
)

db.book.find()

use('new_db')
// upsert : true : 조건에 해당되는 도큐먼트 없으면 새로 추가
db.book.updateOne(
    {'bookAuthor':'이길동'},
    {$set : 
        {'book_author_first':'길동', 'book_author_last':'이'}},
    {upsert : true}
)
db.book.find()

use('new_db')
// "키" : 따옴표 / 키: 따옴표 없어도 오류 없음
db.book.deleteOne({bookAuthor: "이길동"})
db.book.find()

use('new_db')
db.product.deleteMany({prdMaker:"삼성전자"})
db.product.find()

// 연습문제
use('new_db')
db.createCollection('clothes')

use('new_db')
db.clothes.insertMany([
    {'cNo': "1",
    "cName": "체크무늬 잠옷바지",
    "cPrice": 5000,
    "ctg": [
            {
                'ctgNo':'1',
                'ctgName':'하의'
            }
        ]
    },
    {'cNo': "2",
    "cName": "가죽 자켓",
    "cPrice": 150000,
    "ctg": [
            {
                'ctgNo':'2',
                'ctgName':'상의'
            }
        ]
    },
    {'cNo': "3",
    "cName": "패딩",
    "cPrice": 500000,
    "ctg": [
            {
                'ctgNo':'2',
                'ctgName':'상의'
            }
        ]
    },
    {'cNo': "4",
    "cName": "여름 반팔",
    "cPrice": 12000,
    "ctg": [
            {
                'ctgNo':'2',
                'ctgName':'상의'
            }
        ]
    },
    {'cNo': "5",
    "cName": "청바지",
    "cPrice": 35000,
    "ctg": [
            {
                'ctgNo':'1',
                'ctgName':'하의'
            }
        ]
    }
])
db.clothes.find()

use('new_db')
db.clothes.updateOne(
    {'cNo':'1'},
    {"$set": 
        {"cPrice":8000}}
)
// 여러 행 수정
use('new_db')
db.clothes.updateMany({"ctg.ctgNo": '1'},
    {"$set":
        {"ctg.ctgName": "바지"}
    }
)
db.clothes.find()

use('new_db')
db.clothes.deleteOne({cName: "체크무늬 잠옷바지"})
db.clothes.deleteMany(
    {'ctg.ctgNo': '2'}
)
db.clothes.find()