-- 조인(JOIN)

-- 다양한 조인 문 표기 방법(1)
-- WHERE 조건 사용
SELECT client.clientNo, clientName, bsQty
FROM client, bookSale
WHERE client.clientNo = booksale.clientNo;
-- ambiguous : 모호한 (명백하지 않음)
-- 양쪽 테이블에 공통되는 열 이름 앞에 모호성을 없애기 위해
-- 테이블명 표기 (테이블명이 없으면 오류)

-- client 테이블과 bookSale 테이블을 공통되는 열 clientNo를 기준으로 inner join
-- 의미 : 어떤 고객?
-- 한 번이라도 주문한 적이 있는 고객
-- 여기에 없는 고객은 한 번도 주문한 적이 없는 고객

-- 다양한 조인 문 표기 방법(2)
-- 양쪽 테이블에 공통되지는 않지만 모든 열 이름에 테이블명 붙임
SELECT client.clientNo, client.clientName, bookSale.bsQty
FROM client, bookSale
WHERE client.clientNo = booksale.clientNo;

-- 다양한 조인 문 표기 방법(3)
-- 테이블명 대신 별칭(Alias) 사용
SELECT C.clientNo, C.clientName, BS.bsQty
FROM client C, bookSale BS
WHERE C.clientNo = BS.clientNo;

-- 다양한 조인 문 표기 방법(4)
-- JOIN ON 명시
SELECT C.clientNo, C.clientName, BS.bsQty
FROM bookSale BS
	 JOIN client C
     ON C.clientNo = BS.clientNo;
     
-- 다양한 조인 문 표기 방법(4)
-- INNER JOIN ON 명시
SELECT C.clientNo, C.clientName, BS.bsQty
FROM bookSale BS
	INNER JOIN client C
    ON C.clientNo = BS.clientNo;
-- 가장 많이 쓰이는 방법으로 권장
-- 우리는 이 방법 사용

-- ---------------------------------------------------------------
-- 모든 열 (*) 출력
SELECT *
FROM client C
	INNER JOIN bookSale BS
    ON C.clientNo = BS.clientNo;
    
-- 필요한 열만 추출
-- 한 번이라도 도서를 주문한 적이 있는 고객의 고객번호와 고객명 출력
SELECT DISTINCT C.clientNo, C.clientName
FROM client C
	INNER JOIN bookSale BS
    ON C.clientNo = BS.clientNo;