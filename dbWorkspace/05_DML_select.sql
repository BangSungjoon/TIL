-- SELECT 문 예제
use sqldb3;

-- 데이터 임포트 : publisher, book, booksale, client
SELECT * FROM book;
describe booksale;
-- 데이터 타입 변경 기본키는 VARCHAR(10) 출판사번호, 도서번호, 고객번호, 주문번호
-- 날짜는 DATE 타입

-- (1) publisher 테이블
ALTER TABLE publisher MODIFY pubNo VARCHAR(10) NOT NULL PRIMARY KEY,
					  MODIFY pubName VARCHAR(20) NOT NULL;
-- (2) book 테이블 
ALTER TABLE book MODIFY bookNo VARCHAR(10) NOT NULL PRIMARY KEY,
				 MODIFY bookDate DATE;
ALTER TABLE book add foreign key(pubNo) REFERENCES publisher(pubNo);
-- (3) client 테이블
ALTER TABLE client MODIFY clientBirth DATE,
				   MODIFY clientNo VARCHAR(10) NOT NULL PRIMARY KEY;

-- (4) booksale 테이블
ALTER TABLE booksale MODIFY bsDate DATE,
					 MODIFY bsNo VARCHAR(10) NOT NULL PRIMARY KEY;
ALTER TABLE booksale add foreign key(clientNo) REFERENCES client(clientNo),
					 add foreign key(bookNo) REFERENCES book(bookNo);
                     

-- -------------------------------------------------------------------
-- book 테이블에서 모든 행 / 모든 열 검색
-- 모든 (*) 열 출력
SELECT * FROM book;

-- 도서명과 가격만 검색
SELECT bookName, bookPrice FROM book;

-- 저자만 검색
SELECT bookAuthor FROM book;

-- 저자만 검색 (중복된 행은 한 번만 출력 : DISTINCT)
SELECT DISTINCT bookAuthor FROM book;

-- ----------------------------------------------------------------
-- 비교 (=, <, >, <=, >=, !=)

-- 저자가 '홍길동'인 도서의 도서명, 저자 출력
SELECT bookName, bookAuthor FROM book
WHERE bookAuthor = '홍길동';

-- 도서가격이 30000 이상인 행의 도서명, 가격, 재고 출력
SELECT bookName, bookPrice, bookStock FROM book
WHERE bookPrice >= 30000;

-- 재고가 3~5 사이인 도서의 도서명, 재고 출력
SELECT bookName, bookStock FROM book
WHERE bookStock >= 3 AND bookStock <= 5;

-- 범위 (BETWEEN)
-- 재고가 3~5 사이인 도서의 도서명, 재고 출력
SELECT bookName, bookStock FROM book
WHERE bookStock BETWEEN 3 AND 5;

-- 리스트에 포함 (IN, NOT IN)
-- 출판사명이 '서울 출판사'(pubNo='1')와 '도서출판 강남'(pubNo='2')인 도서의 도서명, 출판사번호 출력
SELECT bookName, pubNo FROM book
WHERE pubNo IN ('1', '2');
-- 또는
SELECT bookName, pubNo FROM book
WHERE pubNo = '1' OR pubNo = '2';

-- '도서출판 강남'에서 출판하지 않은 도서의 도서명, 출판사 번호 출력
SELECT bookName, pubNo FROM book
WHERE pubNo NOT IN ('2');

-- NULL (IS NULL, IS NOT NULL)

-- 먼저 client 테이블 확인
SELECT * FROM client;

-- 취미에 null 값이 들어 있는 행 검색
-- 고객명, 취미 출력 (현재 NULL 값 없음)
SELECT clientName, clientHobby FROM client
WHERE clientHobby IS NULL;

-- NULL로 설정
ALTER TABLE CLIENT MODIFY clientName VARCHAR(20) NULL,
				   MODIFY clientHobby VARCHAR(20) NULL;

UPDATE client SET clientHobby=null WHERE clientName='호날두';
UPDATE client SET clientHobby=null WHERE clientName='샤라포바';

-- 취미에 null 값이 들어 있는 행 검색
-- 고객명, 취미 출력
SELECT clientName, clientHobby FROM client
WHERE clientHobby IS NULL;

-- 취미에 NULL 값이 아닌 행 검색
SELECT clientName, clientHobby FROM client
WHERE clientHobby IS NOT NULL;

-- 취미에 공백이 들어 있는 행 검색
SELECT clientName, clientHobby FROM client
WHERE clientHobby = '';

SELECT clientName, clientHobby FROM client
WHERE clientHobby = '         ';   -- 스페이스 개수 상관없음

-- 논리 (AND, OR)

-- 저자가 '홍길동'이면서 재고가 3권 이상인 모든 도서 출력
SELECT * FROM book
WHERE bookAuthor = '홍길동' and bookstock >= 3;

-- 저자가 '홍길동'이거나 '성춘향'인 모든 도서 출력
SELECT * FROM book
WHERE bookAuthor = '홍길동' or bookAuthor = '성춘향';
-- 또는
SELECT bookName, bookAuthor FROM book
WHERE bookAuthor IN ('홍길동', '성춘향');

-- 패턴 매칭 (LIKE)
-- 출판사 테이블에서 출판사명에 '출판사'가 포함된 모든 행 검색
SELECT * FROM publisher
WHERE pubName LIKE '%출판사%';

-- 고객 테이블에서 출생연도가 1990년대인 모든 행 검색
SELECT * FROM client
WHERE clientBirth LIKE '199%';

-- 고객 테이블에서 이름이 4글자인 모든 행 검색
-- 4글자 : 언더바 4개 (____)
SELECT * FROM client WHERE clientName LIKE '____';

-- 도서 테이블에서 도서명에 '안드로이드'가 들어 있지 않는 도서의 도서명 출력
SELECT bookName FROM book
WHERE bookName NOT LIKE '%안드로이드%';




