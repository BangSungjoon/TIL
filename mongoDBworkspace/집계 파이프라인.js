
// MongoDB 집계 기능

// count() : 컬렉션 내의 도큐먼트 수
use('new_db')
db.book.find().count()

// 배열 형태로 반환되지만 length 사용안됨
use('new_db')
db.book.find().length

// 배열로 문자열 값 반환, 배열의 길이 속성 length 사용 가능
use('new_db')
db.book.distinct('bookAuthor').length

// 도큐먼트가 아닌 값인 경우 count() 사용하면 오류
use('new_db')
db.book.distinct('bookAuthor').count()


// 집계 파이프라인

// 도서의 출판사별로 그룹지어 총재고수량 계산
use("new_db")
db.book.aggregate(
    [
        {
            '$group' :
            {
                '_id': {'출판사' : '$publisher.pubName'},
                '총재고수량' : {$sum : '$bookStock'}
            }
        }
    ]
)

// 출판사별로 그룹지어 도서의 평균재고수량 계산
// $avg
use("new_db")
db.book.aggregate(
    [
        {
            '$group' :
            {
                '_id': {'출판사' : '$publisher.pubName'},
                '평균재고수량' : {$avg : '$bookStock'}
            }
        }
    ]
)

// 출판사별로 그룹지어 총재고수량 출력
// 총재고수량 기준 내림차순 정렬
// 2개 스테이지 사용
// (1) 그룹화 : $group
// (2) 정렬 : $sort  : 오름차순 정렬(1), 내림차순 정렬(-1)
use("new_db")
db.book.aggregate(
    [
        {
            '$group' :
            {
                '_id': {'출판사' : '$publisher.pubName'},
                '총재고수량' : {$sum : '$bookStock'}
            }
        },
        {
            '$sort' : {'총재고수량' : -1}
        }
    ]
)

// 출판사별로 그룹지어 평균재고수량 출력
// 평균재고수량 기준 오름차순 정렬
use("new_db")
db.book.aggregate(
    [
        {
            '$group' :
            {
                '_id': {'출판사' : '$publisher.pubName'},
                '평균재고수량' : {$avg : '$bookStock'}
            }
        },
        {
            '$sort' : {'평균재고수량' : 1}
        }
    ]
)

// 출판사별로 도서의 최고가, 최저가 출력
use("new_db")
db.book.aggregate(
    [
        {
            '$group' :
            {
                '_id': {'출판사' : '$publisher.pubName'},
                '도서의 최고가' : {$max : '$bookPrice'},
                '도서의 최저가' : {$min : '$bookPrice'}
            }
        }
    ]
)

// 도서의 최고가 / 최저가 출력
use("new_db")
db.book.aggregate(
    [
        {
            '$group' :
            {
                '_id': {},
                '도서의 최고가' : {$max : '$bookPrice'},
                '도서의 최저가' : {$min : '$bookPrice'}
            }
        }
    ]
)