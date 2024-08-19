# CSS

Cascading Style Sheet
웹 페이지의 디자인과 레이아웃을 구성하는 언어

### CSS 구문

```html
h1 {                   # 선택자
	color: red;          # 선언
	font-size: 30px;     # 속성(Property) : 값(Value)
}
```

- 하나의 구문이 끝나고 내려갈 때 `;` 꼭 붙이기 (문장의 종료)
- 들여쓰기는 html과 마찬가지로 의미 없다.

### 인라인(Inline) 스타일

- HTML 요소 안에 style 속성 값으로 작성

```html
<body>
	<h1 style="color: blue, background-color: yellow;">Hello World!</h1>
</body>
```

- 권장하지 않음

### 내부(Internal) 스타일 시트

- head 태그 안에 style 태그에 작성

```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    h2 {
      color: red;
    }
  </style>
</head>

<body>
  <h2>Internal Style</h2>
</body>
```

### 외부(External) 스타일 시트

- 별도 CSS 파일 생성 후 HTML link 태그를 사용해 불러오기

```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style.css">
  <title>Document</title>
</head>

<body>
  <h3>External Style</h3>
</body>
```

---

### CSS Selectors(선택자) 종류

- 기본 선택자
    - 전체(*) 선택자
    - 요소(tag) 선택자
    - 클래스(class) 선택자 (’.’ (dot))
        - 주어진 클래스 속성을 가진 모든 요소를 선택
    - 아이디(id) 선택자 (’#’)
        - 주어진 아이디 속성을 가진 요소 선택
        - 문서에는 주어진 아이디를 가진 요소가 하나만 있어야 함
    - 속성(attr) 선택자 등
- 결합자 (Combinators)
    - 자손 결합자 (” “ (space) )
        - 첫 번째 요소의 자손 요소들 선택
        - 예) p span은 <p> 안에 있는 모든 <span>를 선택 (하위 레벨 상관 없이)
    - 자식 결합자 (”>”)
        - 첫 번째 요소의 직계 자식만 선택
        - 예) ul > li은 <ul> 안에 있는 모든 <li>를 선택 (한단계 아래 자식들만)
- 코드
    
    ```html
    <!DOCTYPE html>
    <html lang="en">
    
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
      <style>
        * {
          color: red;
        }
    
        h2 {
          color: orange;
        }
    
        h3,
        h4 {
          color: blue;
        }
    
        /* 클래스 선택자 */
        .green {
          color: green;
        }
        /* 아이디 선택자 */
        #purple {
          color: purple;
        }
    
        /* 자식 결합자 */
        .green > span {
          font-size: 50px;
        }
        .green li {
          color: brown;
        }
      </style>
    </head>
    
    <body>
      <h1 class="green">Heading</h1>
      <h2>선택자</h2>
      <h3>연습</h3>
      <h4>반가워요</h4>
      <p id="purple">과목 목록</p>
      <ul class="green">
        <li>파이썬</li>
        <li>알고리즘</li>
        <li>웹
          <ol>
            <li>HTML</li>
            <li>CSS</li>
            <li>PYTHON</li>
          </ol>
        </li>
      </ul>
      <p class="green">Lorem, <span>ipsum</span> dolor.</p>
    </body>
    
    </html>
    
    ```
    

### Specificity 명시도

- CSS Selector에 가중치를 계산하여 어떤 스타일을 적용할지 결정
    - 동일한 요소를 가리키는 2개 이상의 CSS 규칙이 있는 경우 가장 높은 명시도를 가진 Selector가 승리하여 스타일이 적용
- 계단식
    - 한 요소에 동일한 가중치를 가진 선택자가 적용될 때 CSS에서 마지막에 나오는 선언이 사용됨
- 예시
    - 동일한 h1 태그에 다음과 같이 스타일이 작성된다면 h1 태그 내용의 색은 red가 적용됨
    
    ```css
    .make-red {
    	color: red;
    }
    
    h1 {
    	color: purple;
    }
    ```
    
- 명시도가 높은 순
    1. Importance
        - `!important`
        - 다른 우선순위 규칙보다 우선하여 적용하는 키워드
            - Cascade의 구조를 무시하고 강제로 스타일을 적용하는 방식이므로 사용을 권장하지 않음
    2. Inline 스타일
    3. 선택자
        - id 선택자 > **class 선택자** > 요소 선택자
    4. 소스 코드 선언 순서
    
    <aside>
    💡 앞으로 코드를 작성할 땐 class 선택자만 사용하자!
    우선 순위를 고려할 필요가 없어짐
    
    </aside>
    
    - 코드
        
        ```html
        <!DOCTYPE html>
        <html lang="en">
        
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Document</title>
          <style>
            h2 {
              color: darkviolet !important;
            }
        
            p {
              color: blue;
            }
        
            .orange {
              color: orange;
            }
        
            .green {
              color: green;
            }
        
            #red {
              color: red;
            }
          </style>
        </head>
        
        <body>
          <p>1</p>
          <p class="orange">2</p>
          <p class="green orange">3</p>           <!-- 명시도가 같다면 css의 선언이 아래 있는 것으로 -->
          <p class="orange green">4</p>           <!-- 3번과 4번의 색상은 같다 -->
          <p id="red" class="orange">5</p>
          <h2 id="red" class="orange">6</h2>
          <p id="red" class="orange" style="color: brown;">7</p>
          <h2 id="red" class="orange" style="color: brown;">8</h2>
        </body>
        
        </html>
        ```
        

---

## 상속

- 기본적으로 CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속해 재사용성을 높임

### CSS 속성 2가지 분류

- 상속 되는 속성
    - Text 관련 요소 (font, color, text-align), opacity, visibility 등
- 상속 되지 않는 속성
    - Box model 관련 요소 (width, height, border, box-sizing….)
    - position 관련 요소 (position, top/right/bottom/left, z-index) 등
- 코드
    
    ```html
    <!DOCTYPE html>
    <html lang="en">
    
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
      <style>
        .parent {
          /* 상속 O */
          color: red;
    
          /* 상속 X */
          border: 1px solid black;
        }
      </style>
    </head>
    
    <body>
      <ul class="parent">
        <li class="">Hello</li>
        <li class="">Bye</li>
      </ul>
    </body>
    
    </html>
    
    ```
    

---

## 박스 타입

1. Block box
2. Inline box

→ 박스 타입에 따라 페이지에서의 배치 흐름 및 다른 박스와 관련하여 박스가 동작하는 방식이 달라짐

### 박스 표시(Display) 타입

1. Outer display type
    - Block & Inline (예전 잡지의 구성을 떠올리자)
    - 박스가 문서 흐름에서 어떻게 동작할지를 결정
    - 속성
        - block, inline → 구조를 나타낸다면 block, 요소를 나타낸다면 inline
    - block 특징
        - 항상 새로운 행으로 나뉨
        - width와 height 속성 사용 가능
        - padding, margin, border로 인해 다른 요소를 상자로부터 밀어냄
        - width 속성을 지정하지 않으면 박스는 inline 방향으로 사용 가능한 공간을 모두 차지함
            - 상위 컨테이너 너비 100%로 채우는 것
        - 대표적인 block 타입 태그
            - h1~6, p, div
    - Inline 특징
        - 새로운 행으로 넘어가지 않음
        - width와 height 속성을 사용할 수 없음
        - 수직 방향
            - padding, margin, border가 적용되지만 다른 요소를 밀어낼 수는 없음
        - 수평 방향
            - padding, margins, borders가 적용되어 다른 요소를 밀어낼 수 있음
        - 대표적인 inline 타입 태그
            - a, img, span, strong, em
2. Inner display type

---

## 참고

### HTML 스타일 가이드

- 대소문자 구분
    - HTML은 대소문자를 구분하지 않지만, 소문자 사용을 강력히 권장
    - 태그명과 속성명 모두 소문자 작성
- 속성 따옴표
    - 속성 값에는 큰 따옴표(”)를 사용하는 것이 일반적
- 공백 처리
    - HTML은 연속된 공백을 하나로 처리
    - Enter키로 줄 바꿈을 해도 브라우저에서 인식하지 않음 (줄 바꿈 태그를 사용해야 함)
- 에러 출력 없음
    - HTML은 문법 오류가 있어도 별도의 에러 메시지를 출력하지 않음
- 코드 구조와 포맷팅
    - 일관된 들여쓰기를 사용 (보통 2칸 공백)
    - 각 요소는 한 줄에 하나씩 작성
    - 중첩된 요소는 한 단계 더 들여쓰기

### CSS 스타일 가이드

- 코드 구조와 포맷팅
    - 일관된 들여쓰기를 사용 (보통 2칸 공백)
    - 선택자와 속성은 각각 새줄에 작성
    - 중괄호 앞에 공백 넣기
    - 속성 뒤에는 콜론(:)과 공백 넣기
    - 마지막 속성 뒤에는 세미콜론(;) 넣기
- 선택자 사용
    - class 선택자를 우선적으로 사용
    - id, 요소 선택자 등은 가능한 피할 것
        - 여러 선택자들이 함께 사용할 경우 우선순위 규칙에 따라 예기치 못한 스타일 규칙이 적용되어 전반적인 유지보수가 어려워지기 때문
    - 속성과 값
        - 속성과 값은 소문자로 작성
        - 0 값에는 단위를 붙이지 않음

### MDN Web Docs

Mozilla Developer Network에서 제공하는 온라인 문서로, 웹 개발자와 디자이너를 위한 종합적인 참고 자료

- HTML, CSS, JavaScript, 웹 API, 개발 도구 등 웹 기술에 대한 정보를 제공
- MDN 문서를 활용해야 하는 이유
    - 정확성 및 신뢰성
        - Mozilla와 웹 커뮤니티의 전문가들에 의해 작성되고 유지 관리
        - 웹 표준을 정확하게 반영하고 있으며, 신뢰할 수 있는 정보 소스를 제공
    - 최신 웹 기술
        - 최신 웹 표준과 기술을 다루고 있어, 웹 개발자들이 최신 정보를 쉽게 접할 수 있음
    - 명확한 설명과 예제
        - 복잡한 개념을 이해하기 쉽게 설명하고, 실습 가능한 예제 코드를 제공
- MDN 문서는 웹 개발 학습의 모든 단계에서 중요한 참고 자료
- 개발 과정에서 발생하는 다양한 문제에 대한 솔루션을 찾는데 유용
- 이 문서를 활용함으로써, 웹 기술에 대한 깊은 이해를 얻고, 실무에 필요한 능력을 갖출 수 있음