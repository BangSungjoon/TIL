# Templates & URLs

## Django Template system

<aside>
💡

데이터 표현을 제어하면서, 표현과 관련된 부분을 담당

</aside>

### HTML의 콘텐츠를 변수 값에 따라 변경하기

```python
# views
def index(request):
    context = {
        'name': 'alice',
    }
    return render(request, 'articles/index.html', context)
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>안녕하세요! {{ name }}</h1>
</body>
</html>
```

### Django Template Language (DTL)

Template에서 조건, 반복, 변수 등의 프로그래밍적 기능을 제공하는 시스템

1. Variable
    - render 함수의 세번째 인자로 딕셔너리 데이터를 사용
    - 딕셔너리 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨
    - dot(’.’)를 사용하여 변수 속성에 접근할 수 있음
    - `{{ variable }}`
    - `{{ variable.attribute }}`
2. Filters
    - 표시할 변수를 수정할 때 사용 (변수 + ‘|’ + 필터)
    - chained(연결)이 가능하며 일부 필터는 인자를 받기도 함
    - 약 60개의 built-in template filters를 제공
    - `{{ variable|filter }}`
    - `{{ name|truncatewords:30 }}`
3. Tags
    - 반복 또는 논리를 수행하여 제어 흐름을 만듦
    - 일부 태그는 시작과 종료 태그가 필요
    - 약 24개의 built-in template tags를 제공
    - `{% tag %}`
    - `{% if %} {% endif %}`
4. Comments
    - DTL에서의 주석
    
    ```html
    <h1>hello, {# name #}</h1>
    
    {% comment %}
    	...
    {% endcomment %}
    ```
    

### 코드

```python
# views.py
def dinner(request):
    foods = ['국밥', '국수', '카레', '탕수육',]
    picked = random.choice(foods)
    context = {
        'foods':foods,
        'picked': picked,
    }
    return render(request, 'articles/dinner.html', context)
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>dinner</h1>
    <p>{{ picked }} 메뉴는 {{ picked|length }}글자 입니다.</p>
    <ul>
        {% for food in foods %}
            <li>{{ food }}</li>
        {% endfor %}
    </ul>

    {% if foods|length == 0 %}
        <p>메뉴가 소진 되었습니다.</p>
    {% else %}
        <p>아직 메뉴가 남았습니다.</p>
    {% endif %}
</body>
</html>
```

## 템플릿 상속

### Template inheritance

<aside>
💡

페이지의 공통 요소를 포함하고, 하위 템플릿이 재정의 할 수 있는 공간을 정의하는 기본 ‘skeleton’ 템플릿을 작성하여 상속 구조를 구축

</aside>

### ‘extends’ tag

`{% extends 'path' %}` 

- 자식(하위) 템플릿이 부모 템플릿을 확장한다는 것을 알림
    - 반드시 자식 템플릿이 최상단에 작성되어야 함 (2개 이상 사용 불가)

### ‘block’ tag

`{% block name %}{% endblock name %}` 

- 하위 템플릿에서 재정의 할 수 있는 블록을 정의
    - 상위 템플릿에 작성하며 하위 템플릿이 작성할 수 있는 공간을 지정하는 것

### 코드

```html
{% comment %} base.html {% endcomment %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>
<body>
    {% block content %}
    {% endblock content %}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>
</html>
```

```html
{% extends "articles/base.html" %}

{% block content %}
  <h1>안녕하세요! {{ name }}</h1>
{% endblock content %}
```

## 요청과 응답

### HTML form

<aside>
💡

HTML ‘form’은 HTTP 요청을 서버에 보내는 가장 편리한 방법

</aside>

- ‘form’ element
    - 사용자로부터 할당된 데이터를 서버로 전송
    - 웹에서 사용자 정보를 입력하는 여러 방식 (text, password, checkbox 등)을 제공

```html
{% extends "articles/base.html" %}

{% block content %}
    <h1>Fake Naver</h1>
    <form action="https://search.naver.com/search.naver" method='GET'>
        <input type="text" name="query">
        <input type="submit">
    </form>
{% endblock content %}
```

### ‘action’ & ‘method’

- action
    - 입력 데이터가 전송될 URL을 지정 (목적지)
    - 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐
- method
    - 데이터를 어떤 방식으로 보낼 것인지 정의
    - 데이터의 HTTP request methods (GET, POST)를 지정

### ‘input’ element

사용자의 데이터를 입력 받을 수 있는 요소

- type 속성 값에 따라 다양한 유형의 입력 데이터를 받음
- 핵심 속성 - ‘name’

### ‘name’ attribute

- input의 핵심 속성
- 사용자가 입력한 데이터에 붙이는 이름(key)
- 데이터를 제출했을 때 서버는 name 속성에 설정된 값을 통해서만 사용자가 입력한 데이터에 접근할 수 있음

### Query String Parameters

- 사용자의 입력 데이터를 URL 주소에 파라미터를 통해 서버로 보내는 방법
- 문자열은 앰퍼샌드(’&’)로 연결된 key=value 쌍으로 구성되며, 기본 URL과는 물음표(’?’)로 구분됨
- 예시
    - http://host:port/path?key=value&key=vlaue

### HTTP request 객체

form으로 전송한 데이터 뿐만 아니라 Django로 들어오는 모든 요청 관련 데이터가 담겨 있음

- view 함수의 첫번째 인자로 전달 됨
- request 객체에서 form 데이터 추출
    - `request.GET.get('message')`

### throw - catch 간 요청과 응답 정리 (1/2)

1. throw/ 로 요청 (throw 페이지를 줘!)
2. throw/ 문자열과 일치하는 urls.py의 path 함수 호출
3. throw view 함수 호출
4. thorw view 함수가 응답 객체 반환
5. 응답 객체 전달
6. 응답 객체 해석 후 화면 출력

### throw - catch 간 요청과 응답 정리 (2/2)

1. throw 페이지에서 form 데이터 작성 후 제출
    - form 요소의 action 속성 값으로 요청
2. catch/ 로 요청 (+ 사용자 입력 데이터와 함께)
3. catch/ 문자열과 일치하는 urls.py의 path 함수 호출
4. catch view 함수 호출
5. catch view 함수에서 사용자가 보낸 form 데이터 추출 후 응답 객체를 반환
6. 응답 객체 전달
7. 응답 객체 해석 후 화면 출력

## Django URLs

### URL dispatcher

- 운항 관리자, 분배기
- URL 패턴을 정의하고 해당 패턴이 일치하는 요청을 처리할 view 함수를 연결(매핑)

### Variable Routing

- URL 일부에 변수를 포함시키는 것
- 변수는 view 함수의 인자로 전달 할 수 있다.
- 작성법
    - `<path_converter:variable_name>`

### Path converters

- URL 변수의 타입을 지정
- str, int 등 5가지 타입 지원

### App URL mapping

- 각 앱에 URL을 정의하는 것
- 프로젝트와 각 앱이 URL을 나누어 관리를 편하게 하기 위함