// findOne() : 도큐먼트 1개 반환 (배열 아님)
use('new_db')
db.book.findOne({'bookNo':'1001'})

// 도서명만 출력 : 데이터베이스 이론
use('new_db')
let book = db.book.findOne({'bookNo':'1001'})
console.log(book.bookName)

// (1) 호출메소드().필드명
use('new_db')
db.book.findOne({'bookNo':'1001'}).bookName

// (2) 호출메소드().key
use('new_db')
db.book.findOne({'bookNo':'1001'}).['bookName']

///////////////////////////////////////////////////
// find() : 배열로 반환된 경우
// 배열.forEach() 사용
use('new_db')
let books = db.book.find({'bookNo':'1001'})
books.forEach(book => {
    console.log(book.bookName)
});

// 도서 전체 내용 출력 (데이터만 출력)
// 도서번호 도서명 저자 가격 출판일 재고 출판사번호 출판사명
use('new_db')
let books = db.book.find()
books.forEach(book => {
    console.log(book.bookNo + " " + 
    book.bookName + " " + 
    book.bookAuthor + " " + 
    book.bookPrice + " " + 
    book.bookDate + " " + 
    book.bookStock + " " + 
    book.publisher.pubNo + " " + 
    book.publisher.pubName)
});