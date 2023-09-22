
-- DROP 문

-- 테이블 삭제
-- publisher 테이블 삭제
-- 외래키 제약조건 설정되어 있기 때문에 삭제 시 오류 
DROP TABLE publisher;

-- 외래키 제약조건 확인할 필요 없도록 설정
SET FOREIGN_KEY_CHECKS = 0;

-- 외래키 제약조건 검사하도록 재설정 
SET FOREIGN_KEY_CHECKS = 1;