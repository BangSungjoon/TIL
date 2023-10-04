-- 모델링 연습문제
/*
	- 스키마 생성 : modeling_db
    - 테이블 생성 (속성 임의로 설정)
		member : 
        category : 번호 / 카테고리명
        product : 
        cart : 장바구니
        order_info : 주문정보 (수령인, 주소, 전화)
        order_product : 주문한 상품정보
	- ER 다이어그램 생성
*/
-- 스키마 생성
CREATE DATABASE IF NOT EXISTS modeling_db;
USE modeling_db;

-- 회원 정보 테이블
CREATE TABLE member (
    member_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 카테고리 테이블
CREATE TABLE category (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(50) NOT NULL
);

-- 상품 테이블
CREATE TABLE product (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES category(category_id)
);

-- 장바구니 테이블
CREATE TABLE cart (
    cart_id INT PRIMARY KEY AUTO_INCREMENT,
    member_id INT,
    product_id INT,
    quantity INT NOT NULL,
    FOREIGN KEY (member_id) REFERENCES member(member_id),
    FOREIGN KEY (product_id) REFERENCES product(product_id)
);

-- 주문 정보 테이블
CREATE TABLE order_info (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    member_id INT,
    recipient_name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (member_id) REFERENCES member(member_id)
);

-- 주문한 상품 정보 테이블
CREATE TABLE order_product (
    order_id INT,
    product_id INT,
    quantity INT NOT NULL,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES order_info(order_id),
    FOREIGN KEY (product_id) REFERENCES product(product_id)
);


















