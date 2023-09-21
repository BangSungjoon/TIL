-- 스키마 (데이터베이스) 생성
CREATE SCHEMA sqldb1 DEFAULT CHARACTER SET utf8; 
CREATE SCHEMA sqldb2 DEFAULT CHARACTER SET utf8mb4;

-- 스키마 (데이터베이스) 삭제
DROP SCHEMA sqldb1;
DROP DATABASE sqldb2;

-- ------------------------------------------------------------
use sqldb1;

-- 테이블 생성
-- 제약 조건
	-- 기본키 : prdNo, NOT NULL
    -- prdName : NOT NULL
CREATE TABLE product (
	prdNo VARCHAR(10) NOT NULL PRIMARY KEY,
    prdName VARCHAR(30) NOT NULL,
    prdPrice INT,
    pridCompany VARCHAR(30)
);

CREATE TABLE product2 (
	prdNo VARCHAR(10)  NOT NULL,
    prdName VARCHAR(30) NOT NULL,
    prdPrice INT,
    pridCompany VARCHAR(30)
    PRIMARY KEY(prdNo)
);

-- 기본키 / 외래키 제약조건 설정
-- publisher : 출판사 테이블
-- book : 도서 테이블

/*
	출판사 테이블 생성 (출판사번호, 출판사명)
    - 기본키로 pubNo 지정, NOT NULL
    - pubName은 NOT NULL로 설정
*/

create table publisher (
	pubNo varchar(10) not null primary key,
    pubName varchar(30) not null
);

/* 
	도서 테이블 생성 (도서번호, 도서명, 가격, 발행일, 출판사번호)
    제약조건 설정
    - 기본키 : bookNo, NOT NULL
    - 외래키 : pubNo (참조하는 테이블과 기본키 지정)
    - bookPrice : 기본값 10000, 1000보다 크게 설정
*/

CREATE TABLE book (
	bookNo VARCHAR(10) NOT NULL PRIMARY KEY,
    bookName VARCHAR(30) NOT NULL,
    bookPrice INT DEFAULT 10000 CHECK(bookPrice > 1000),
    bookDate DATE,
    pubNo VARCHAR(10) NOT NULL,  -- 외래키로 사용하는 열 이름 (필수)
	FOREIGN KEY (pubNo) REFERENCES publisher (pubNo) -- 외래키 제약조건 설정
    -- FOREIGN KEY (현재 테이블의 열이름) REFERENCES 참조하는 테이블명
);

CREATE TABLE book2 (
	bookNo VARCHAR(10) NOT NULL PRIMARY KEY,
    bookName VARCHAR(30) NOT NULL,
    bookPrice INT DEFAULT 10000 CHECK(bookPrice > 1000),
    bookDate DATE,
    pubNo VARCHAR(10) NOT NULL,  -- 외래키로 사용하는 열 이름 (필수)
	CONSTRAINT FK_book_publisher FOREIGN KEY (pubNo) REFERENCES publisher (pubNo) -- 외래키 제약조건 설정
);

-- 테이블 상세 정보 확인
describe book;


-- 테이블 생성 및 기본키/외래키 제약조건 설정 연습문제
-- 학생(student)과 학과 (department) 테이블 생성하고 데이터 입력 (각 3개씩)
-- 제약 조건
	-- 기본키 / 외래키 설정
    -- 학생은 학과에 소속
    -- 학생명과 학과명은 NULL 허용하지 않음
    -- 학년은 4를 기본값으로, 범위를 1~4로 설정
		-- (AND 키워드 사용)

create table department (
	departNo varchar(10) not null primary key,
    departName varchar(30) not null
);

CREATE TABLE student (
	stNo VARCHAR(10) NOT NULL PRIMARY KEY,
    stName VARCHAR(30) NOT NULL,
    stGrade INT DEFAULT 4 CHECK(stGrade >= 1 AND stGrade <= 4),
    departNo VARCHAR(10) NOT NULL,  
	FOREIGN KEY (departNo) REFERENCES department (departNo) 
);

-- 테이블 생성 및 기본키/외래키 제약조건 설정 연습문제2

create table department2 (
	departNo varchar(10) not null primary key,
    departName varchar(30) not null
);

CREATE TABLE employee (
	emNo VARCHAR(10) NOT NULL PRIMARY KEY,
    emName VARCHAR(30) NOT NULL,
    departNo VARCHAR(10) NOT NULL,  
	CONSTRAINT FK_employee_department FOREIGN KEY (departNo) REFERENCES department2 (departNo) 
);

-- 테이블 생성 및 기본키/외래키 제약조건 설정 연습문제3

create table category (
	cateNo varchar(10) not null primary key,
    cateName varchar(30) not null
);

CREATE TABLE product (
	prNo VARCHAR(10) NOT NULL PRIMARY KEY,
    prName VARCHAR(30) NOT NULL,
    cateNo VARCHAR(10) NOT NULL,  
    prdCompany VARCHAR(10) NOT NULL,  
	CONSTRAINT FK_product_category FOREIGN KEY (cateNo) REFERENCES category (cateNo) 
);


-- 테이블 생성 및 기본키/외래키 제약조건 설정 연습문제4
CREATE TABLE department3 (
	dptNo INT not null primary key,
    dptName VARCHAR(30) NOT NULL,
    dptPhone VARCHAR(20) NOT NULL
);

CREATE TABLE student (
	stdNo INT not null primary key,
    stdName VARCHAR(20) NOT NULL,
    stdYear INT NOT NULL DEFAULT 4 CHECK(stGrade >= 1 AND stGrade <= 4),
    stdPhone VARCHAR(20) NOT NULL,
    stdAddress VARCHAR(30) NOT NULL,
    dptNo INT not null,
    FOREIGN KEY (dptNo) REFERENCES department3 (dptNo) 
);

CREATE TABLE professor (
	profId INT not null primary key,
    profName VARCHAR(30) NOT NULL,
    profTel VARCHAR(30) NOT NULL,
    profGrade VARCHAR(30) NOT NULL,
    dptNo INT not null,
    FOREIGN KEY (dptNo) REFERENCES department3 (dptNo) 
); 

CREATE TABLE course (
	courseId INT not null primary key,
    coureTitle VARCHAR(30) NOT NULL,
    courseCredit VARCHAR(30) NOT NULL,
    profId INT not null,
    FOREIGN KEY (profId) REFERENCES professor (profId) 
);

CREATE TABLE score (
	score VARCHAR(30) NOT NULL,
    grade VARCHAR(10) NOT NULL,
    stdNo INT not null,
    courseId INT not null,
    CONSTRAINT FK_studio_no FOREIGN KEY (stdNo) REFERENCES student (stdNo),
	CONSTRAINT FK_course_no FOREIGN KEY (courseId) REFERENCES course (courseId)
);

-- 자동 증가
CREATE TABLE board(
	boardNo INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    boardTitle VARCHAR(30) NOT NULL,
    boardWriter VARCHAR(30) NOT NULL,
    boardContent VARCHAR(30) NOT NULL
);
