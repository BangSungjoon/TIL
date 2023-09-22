
-- 스키마 (데이터베이스) 생성
CREATE SCHEMA sqldb1 DEFAULT CHARACTER SET utf8;
CREATE SCHEMA sqldb2 DEFAULT CHARACTER SET UTF8MB4;
CREATE DATABASE sqldb3 DEFAULT CHARACTER SET UTF8MB4;

-- 스키마 (데이터베이스) 삭제
DROP SCHEMA sqldb1;
DROP DATABASE sqldb2;
DROP DATABASE sqldb3;

-- -------------------------------------------------------
use sqldb1;


-- 테이블 생성
-- 제약 조건 
	-- 기본키 : prdNo, NOT NULL
    -- prdName : NOT NULL
CREATE TABLE product (
	prdNo VARCHAR(10) NOT NULL PRIMARY KEY,
    prdName VARCHAR(30) NOT NULL,
    prdPrice INT,
    pridComapny VARCHAR(30)
);

CREATE TABLE product2 (
	prdNo VARCHAR(10),
    prdName VARCHAR(30) NOT NULL,
    prdPrice INT,
    pridComapny VARCHAR(30),
    PRIMARY KEY(prdNo)
);

CREATE TABLE product3 (
	prdNo VARCHAR(10) NOT NULL,
    prdName VARCHAR(30) NOT NULL,
    prdPrice INT,
    pridComapny VARCHAR(30),
    CONSTRAINT PK_prduct_prdNo PRIMARY KEY (prdNo)
);

-- 기본키 / 외래키 제약조건 설정
-- publisher : 출판사 테이블
-- book : 도서 테이블

/*
	출판사 테이블 생성 (출판사번호, 출판사명)
    - 기본키로 pubNo 지정, NOT NULL
    - pubName은 NOT NULL로 설정
*/

CREATE TABLE publisher (
	pubNo VARCHAR(10) NOT NULL PRIMARY KEY,
    pubName VARCHAR(30) NOT NULL
);

/*
	도서 테이블 생성 (도서번호, 도서명, 가격, 발행일, 출판사번호)
    제약조건 설정
    - 기본키 : bookNo, NOT NULL
    - 외래키 : pubNo (참조하는 테이블과 기본키 지정)
    - bookPrice : 기본값 10000, 1000 보다 크게 설정
*/

CREATE TABLE book (
	bookNo VARCHAR(10) NOT NULL PRIMARY KEY,
    bookName VARCHAR(30) NOT NULL,
    bookPrice INT DEFAULT 10000 CHECK(bookPrice > 1000),
    bookDate DATE,
    pubNo VARCHAR(10) NOT NULL, -- 외래키로 사용하는 열이름 (필수)
    FOREIGN KEY (pubNo) REFERENCES publisher (pubNo)  -- 외래키 제약조건 설정
    -- FOREIGN KEY (현재 테이블의 열이름) REFERENCES 참조하는 테이블명 (참조테이블의 기본키)
);

CREATE TABLE book2 (
	bookNo VARCHAR(10) NOT NULL PRIMARY KEY,
    bookName VARCHAR(30) NOT NULL,
    bookPrice INT DEFAULT 10000 CHECK(bookPrice > 1000),
    bookDate DATE,
    pubNo VARCHAR(10) NOT NULL, -- 외래키로 사용하는 열이름 (필수)
    CONSTRAINT FK_book_publisher  FOREIGN KEY (pubNo) REFERENCES publisher (pubNo)  -- 외래키 제약조건 설정
    -- FOREIGN KEY (현재 테이블의 열이름) REFERENCES 참조하는 테이블명 (참조테이블의 기본키)
);

-- 테이블 상세 정보 확인
describe book;
-- PRI : 기본키
-- MUL : 중복 가능한 키 (외래키)

/*
	테이블 생성 및 기본키/외래키 제약조건 설정 연습문제
	- 학생(student)과 학과(department) 테이블 생성하고 데이터 입력 (각 3개씩)
		- 제약 조건
		- 기본키 / 외래키 설정
		- 학생은 학과에 소속
		- 학생명과 학과명은 NULL 허용하지 않음
		- 학년은 4를 기본값으로, 범위를 1~4로 설정
			(AND 키워드  사용)
*/

CREATE TABLE department(
	deptID VARCHAR(10) PRIMARY KEY,
    deptName VARCHAR(10) NOT NULL
);

CREATE TABLE student(
	stdID VARCHAR(10) PRIMARY KEY,
	stdName VARCHAR(10) NOT NULL,
	stdGrade INT DEFAULT 4 CHECK(stdGrade>=1 AND stdGrade<=4),
    deptID VARCHAR(10) NOT NULL,
    CONSTRAINT FK_student_department FOREIGN KEY (deptID) REFERENCES department(deptID)
);


/*
	테이블 생성 및 기본키/외래키 제약조건 설정 연습문제2
		부서(department) / 직원(employee) 테이블 생성
		기본키 / 외래키 설정
		직원은 부서에 소속
		직원명과 부서명은 NULL 허용하지 않음
*/

CREATE TABLE department2 (
	depNo VARCHAR(10) NOT NULL PRIMARY KEY,
    depName VARCHAR(30) NOT NULL
);

CREATE TABLE employee (
	empNo VARCHAR(10) NOT NULL PRIMARY KEY,
    empName VARCHAR(10) NOT NULL,
    depNo VARCHAR(10) NOT NULL,
    CONSTRAINT FK_department_no FOREIGN KEY (depNo) REFERENCES department2 (depNo)
);

/*
	테이블 생성 및 기본키/외래키 제약조건 설정 연습문제3
		카테고리(category) / 상품(product) 테이블 생성
		기본키 / 외래키 설정
		상품은 카테고리 별로 분류 
		카테고리명은 NULL 허용하지 않음
*/
CREATE TABLE category (
    ctgID INT NOT NULL PRIMARY KEY,
    ctgName VARCHAR(30) NOT NULL
);

CREATE TABLE product (
    productID INT NOT NULL PRIMARY KEY,
    productName VARCHAR(30) NOT NULL,
    ctgID INT NOT NULL,
    CONSTRAINT fk_product_category FOREIGN KEY (ctgID) REFERENCES category(ctgID)
);

/*
	테이블 생성 및 기본키/외래키 제약조건 설정 연습문제4
		- 그림과 같이 테이블 생성하고 기본키 외래키 설정
        - 5개 테이블 : 학과, 학생, 교수, 과목, 성적
*/
CREATE TABLE department(
	deptNo VARCHAR(10) PRIMARY KEY,
    deptName VARCHAR(30) NOT NULL,
    depPhone VARCHAR(13)
);

CREATE TABLE student(
	stdNo VARCHAR(10) PRIMARY KEY,
	stdName VARCHAR(30) NOT NULL,
	stdYear INT DEFAULT 4 CHECK(stdYear>=1 AND stdYear<=4),
    stdPhone VARCHAR(13),
    stdAddress VARCHAR(30),
    deptNo VARCHAR(10) NOT NULL,
    CONSTRAINT FK_student_department FOREIGN KEY (deptNo) REFERENCES department(deptNo)
);

CREATE TABLE professor(
	profID VARCHAR(10) PRIMARY KEY,
    profName VARCHAR(30) NOT NULL,
    profTel VARCHAR(10),
    deptNo VARCHAR(10) NOT NULL,
    CONSTRAINT FK_professor_department FOREIGN KEY (deptNo) REFERENCES department(deptNo)
);

CREATE TABLE course(
	courseId VARCHAR(10) PRIMARY KEY,
    courseTitle VARCHAR(30) NOT NULL,
    courseCredit INT,
    profID VARCHAR(10),
    CONSTRAINT FK_course_professor FOREIGN KEY (profID) REFERENCES professor(profID)
);

CREATE TABLE scores(
	stdNo VARCHAR(10) NOT NULL,
    courseId VARCHAR(10) NOT NULL,    
    score INT,
    grade VARCHAR(3),
    CONSTRAINT PK_scores_stdNo_courseId PRIMARY KEY(stdNo, courseId), -- 복합키
    CONSTRAINT FK_score_student FOREIGN KEY (stdNo) REFERENCES student(stdNo),
    CONSTRAINT FK_score_course FOREIGN KEY (courseId) REFERENCES course(courseId)
);




