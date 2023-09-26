-- 내장 함수
/* 
	ROUND() 함수
		반올림한 값을 구하는 함수
			ROUND(값, 자리수)
            자리수 아래서 반올림하여 자리수까지 출력
            - 양수 값 : 소수점 오른쪽 자리수
            - 음수 값 : 소수점 왼쪽 자리수
*/

-- 고객별 평균 주문액을 백원 단위에서 반올림하여 출력 (천의자리까지 출력)
SELECT clientNo, ROUND(AVG(bookPrice * bsQty)) 평균주문액,
				 ROUND(AVG(bookPrice * bsQty), 0) 1자리까지출력,
                 ROUND(AVG(bookPrice * bsQty), -1) 10자리까지출력,
                 ROUND(AVG(bookPrice * bsQty), -2) 100자리까지출력,
                 ROUND(AVG(bookPrice * bsQty), -3) 1000자리까지출력
FROM book, bookSale
WHERE book.bookNo = bookSale.bookNo
GROUP BY clientNo;

-- format() 함수
-- 천단위 구분 표시
-- 반올림
-- 문자열 타입 반환
-- 출판사별 재고 수량과 평균 재고액 출력
SELECT pubNo, format(AVG(bookStock), 3) 평균재고수량,
			  format(AVG(bookPrice * bookStock), 0) 평균재고액 
FROM book 
GROUP BY pubNo;

-- 순위 출력 함수
-- RANK() / DENSE_RANK() / ROW_NUMBER()
-- RANK() : 값의 순위 반환 (동일 순위 개수만큼 증가) 1 1 3 4 ...
-- DENSE_RANK() : 값의 순위 반환 (동일 순위 상관없이 1 증가) 1 1 2 3
-- ROW_NUMBER() : 행위 순위 반환. 1 2 3 ...
SELECT bookPrice,
	   RANK() OVER (ORDER BY bookPrice DESC) 'RANK',
       DENSE_RANK() OVER (ORDER BY bookPrice DESC) 'DENSE_RANK',
       ROW_NUMBER() OVER (ORDER BY bookPrice DESC) 'ROW_NUMBER'
FROM book;


-- 문자 함수
-- REPLACE() : 문자열을 치환하는 함수
	-- 테이블의 실제 데이터는 변경되지 않음
-- 도서명에 '안드로이드'가 포함된 도서에 대해서
-- 도서명에 포함된 '안드로이드'를 'Android'로 변경해서 출력
SELECT bookNo, REPLACE(bookName, '안드로이드', 'Android') bookName,
	   bookAuthor, bookPrice 
FROM book 
WHERE bookName Like '%안드로이드%';

-- CHAR_LENGTH() : 글자의 수를 반환하는 함수
-- LENGTH() : 바이트 수 반환
-- '서울 출판사'에서 출간한 도서의 도서명과 도서명의 글자 수, 바이트 수, 출판사명 출력
SELECT bookName, LENGTH(bookName), CHAR_LENGTH(bookName), pubName
FROM book INNER JOIN publisher ON book.pubNo = publisher.pubNo
WHERE pubName = '서울 출판사';
-- '자바 프로그래밍' : 8글자 스페이스 포함
-- 22바이트 : 한글은 3바이트. 3x7=21바이트, 스페이스는 1바이트

-- SUBSTR() : 지정한 길이만큼의 문자열을 반환하는 함수
-- SUBSTR(전체문자열, 시작, 길이)

-- 저자에서 성씨만 출력
SELECT SUBSTR(bookAuthor, 1, 1)
FROM book

-- 저자에서 이름만 출력
SELECT SUBSTR(bookAuthor, 2, 2) 
FROM book

-- SUBSTR() 연습문제
-- (1) 도서 테이블에서 저자 중 성씨가 '손'인 모든 저자 출력
SELECT bookAuthor
FROM book
WHERE SUBSTR(bookAuthor, 1,1) LIKE '손%';

-- (2) 저자 중에서 같은 성씨를 가진 사람이 몇 명이나 되는 지 알아보기 위해
	-- 성씨별로 그룹지어 인원 수 출력
SELECT SUBSTR(bookAuthor, 1, 1) 성, COUNT(SUBSTR(bookAuthor, 1, 1)) 인원수
FROM book
GROUP BY 성;

-- -----------------------------------------------------------------------
-- 현재 날짜와 시간 출력

SELECT DATE(NOW()) 날짜, TIME(NOW()) 시간;

-- 연 월 일 출력
SELECT YEAR(CURDATE()), MONTH(CURDATE()), DAYOFMONTH(CURDATE());

-- 시 분 초 마이크로초 출력
SELECT HOUR(CURTIME()), MINUTE(CURTIME()), SECOND(CURTIME()), 
	   MICROSECOND(CURTIME());

SELECT HOUR(CURRENT_TIME()), MINUTE(CURRENT_TIME()), SECOND(CURRENT_TIME()), 
	   MICROSECOND(CURRENT_TIME());

-- 시간 계산
SELECT DATEDIFF('2022-09-26', NOW()), TIMEDIFF('23:23:59', '12:11:10');
SELECT DATEDIFF(NOW(), '2022-09-26'), TIMEDIFF('23:23:59', '12:11:10');


-- ---------------------------------------------------------------
CREATE TABLE flower(
	flowerNo VARCHAR(10) NOT NULL PRIMARY KEY,
    flowerName VARCHAR(30),
    flowerInfo LONGTEXT,
	flower LONGBLOB
);

INSERT INTO flower VALUES ('f002', '장미',
	LOAD_FILE('C:/AI-backend/TIL/dbWorkspace/rose.txt'),
    LOAD_FILE('C:/AI-backend/TIL/dbWorkspace/rose.jpg'));

-- 파일 업로드/다운로드 경로 변수 확인
SHOW variables LIKE 'secure_file_priv';

-- 동영상 파일 저장
CREATE TABLE movie (
	movieId VARCHAR(10) NOT NULL PRIMARY KEY,
    movieTitle VARCHAR(50),
    movieDirector VARCHAR(20),
    movieStar VARCHAR(20),
    movieScript LONGTEXT,
    movieFilm LONGBLOB
);

INSERT INTO movie VALUES ('1', '쉰들러 리스트', '스필버그', '리암 니슨',
	LOAD_FILE('C:/AI-backend/TIL/dbWorkspace/movies/Schindler.txt'),
    LOAD_FILE('C:/AI-backend/TIL/dbWorkspace/movies/Schindler.mp4'));

SHOW variables LIKE 'max_allowed_packet';

-- -----------------------------------------------------------------
-- 테이블 데이터를 파일로 내보내기

-- 도서 테이블 데이터를 텍스트 파일로 내보내기
SELECT * FROM book
	INTO OUTFILE 'C:/AI-backend/TIL/dbWorkspace/movies/book_out.txt';

-- LONGTEXT 타입의 영화 대본 데이터를 텍스트 파일로 내보내기 : INTO OUTFILE
SELECT movieScript FROM movie
	INTO OUTFILE 'C:/AI-backend/TIL/dbWorkspace/movies/Schindler_out.txt';

-- LONGTEXT 타입의 영화 대본 데이터를 텍스트 파일로 내보내기 
-- 줄바꿈 문자로 출력되지 않도록 저장
SELECT movieScript FROM movie
	INTO OUTFILE 'C:/AI-backend/TIL/dbWorkspace/movies/Schindler_out2.txt'
    LINES TERMINATED BY '\\n';

-- 동영상 파일 : 바이너리 파일 내보내기 : INTO DUMPFILE
SELECT movieFilm FROM movie
	INTO DUMPFILE 'C:/AI-backend/TIL/dbWorkspace/movies/Schindler_out.mp4';


-- --------------------------------------------------------

-- 테이블 복사
-- 복사 후 기본키(제약조건) 설정해야 함

-- 테이블 복사1 : 새 테이블로 전체 복사 
CREATE TABLE new_book1 AS
SELECT * FROM book;

describe new_book1;
describe book;

-- new_book1에 기본키/외래키 제약조건 추가  
alter table new_book1 add primary key (bookno);
alter table new_book1 add foreign key (pubno) references publisher (pubno);


-- 테이블 복사2 : 새 테이블로 일부만 복사 
-- book 테이블에서 도서출간일이 2021년 1월 1일 이후 도서들만 복사하여
-- new_book2 테이블 생성 
create table new_book2 as
select * from book
where bookDate >= '2021-01-01';

alter table new_book2 add primary key (bookno);
alter table new_book2 add foreign key (pubno) references publisher (pubno);
describe new_book2;

-- 테이블 복사3 : 이미 존재하는 테이블에 데이터만 복사 
-- (테이블 구조가 동일한 경우에만 가능함)

-- new_book2 테이블의 모든 데이터 삭제 (구조 유지)
-- DELETE : 데이터만 삭제 (DML)
DELETE FROM new_book2; 
SELECT * FROM new_book2;

-- 테이블 구조가 동일한 new_book2에 book 테이블의 모든 데이터 복사 
INSERT INTO new_book2 SELECT * FROM book;

-- -------------------------------------------------------

-- 다른 데이터베이스의 테이블 복사 
-- 데이터베이스명.테이블명 

CREATE TABLE product AS
SELECT * FROM sqldb2.product;

SELECT * FROM product;
describe product;
alter table product add primary key (prdNo);










