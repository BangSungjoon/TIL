
// 쿼리
// 연산자를 이용한 쿼리

// 비교 연산자
// 상품 가격이 백만원 이상인 도큐먼트
use('new_db')
db.product.find({prdPrice: {$gte: 1000000}})

// 50만 이상 ~ 백만 미만 (and)
use('new_db')
db.product.find({prdPrice: {$gte: 500000, $lt:1000000}})

// 여러 개의 필도에 조건 설정
// 가격이 30000 이상이면서 재고가 5개 이하인 도서
use('new_db')
db.book.find({bookPrice: {$gte:30000}, bookStock: {$lte: 5}})



// 논리 연산자
// 상품 제조회사가 '삼성전자' 또는 'LG전자'만 출력 : $or
use('new_db')
db.product.find(
    {
        $or : 
        [
            {prdMaker:'HP'},
            {prdMaker:'LG전자'}
        ]
    }
)

// $not : 부정
// 재고가 5 초과 아닌 것 : 5이하
use('new_db')
db.book.find({bookStock: {$not: {$gt: 5}}})

// 도서가격이 2만원 미만이거나 3만원 이상인 도서 출력
use('new_db')
db.book.find(
    {
        $or : 
        [
            {bookPrice: {$lt:20000}},
            {bookPrice: {$gte: 30000}}
        ]
    }
)

// 도서가격이 2만원 이상, 3만원 미만인 도서 출력
use('new_db')
db.book.find({bookPrice: {$gte: 20000, $lt:30000}})

use('new_db')
db.book.find(
    {
        $and : 
        [
            {bookPrice: {$lt:30000}},
            {bookPrice: {$gte:20000}}
        ]
    }
)

// 문자열 검색
// 검색 필드에 문자열 인덱스 설정해야 함
// bookName과 bookAuthor 필드에 문자열 인덱스 생성
use('new_db')
db.book.createIndex({ bookName: 'text', bookAuthor: 'text'})
// $text, $search 연산자를 사용해서 문자열 탐색
db.book.find({$text : {$search : '프로그래밍'}})

use('new_db')
db.book.find({$text : {$search : '홍길동'}})

// 정규식
// 도서명이 '안'으로 시작하는 도서 출력
use('new_db')
db.book.find({bookName:/^안/})

// 도서명이 '밍'으로 끝나는 : $
use('new_db')
db.book.find({bookName:/밍$/})

// 도서명이 '밍'으로 끝나는 도큐먼트 수 출력
use('new_db')
db.book.find({bookName:/밍$/}).count() //5개

// 도서명이 '밍'으로 끝나고, 가격이 25,000 이상 ~ 30,000이하인 도서 출력
use('new_db')
db.book.find(
    {
        $and :
        [
            {bookName:/밍$/},
            {bookPrice: {$gte:25000}},
            {bookPrice: {$lt:30000}}
        ]
    }
)

// $regex : 한 필드에 여러 연산자를 같이 적용할 때 사용
// '밍'으로 끝나면서 '안'~'자' : and
use('new_db')
db.book.find({bookName : {$regex: /밍$/, $gte:'안', $lt:'자'}})

// Array (배열 연산자)
use('new_db')
db.createCollection('inventory')

// 배열을 포함하는 도큐먼트 삽입
use('new_db')
db.inventory.insertMany(
    [
        { item: 'journal', qty: 25, tags: ['blank', 'red']},
        { item: 'notebook', qty: 50, tags: ['red', 'blank']},
        { item: 'journal', qty: 100, tags: []},
        { item: 'journal', qty: 75, tags: ['blank', 'red']},
        { item: 'journal', qty: 45, tags: ['blue']}
    ]
)

// 'red'가 포함된 모든 도큐먼트 출력
use('new_db')
db.inventory.find({tags:'red'})

// 배열 안에서 값과 순서가 일치하는 도큐먼트 검색
use('new_db')
db.inventory.find({tags:['red', 'blank']})

// $all : 'red', 'blank' 모두 만족 (순서 상관 없음)
use('new_db')
db.inventory.find({tags: {$all: ['red', 'blank']}})



use('new_db')
db.createCollection('fruits')

use('new_db')
db.fruits.insertOne({_id:1, fruit: ['apple', 'pear', 'banana']})
db.fruits.insertOne({_id:2, fruit: ['apple', 'banana', 'peach']})
db.fruits.insertOne({_id:3, fruit: ['cherry', 'pear', 'strawberry']})
db.fruits.insertOne({_id:4, fruit: ['rasberry', 'cherry', 'banana']})
db.fruits.find()

// apple과 banana가 포함된 document 출력
use('new_db')
db.fruits.find({fruit:{$all: ['apple', 'banana']}})

// $in : or
use('new_db')
db.fruits.find({fruit:{$in: ['apple', 'banana']}})

// fruit 배열 요소가 4개인 도큐먼트 추가
use('new_db')
db.fruits.insertOne({_id:5, fruit: ['apple', 'cherry', 'pear', 'banana']})

// $size : 3 배열 요소가 3개인 도큐먼트 
use('new_db')
db.fruits.find({fruit: {$size : 3}})
// $size : 4 배열 요소가 4개인 도큐먼트 
use('new_db')
db.fruits.find({fruit: {$size : 4}})

// $push : 배열에 요소 추가
use('new_db')
db.fruits.updateOne({_id:4}, {$push : { fruit: 'strawberry'}})
db.fruits.find({_id: 4})


// board 콜렉션 추가
use('new_db')
db.createCollection('board')

use('new_db')
db.board.insertOne({
    _id:1,
    title: '사용후기',
    writer: 'abcd',
    content: '가성비 최고',
    comments:
        [
            {id:1, content:'댓글1', user_id:'aaa'},
            {id:2, content:'댓글2', user_id:'bbb'},
            {id:3, content:'댓글3', user_id:'ccc'}
        ]
})

db.board.insertOne({
    _id:2,
    title: '중고거래',
    writer: 'sky',
    content: '최저가 판매',
    comments:
        [
            {id:4, content:'댓글4', user_id:'ddd'},
            {id:5, content:'댓글5', user_id:'eee'},
            {id:6, content:'댓글6', user_id:'fff'}
        ]
})

use('new_db')
db.board.find()

// 임베디드 도큐먼트 접근 : 필드명.필드명
// "comments.id" : 따옴표 없으면 오류
use('new_db')
db.board.find({'comments.id':1})

// 배열에서 인덱스 사용시 [] 없이 숫자만 (0부터 시작)
use('new_db')
db.board.find({'comments.0.id':1, 'comments.0.user_id': 'aaa'})

// 배열 안에서 요소 단위 찾음
use('new_db')
db.board.findOne({comments: {$elemMatch: {id:4, user_id:'ddd'}}})

// 못찾음 : null
use('new_db')
db.board.findOne({comments: {id:4, user_id:'ddd'}})

// 프로젝션 연산자 : 필드만 선택해서 표시 (1)
use('new_db')
db.inventory.find({tags: 'red'}, {tags:1})

// 프로젝션 연산자 : $
// red로 검색해서 red 만 출력
use('new_db')
db.inventory.find({tags: 'red'}, {'tags.$':true})