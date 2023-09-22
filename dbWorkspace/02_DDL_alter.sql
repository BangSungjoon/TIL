-- ALTER 문 

-- 열 추가 : stdTel 열 추가
ALTER TABLE student ADD stdTel VARCHAR(13);

describe student;

-- 여러 개의 열 추가 : stdAge, stdAddress2 열 추가
ALTER TABLE student ADD (stdAge VARCHAR(2), stdAddress2 VARCHAR(50));

-- 열의 데이터 형식 변경 : stdAge열의 데이터 타입을 INT로 변경
ALTER TABLE student MODIFY stdAge INT;

-- 열의 제약조건 변경 : stdName을 NOT NULL로 변경
ALTER TABLE student MODIFY stdName VARCHAR(20) NOT NULL;

-- 열 이름 변경 : stdTel을 stdHP로 변경 (데이터 타입 적으면 안 됨)
ALTER TABLE student RENAME COLUMN stdTel TO stdHP;

-- 열 이름과 타입 변경 : stdAddress ->  stdAddress1로 변경
ALTER TABLE student CHANGE stdAddress stdAddress1  VARCHAR(30);

-- 열 삭제 : stdHP 열 삭제 : 1개 열 삭제
ALTER TABLE student DROP COLUMN stdHP;

-- 여러 개의 열 삭제 : DROP 열이름
ALTER TABLE student DROP stdAge,
					DROP stdAddress1,
                    DROP stdAddress2;


/*
테이블 ALTER 문 연습문제
	(1) product 테이블에 숫자 값을 갖는 prdStock과 제조일을 나타내는 prdDate 열 추가
	(2) product 테이블의 prdCompany 열을 NOT NULL로 변경
	(3) publisher 테이블에 pubPhone, pubAddress 열 추가
	(4) publisher 테이블에서 pubPhone 열 삭제

*/
-- (1) product 테이블에 숫자 값을 갖는 prdStock과 제조일을 나타내는 prdDate 열 추가
ALTER TABLE product ADD (prdStock INT, prdDate DATE);

-- (2) product 테이블의 prdCompany 열을 NOT NULL로 변경
ALTER TABLE product MODIFY prdCompany VARCHAR(30) NOT NULL;

-- (3) publisher 테이블에 pubPhone, pubAddress 열 추가
ALTER TABLE publisher ADD (pubPhone VARCHAR(20), pubAddress VARCHAR(100));

-- (4) publisher 테이블에서 pubPhone 열 삭제
ALTER TABLE publisher DROP COLUMN pubPhone;

-- ------------------------------------------------------------

-- 기본키 삭제
ALTER TABLE student DROP PRIMARY KEY;

-- 외래키 삭제
ALTER TABLE student DROP FOREIGN KEY FK_student_department;
-- student_ibfk_1 이름의 외래키 삭제
ALTER TABLE student DROP FOREIGN KEY student_ibfk_1;

-- 기본키 추가
ALTER TABLE student ADD PRIMARY KEY (stdNo);

-- 외래키 추가
ALTER TABLE student ADD FOREIGN KEY (deptNo) REFERENCES department (deptNo);
ALTER TABLE student ADD CONSTRAINT FK_student_department 
	FOREIGN KEY (deptNo) REFERENCES department (deptNo);


-- (1) scores 테이블에서 기본키 삭제
-- 외래키 2개 먼저 삭제하고 기본키 삭제
alter table scores drop foreign key FK_score_course;
alter table scores drop foreign key FK_score_student;
alter table scores drop primary key;


-- (2) scores 테이블에서 기본키 추가
-- 외래키 2개 추가하고, 기본키 추가
alter table scores add CONSTRAINT FK_score_student 
	FOREIGN KEY (stdNo) REFERENCES student(stdNo);
alter table scores add CONSTRAINT FK_score_course 
	FOREIGN KEY (courseId) REFERENCES course(courseId);
alter table scores add primary key (stdNo, courseId);

-- 또는

ALTER TABLE scores ADD foreign KEY (stdNo) REFERENCES student (stdNo);
ALTER TABLE scores ADD foreign KEY (courseId) REFERENCES course (courseId);
ALTER TABLE scores ADD PRIMARY KEY (stdNo, courseId);

-- --------------------------------------------------------
/*
	ON DELETE CASCADE
	- 기준 테이블의 데이터가 삭제되었을 때
	- 외래키로 지정된 테이블(참조하는 테이블)의 데이터도 자동으로 삭제되도록 설정
*/

-- student 테이블에 설정된 외래키 제거하고
-- ON DELETE CASCADE로 외래키 다시 설정
-- department 테이블에서 데이터 삭제할 때
-- student 테이블에서도 데이터 삭제되는 지 확인
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

-- department에서 2 영어과 행 삭제
-- 행 선택하고 우클릭 / Delete Row(s)

