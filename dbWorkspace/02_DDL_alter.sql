ALTER TABLE student ADD stdTel VARCHAR(13);

describe student;

-- 여러개의 열 추가 : stdAge, stdAddress2 열 추가
ALTER TABLE student ADD (stdAge VARCHAR(2), stdAddress2 VARCHAR(50));

-- 열의 데이터 형식 변경 : 
ALTER TABLE student modify stdAge INT;

-- 열의 제약조건 변경 : stdName을 NOT NULL로 변경
ALTER TABLE student modify stdName VARCHAR(20) NOT NULL;

-- 열 이름 변경 : stdTel을 stdHP로 변경 (데이터 타입 적으면 안 됨)
ALTER TABLE student RENAME column stdtel TO stdHP;

-- 열 이름과 타입 변경 : stdAddress -> stdAddress1로 변경
ALTER TABLE student CHANGE stdAddress stdAddress1 VARCHAR(30);

-- 열 삭제 : stdHP 열 삭제
ALTER TABLE student DROP COLUMN stdHP;

-- 여러 개의 열 삭제 : DROP 열 이름
ALTER TABLE student DROP stdAge,
					DROP stdAddress1,
                    DROP stdAddress2;
                    
				
-- 테이블 ALTER 문 연습문제
ALTER TABLE product ADD (prdStock INT, prdDate DATE);
ALTER TABLE product modify prdCompany VARCHAR(20) NOT NULL;
ALTER TABLE publisher ADD (pubPhone VARCHAR(20), pubAddress VARCHAR(20));
ALTER TABLE publisher DROP COLUMN pubPhone;

-- -----------------------------------------------------------------

-- 기본키 삭제
ALTER TABLE student DROP PRIMARY KEY;

-- 외래키 삭제
ALTER TABLE student DROP foreign key FK_student_department;

-- 기본키 추가
ALTER TABLE student ADD PRIMARY KEY (stdNo);

-- 외래키 추가
ALTER TABLE student ADD foreign KEY (depNo) REFERENCES department (depNo);
ALTER TABLE student ADD CONSTRAINT FK_student_department
	FOREIGN KEY (depNo) REFERENCES department (depNo);

-- (1) scores 테이블에서 기본키 삭제
-- 외래키 2개 먼저 삭제하고 기본키 삭제
ALTER TABLE scores DROP foreign key FK_studio_no;
ALTER TABLE scores DROP foreign key FK_course_no;
ALTER TABLE scores DROP PRIMARY KEY;

-- (2) scores 테이블에서 기본키 추가
-- 외래키 2개 추가하고, 기본키 추가
ALTER TABLE scores ADD foreign KEY (stdNo) REFERENCES student (stdNo);
ALTER TABLE scores ADD foreign KEY (courseId) REFERENCES course (courseId);
ALTER TABLE scores ADD PRIMARY KEY (scoreNo);

-- ---------------------------------------------------------------
/*
	ON DELETE CASCADE
    - 기준 테이블의 데이터가 삭제되었을 때
    - 외래키로 지정된 테이블 (참조하는 테이블)의 데이터도 자동으로 삭제되도록 설정
*/

-- student 테이블에 설정된 외래키 제거하고
-- ON DELETE CASCADE로 외래키 다시 설정
-- department 테이블에서 데이터 삭제할 때
-- student 테입르에서도 데이터 삭제되는 지 확인
ALTER TABLE student DROP FOREIGN KEY FK_student_department;

ALTER TABLE student
	ADD CONSTRAINT FK_student_department
    FOREIGN KEY (deptNo) REFERENCES department (deptNo)
    ON DELETE CASCADE;
    
-- department 테이블에 데이터 삽입
-- 1 수학과
-- 2 영어과

-- student 테이블에 데이터 삽입
-- 2023001 홍길동 1 deptNo(2)
-- 2023002 이몽룡 1 deptNo(1)























