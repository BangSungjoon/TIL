-- 뷰 생성
CREATE VIEW client_view
AS
SELECT clientNo, clientName, clientAddress
FROM client;

-- 뷰에서 데이터 조회 (테이블처럼 사용)
SELECT * FROM client_view;

-- 뷰를 통해 데이터 변경 가능
-- (1) 뷰를 통해 INSERT 수행
-- 열이름 리스트 생략
INSERT INTO client_view VALUES('10', '케인', '제주');

alter table client modify clientAddress varchar(100) null;
alter table client modify clientGender varchar(2) null;

-- 오류 : 뷰에 clientphone 열은 포함되어 있지 않기 때문에 사용 불가
INSERT INTO client_view VALUES('10', '케인', '010-1234-1234', '제주');

describe client;

-- 뷰를 통해 update 수행
-- 고객번호 '1'의 주소를 '서울시'로 변경
UPDATE client_view SET clientAddress = '서울시' WHERE clientNo='1';
SELECT * FROM client_view;
SELECT * FROM client;

-- 뷰에 포함되어 있지 않은 열 수정 시 오류 : 사용 불가
UPDATE client_view SET clientHobby = '여행' WHERE clientNo='1';

-- (3) 뷰를 통해 delete 수행
-- 뷰를 통해 삽입한 데이터 삭제
DELETE FROM client_view where clientNo='10';

-- 뷰를 통해 삽입하지 않은 원래 있던 데이터도 삭제 가능
DELETE FROM client_view WHERE clientNo='9';


-- 뷰의 구조 변경 : ALTER 문 사용
CREATE VIEW top5_sales_clients
AS
SELECT C.clientNo 고객번호, C.clientName 고객명, 
	   SUM(BS.bsQty) 총주문수량, SUM(BS.bsQty * B.bookPrice) 총주문액
FROM booksale BS
	INNER JOIN client C ON C.clientNo = BS.clientNo
    INNER JOIN book B ON B.bookNo = BS.bookNo
GROUP BY BS.clientNo, C.clientName
ORDER BY 총주문액 DESC
LIMIT 5;

SELECT * FROM top5_sales_clients;

-- 또는 
create view top5_sales_client3
as
select bs.clientNo '고객번호', 
	   (select clientName from client where bs.clientNo = clientNo) '고객명', 
       sum(bsqty) '총주문수량',
	   sum((select bookPrice from book where bs.bookNo = bookNo) * bsqty) '총주문액'
from booksale bs
group by bs.clientNo 
ORDER BY 총주문액 DESC
limit 5;

SELECT * FROM top5_sales_client3;

-- 원본 테이블의 데이터 변경 --> 뷰에 바로 반영됨 
-- 고객번호 '4'의 주문수량 5개로 변경 
-- 뷰에 반영되는지 확인

-- ---------------------------------------------------------------------
-- 저장 프로시저

-- 저장 프로시저 정의
DROP PROCEDURE IF EXISTS clientProc;
DELIMITER $$
CREATE PROCEDURE clientProc()
BEGIN
	SELECT * FROM client;
END $$
DELIMITER ;

-- 저장 프로시저 호출
CALL clientProc();

-- 매개변수가 있는 저장 프로시저
-- 매개변수 유형 : IN / OUT
-- IN 매개변수 : 프로시저 호출하면서 전달되는 값을 받는 매개변수
	-- 형식 : IN 매개변수명 데이터타입
    -- 주의! : 매개변수명이 테이블의 열이름과 동일하면 안 됨
DROP PROCEDURE IF EXISTS clientProc2;
DELIMITER $$
CREATE PROCEDURE clientProc2(IN cName VARCHAR(20))
BEGIN
	SELECT * FROM client WHERE clientName = cName;
END $$
DELIMITER ;

-- 호출하면서 값 전달
CALL clientProc2('메시');
CALL clientProc2('베컴');


-- 연습문제
-- 저장 프로시저 생성 : bookStockProc()
-- 재고 수량 전달하고, 전달된 재고 수량 보다 더 많은 재고가 있는 도서 정보 출력하는 프로시저
-- 도서번호, 도서명, 저자, 가격, 출판사명
DELIMITER $$
CREATE PROCEDURE bookStockProc2(IN pbookStock INT)
BEGIN
	SELECT bookNo, bookName, bookAuthor, bookPrice, publisher.pubName 
    FROM book 
    INNER JOIN publisher ON publisher.pubNo = book.pubNo 
    WHERE pbookStock < bookStock;
END $$
DELIMITER ;

CALL bookStockProc2(5);

-- OUT 매개변수 : 출력 매개변수
-- 프로시저에서 결과를 반환하기 위해 사용하는 매개변수 (1개의 값을 받음)
-- 프로시저에서 출력할 값을 OUT 매개변수에 저장하고
	-- SELECT 열이름 INTO 출력매개변수
-- 저장 프로시저 CALL 하면서 출력매개변수 값을 받아서 @변수에 저장하고 사용
	-- CALL 프로시저명(@변수)
    -- SELECT @변수;
DROP PROCEDURE IF EXISTS bookMaxProc;
DELIMITER $$
CREATE PROCEDURE bookMaxProc(OUT maxPrice INT)
BEGIN
	-- 도서 최고가를 OUT 매개변수 maxPrice에 저장
	SELECT MAX(bookPrice) INTO maxPrice FROM book;
END $$
DELIMITER ;

CALL bookMaxProc(@maxP);  -- 결과 받은 변수명은 매개변수명과 달라도 됨
SELECT @maxP;

-- OUT 매개변수 연습문제
-- 도서가격이 25,000원 이상인 도서의 수를 OUT 매개변수로 반환해서 출력
-- 프로시저명 : bookCountProc
DROP PROCEDURE IF EXISTS bookCountProc;
DELIMITER $$
CREATE PROCEDURE bookCountProc(OUT upPrice INT)
BEGIN
	SELECT count(bookPrice) INTO upPrice FROM book WHERE bookPrice >= 25000;
END $$
DELIMITER ;

CALL bookCountProc(@COUNT); 
SELECT @COUNT;

-- IN / OUT 매개변수 둘 다 사용하는 경우
-- 도서가격을 전달하면, 전달된 도서가격 이상인 도서 수를 반환
DROP PROCEDURE IF EXISTS bookPriceCountProc;
DELIMITER $$
CREATE PROCEDURE bookPriceCountProc(IN bPrice INT, OUT bCount INT)
BEGIN
	SELECT count(*) INTO bCount 
    FROM book 
    WHERE bookPrice >= bPrice;
END $$
DELIMITER ;

CALL bookPriceCountProc(30000, @COUNT); 
SELECT @COUNT;

-- MySQL 변수 선언해서 사용하는 경우
SET @bPrice = 35000;
CALL bookPriceCountProc(@bPrice, @bookCount);
SELECT @bookCount;

-- -----------------------------------------------------------------
-- IF 문
/* 
	IF 조건 THEN
		- 수행문장
    ELSE 
		- 수행문장
    END IF;
*/

-- IF 문 예제
-- 도서번호를 전달하면, 해당 도서의 가격이 평균가 이상인지, 이하인지 
-- 평균, 도서가격, 결과(평균가 이하/평균가 이상)
DROP PROCEDURE IF EXISTS bookPriceCheckProc;
DELIMITER $$
CREATE PROCEDURE bookPriceCheckProc(IN bNo VARCHAR(10))
BEGIN
	-- 변수 선언
    DECLARE bAVG INT;
    DECLARE bPrice INT;
    
    -- 도서 평균가 구해서 변수 bAVG에 저장
    SELECT AVG(bookPrice) INTO bAVG FROM book;

	-- 전달 받은 도서번호에 해당되는 도서가격을 변수 bPrice에 저장
    SELECT bookPrice INTO bPrice FROM book WHERE bookNo = bNo;
    
    -- IF문 사용해서 비교 후 결과 출력
    IF bPrice >= bAVG THEN
		SELECT bAVG 평균, bPrice 도서가격, '평균가 이상' 결과;
	ELSE 
		SELECT bAVG 평균, bPrice 도서가격, '평균가 이하' 결과;
	END IF;
END $$
DELIMITER ;

-- 호출하면서 값 전달
CALL bookPriceCheckProc('1001'); -- 평균가 이하
CALL bookPriceCheckProc('1003'); -- 평균가 이상

-- IF 문 연습 문제
-- 재고 상황을 확인하는 프로시저
-- 도서번호를 전달 받아서 해당도서의 재고가 7 이상이면 재고 수준 위험, 아니면 재고 수준 보통
-- 재고수량, 결과(재고 수준 위험/재고 수준 보통) 출력
-- 프로시저명 : bookStockCheckProc
DROP PROCEDURE IF EXISTS bookStockCheckProc;
DELIMITER $$
CREATE PROCEDURE bookStockCheckProc(IN bNo VARCHAR(10))
BEGIN
	-- 변수 선언
    DECLARE bstock INT;
    SELECT bookStock INTO bstock FROM book WHERE bookNo = bNo;
    
    -- IF문 사용해서 비교 후 결과 출력
    IF bstock >= 7 THEN
		SELECT '재고 수준 위험' 결과;
	ELSE 
		SELECT '재고 수준 보통' 결과;
	END IF;
END $$
DELIMITER ;

CALL bookStockCheckProc('1001');

-- ----------------------------------------------------------------
-- CASE 문
/* 
	CASE
		WHEN 조건1 THEN 결과1
		WHEN 조건2 THEN 결과2
        WHEN 조건3 THEN 결과3
        ELSE 결과4
	END
    
    - 조건에 따라 결과값 반환
    - 조건이 여러 개인 경우에 사용
    - 주로 SELECT 절에서 반환값 열로 사용
*/
    
-- CASE문 예제
-- 고객의 연령대를 출력하는 프로시저
-- 고객번호를 전달 받아서, 해당 고객의 생년월일 확인 후 '~년대생' 출력
-- 예 : 1990년대생, 1970년대생, 2000년대생
-- 고객번호, 고객명, 연령대
DROP PROCEDURE IF EXISTS clientAgeCheckProc;
DELIMITER $$
CREATE PROCEDURE clientAgeCheckProc(IN cNo VARCHAR(10))
BEGIN
    SELECT clientNo, clientName, clientBirth,
		CASE
			WHEN SUBSTR(clientBirth, 1, 3) = '197' THEN '1970년대생'
			WHEN SUBSTR(clientBirth, 1, 3) = '198' THEN '1980년대생'
			WHEN SUBSTR(clientBirth, 1, 3) = '199' THEN '1990년대생'
			ELSE '2000년대생'
		END AS 연령대
    FROM client
    WHERE clientNo = cNo;
END $$
DELIMITER ;

CALL clientAgeCheckProc('1');
CALL clientAgeCheckProc('4');
    
    
-- CASE 연습문제
-- 한 번이라도 주문한 적이 있는 고객을 대상으로 해서 고객등급을 분류하는 프로시저
-- 고객번호를 전달하면 고객번호, 고객명, 총주문액, 고객등급 출력
-- 고객등급
	-- 총주문액이 200,000 이상이면 '최우수'
    -- 200,000 미만 100,000 이상이면 '우수'
    -- 100,000 미만 50,000 이상이면 '보통'
    -- 50,000 미만이면 '관심고객'
DROP PROCEDURE IF EXISTS clientRatingProc;
DELIMITER $$
CREATE PROCEDURE clientRatingProc(IN cNo VARCHAR(10))
BEGIN
	SELECT C.clientNo 고객번호, clientName 고객명, SUM(B.bookPrice*BS.bsQty) 총주문액,
    CASE
		WHEN SUM(B.bookPrice*BS.bsQty) >= 200000 THEN '최우수'
		WHEN SUM(B.bookPrice*BS.bsQty) >= 100000 THEN '우수'
        WHEN SUM(B.bookPrice*BS.bsQty) >= 50000 THEN '보통'
        ELSE '관심고객'
        END AS 고객등급
    FROM client C
		INNER JOIN booksale BS ON BS.clientNo = C.clientNo
		INNER JOIN book B ON B.bookNo = BS.bookNo
    WHERE C.clientNo = cNo
    GROUP BY C.clientNo, clientName;
END $$
DELIMITER ;

CALL clientRatingProc('1');
CALL clientRatingProc('2');

-- 한 번이라도 주문한 모든 고객의 고객등급 출력
-- 고객번호, 고객명, 총주문액, 고객등급 출력
DROP PROCEDURE IF EXISTS clientAllRatingProc;
DELIMITER $$
CREATE PROCEDURE clientAllRatingProc()
BEGIN
	SELECT C.clientNo 고객번호, clientName 고객명, SUM(B.bookPrice*BS.bsQty) 총주문액,
    CASE
		WHEN SUM(B.bookPrice*BS.bsQty) >= 200000 THEN '최우수'
		WHEN SUM(B.bookPrice*BS.bsQty) >= 100000 THEN '우수'
        WHEN SUM(B.bookPrice*BS.bsQty) >= 50000 THEN '보통'
        ELSE '관심고객'
        END AS 고객등급
    FROM client C
		INNER JOIN booksale BS ON BS.clientNo = C.clientNo
		INNER JOIN book B ON B.bookNo = BS.bookNo

    GROUP BY C.clientNo, clientName;
END $$
DELIMITER ;

CALL clientAllRatingProc();


-- ------------------------------------------------------
-- MySQL에서는 디폴트로 autocommit이 ON으로 설정되어 있음
-- AUTO COMMIT 설정 확인
SHOW VARIABLES LIKE '%commit%';

-- autocommit 설정 변경 가능
-- 0 : OFF
-- 1 : ON

set autocommit = 0;
set autocommit = 1;

-- rollback 확인
select * from book;
update book set bookAuthor='김길동' where bookNo='1001';
select * from book; -- 변경됨
rollback; -- 취소 (rollback 명령어 있다고 무조건 취소되는 것은 아님)
select * from book; -- 취소되지 않았음

-- transaction 시작 후 rollback 수행
start transaction;
update book set bookAuthor = '홍길동' where bookNo = '1001';
select * from book; -- 변경됨
rollback; -- 취소됨 (원래 김길동으로 바뀜)
select * from book; 

-- commit 이후에는 rollback 되지 않음
start transaction;
update book set bookAuthor = '홍길동' where bookNo = '1001';
commit; -- 작업 완료 (이후 rollback 되지 않음)
select * from book; -- 변경됨
rollback; -- 취소 안 됨 (앞에서 commit 했기 때문에)
select * from book; 