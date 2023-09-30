use sqldb3;

use mysql;

-- 사용자 계정 조회
SELECT * FROM user;

-- 사용자 계정 생성
-- CREATE USER 계정@호스트 identified by 비밀번호;
-- 호스트
	-- localhost : 로컬에서 접근 가능
    -- 192.168.172.1 : 특정 IP에서 접근 가능
    -- '%' : 어디에서나 접근 가능
    
-- 비밀번호 변경
	-- SET PASSWORD for '계정명@호스트' = '새 비밀번호';
    
    -- 계정 삭제 : DROP USER 계정명@호스트;
    
-- 계정 삭제 : DROP USER 계정명@호스트;

-- 계정 생성
CREATE USER newuser1@'%' identified by '1111';
-- newuser1으로 Connection 생성해서 서버에 접속되는지 확인
-- 스키마 접근 불가
-- 현재 계정만 생성되고, 어떤 권한도 설정되지 않았음

-- 비밀번호 변경
SET PASSWORD for 'newuser1'@'%' = '1234';

-- 계정 삭제
DROP USER 'newuser1'@'%';

-- ----------------------------------------------------------
-- 권한 조회 : SHOW GRANTS FOR 사용자계정;

-- 권한 부여 : GRANT 권한 ON 데이터베이스.테이블 To 계정@호스트;
-- 모든 권한 부여 : GRANT all privileges ON *.* TO 계정@호스트;
-- 특정 DB의 모든 테이블에 특정 권한 부여
	-- GRANT select, insert, update, delete ON 특정DB.* TO 계정@호스트;

-- 계정 생성
CREATE USER newuser1@'%' identified by '1111';

-- newuser1에 권한 부여
GRANT all privileges on *.* to newuser1@'%';

-- newuser1에 권한 조회
SHOW GRANTS FOR newuser1;

-- 다시 접속 생성
-- 모든 스키마/테이블 접근 가능한지 확인

-- SELECT 권한 삭제
REVOKE select ON *.* FROM newuser1@'%';
-- sqldb4 데이터베이스에서 테이블 선택해서 내용 확인 -> 접근 불가
    
    
-- 특정 DB에 모든 테이블에 특정 권한 부여 
-- *.* : 데이터베이스.테이블
GRANT select ON sqldb4.* TO newuser1@'%';
SHOW GRANTS FOR newuser1;


-- ----------------------------------------------------------
/*
	DCL 작업은 다음과 같은 권한을 부여
	- 계정 생성 및 삭제
    - 비밀번호 변경
    - 권한 부여 및 제거
*/