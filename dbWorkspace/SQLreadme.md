# SQL

## 데이터베이스 기본 개념

### 데이터와 정보

⦁ **데이터 (Data)**<br>
	관찰이나 측정을 통해 수집된 사실(facts)이나 값(value)<br>
	정량적 또는 정성적인 실제값<br>
⦁ **정보 (Information)**<br>
	의사결정에 도움이 되도록 데이터를 의미 있는 패턴으로 정리한 것<br> 
    데이터에 의미를 부여한 것

### 데이터와 정보의 예

⦁ 데이터<br>
	한라산 1950 m 제주도 <br>
	지리산 1915 m 전북<br>
	반야봉 1732 m 전라남도<br>
	설악산 1708 m 강원도<br>
⦁ 정보<br>
	대한민국에서 가장 높은 산은 한라산

### 데이터 구조

⦁ 논리적 구조<br>
	사용자의 관점에서 본 데이터의 개념적 구조<br>
	데이터의 논리적 배치<br>
	논리적 레코드<br>
⦁ 물리적 구조<br>
	저장 관점에서 본 데이터의 물리적 배치<br>
	저장장치에 저장된 데이터의 실제 구조<br>
	물리적 레코드

### 데이터베이스

⦁ 데이터의 집합체<br>
⦁ 조직에 필요한 정보를 얻기 위해
	논리적으로 연관된 데이터를 모아서
	구조적으로 통합해 놓은 것<br>
⦁ 여러 사용자나 응용프로그램이 공유<br>
⦁ 동시 접근 가능

### 데이터베이스 관리 시스템 (DBMS)

⦁ 데이터 베이스를 관리해주는 소프트웨어 시스템<br>
⦁ Oracle, MS SQL, MS SQL, ….

### 데이터 중복의 최소화

동일한 데이터가 여러 개 중복되어 저장되는 것 방지

### 데이터의 독립성

프로그램과 데이터 분리 <br>데이터베이스 크기를 변경하거나 데이터 파일의 저장소 변경 시 기존에 작성된 응용 프로그램에는 영향을 미치지 않도록 데이터의 독립성 보장한다.

### 데이터의 안전성 향상

⦁ 대부분의 DBMS가 제공하는 백업·복원 기능 이용<br>
⦁ 데이터가 손상되는 문제가 발생할 경우 원상으로 복원, 복구하는 방법이 명확해짐

### 데이터의 무결성 (Integrity)

⦁ 데이터베이스 안의 데이터는 오류가 없어야 하고 데이터베이스에 저장된 데이터 값과 표현하는 현실 세계의 실제 값이 일치해야 함<br>
⦁ 데이터가 상호 간에 모순성이 없고, 현실 세계에 모순되지 않도록 데이터 유지

### 데이터 무결성 해결 방법

데이터베이스 시스템에서는 이러한 오류를 방지하기 위해 외래키(FK)를 사용하여 테이블 간의 모순성 배제

⦁ 무결성 제약 조건<br>
⦁ 보안<br>
⦁ 데이터 추상화<br>
⦁ 다양한 뷰 제공

## DBMS의 언어

### 데이터베이스 언어

데이터베이스를 구축하고 이용하기 위한 데이터베이스 관리 시스템과의 통신 수단

### 데이터 정의어 (DDL : Data Definition Language)

```sql
CREATE / ALTER / DROP
-- 데이터베이스 구조 정의를 위한 언어
```

### 데이터 조작어 (DML : Data Manipulation  Language)

```sql
INSERT / DELETE / UPDATE / SELECT
/* 데이터 처리를 위해 응용프로그램과 
   데이터베이스 관리 시스템 간의 인터페이스를 위한 언어 */
```

### 데이터 제어어 (DCL : Data Control Language)

```sql
GRANT / REVOKE / COMMIT / ROLLBACK
/* 보안 및 권한 제어, 데이터 무결성, 복구, 
   병행 제어 등을 위한 언어 */
```

## 관계형 데이터베이스

### 관계형 데이터 모델

데이터를 2차원 테이블 형태인 **릴레이션** 구조로 표현하는 
논리적 데이터 모델

### 릴레이션(테이블) 스키마 – 구조

릴레이션에 데이터를 넣을 수 있도록 하는 릴레이션 틀
릴레이션(테이블) 이름, 속성(열) 이름, 속성값의 도메인 정의

### 속성 (Attribute)

데이터베이스를 구성하는 가장 작은 논리적 단위
테이블의 열 (Column)
개체의 특성, 상태 등 기술
파일 구조의 데이터 필드에 해당

### 도메인 (Domain)

테이블에서 하나의 속성(열)이 취할 수 있는 같은 타입의 원자(Atomic)값들의 집합
속성값의 적법 여부를 검사하는데 이용

### 행 (Tuple)

테이블의 행 (Row) (데이터 행)
최소 하나의 열은 달라야 함 - 기본키

---

### 제약 (Constraints)

데이터베이스에 저장되는 데이터에 대한 규칙
데이터 무결성을 유지하기 위한 방법이다.

### 관계 데이터 제약

1. 키
2. 무결성 제약 조건

### 키 (Key)

릴레이션(테이블)을 구성하는 각 튜플(행)을 속성(열)값에 의해 유일하게 식별할 수 있게 해주는 속성(열) 또는 속성(열)의 집합

1. **기본키 (주 키, Primary Key, PK)**
한 테이블에서 모든 튜플(행)을 유일하게 구별할 수 있는 수 있는 속성(열)
NOT NULL, 중복 불가, 키 값 변동 불가
2. **외래키 (Foreign Key, FK)**
다른 테이블의 기본키를 참조하는 속성(열)
테이블 간의 관계(relationship) 표현에 사용
NULL 값과 중복값 허용, 참조하는 값이 바뀌면 변동 가능
3. **후보키**
특수한 역할을 가진 키가 아닌 일반 적인 속성
4. **대체키**
기본키를 대신하여 역할을 수행할 수 있는 키
5. **복합키**
단일 속성 중 유일한 값을 가진 키가 없을 때
****여러 개의 속성(열)을 묶어서 기본키로 사용하는 키

## MySQL 사용법

### 데이터베이스 / 테이블 생성

데이터베이스 (스키마) 생성
MySQL에서는 데이터베이스와 스키마가 동일한 의미로 사용
root 권한으로 생성

### 스키마 생성

1. Schema 탭에서 우클릭 / Create Schema
2. Name : shopdb (소문자)
3. CharacterCollation : utf-8
4. Default Collation 기본 그대로 둠
5. 스키마 이름에 대문자가 포함되면, 소문자로 변경하겠다는 알림창
6. Apply (코드 자동 생성)
7. Finish
8. (잘못 만들었으면 삭제하면 됨 )
우클릭  / Drop Schema

```sql
CREATE SCHEMA -- 스키마 생성
DROP SCHEMA   -- 스키마 삭제
```

### 데이터 정의어 (DDL)

테이블 생성 CREATE

```sql
CREATE TABLE 테이블명 (
		열이름 데이터타입(크기) [제약조건]
	);

CREATE TABLE product(
	prdNo VARCHAR(10) NOT NULL PRIMARY KEY,
	prdName VARCHAR(30) NOT NULL
);
```

참조 무결성 제약 조건 : 외래키 값을 입력할 때는 참조되는 테이블의 기본키로서의 값과 동일해야 함

테이블 수정 ALTER

```sql
-- 기본키 / 외래키 삭제
ALTER TABLE 테이블명 DROP PRIMARY KEY;
ALTER TABLE 테이블명 DROP FOREIGN KEY 키이름;

-- 기본키 / 외래키 추가
ALTER TABLE 테이블명 ADD PRIMARY KEY (열이름);
ALTER TABLE 테이블명 ADD FOREIGN KEY (열이름) REFERENCES 참조테이블명 (기본키 열이름);
```

ON DELETE CASCADE : 기준 테이블의 데이터가 삭제되었을 때, 외래키로 지정된 테이블의 데이터도 자동으로 삭제되도록 설정한다.

테이블 삭제 DROP

```sql
-- 테이블 삭제
DROP TABLE;
```

---

### 데이터 조작어 (DML)

데이터 입력 INSERT

```sql
INSERT INTO 테이블명(열이름 리스트) VALUES(값 리스트)
INSERT INTO student(stdNo, stdName, stdYear) VALUES('2023001', '홍길동', 1)
```

데이터 임포트 : CSV 파일을 읽어서 테이블 자동 생성 및 입력<br>
[Table Data Import Wizard] / 파일 선택 / 테이블명 / 데이터 타입 설정

데이터 수정 UPDATE

```sql
-- 조건에 맞는 행을 찾아서 열의 값 수정
UPDATE 테이블명 SET 열=값 WHERE 조건;
UPDATE product SET prdName= 'UHD TV'  WHERE predNo='5';
```

데이터 삭제 DELETE

```sql
-- 테이블에 있는 기존 행을 삭제하는 명령어
DELETE FROM 테이블명 WHERE 조건;
DELETE FROM product WHERE prdName='그늘막 텐트';
-- 테이블의 모든 행 삭제
DELETE FROM product;
```

데이터 검색 SELECT

```sql
SELECT [ALL|DISTINCT] 열이름 리스트  -- DISTINCT : 중복 제거
FROM 테이블명
[WHERE 검색조건(들)]
[GROUP BY 열이름]
[HAVING 검색조건(들)]
[ORDER BY 열이름 [ASC|DESC]]

-- [ ]안의 부분은 생략해도 상관없으나 순서는 반드시 지켜져야 한다.
```

- GROUP BY 절<BR>
그룹 쿼리를 기술할 때 사용<bR>
특정 열로 그룹화 한 후 각 그룹에 대해 한 행 씩 쿼리 결과 생성
- HAVING 절<br>
GROUP BY 절에 의해 구성된 그룹들에 대해 적용할 조건 기술<BR>
검색 조건에는 집계 함수가 와야 한다<BR>
반드시! GROUP BY 절과 함께 사용!
- ORDER BY 절
특정 열의 값을 기준으로 쿼리 결과 정렬<BR>
ASC : 오름차순 (디폴트 : 생략 가능)<BR>
DESC : 내림차순
---
테이블 결합 JOIN

```sql
INNER JOIN (내부 조인) : 가장 많이 사용
양쪽 테이블에 공통되는 열이 있을 때
OUTER JOIN (외부 조인) : 공통되는 열이 없을 때
```

뷰 (View) <br>
⦁	테이블의 일부를 추출하여 별도의 테이블로 생성한 가상 테이블<br>
⦁	실제 데이터를 저장하는 것이 아니라 다른 테이블의 내용을 보여주는 역할 <br>
⦁	다양한 형태의 뷰로 사용자에게 필요한 데이터 세트 제공<br>
⦁	뷰를 통한 데이터 수정 및 삭제 가능 (단 접근 가능한 데이터만 변경 가능)<br>
뷰의 장점<br>
⦁	보안성 : 사용자별로 접근 권한 다르게 뷰 생성<br>
⦁	복잡한 쿼리 단순화<br>
⦁	자중 사용되는 쿼리문을 뷰로 만들어 놓고 여러 번 사용
