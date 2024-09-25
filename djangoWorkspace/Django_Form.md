# Django Form

## 개요

### HTML ‘form’

- 지금까지 사용자로부터 데이터를 제출 받기 위해 활용한 방법
- 그러나 비정상적 혹은 악의적인 요청을 필터링 할 수 없음
    - 유효한 데이터 인지에 대한 확인이 필요

### 유효성 검사

- 수집한 데이터가 정확하고 유효한지 확인하는 과정
- 유효성 검사 구현의 어려움
    - 유효성 검사를 구현하기 위해서는 입력 값, 형식, 중복, 범위, 보안 등 많은 것들을 고려해야 함
    - 이런 과정과 기능을 직접 개발하는 것이 아닌 Django가 제공하는 Form을 사용

## Django Form

<aside>
💡

사용자 입력 데이터를 수집하고, 처리 및 유효성 검사를 수행하기 위한 도구

→ 유효성 검사를 단순화하고 자동화 할 수 있는 기능을 제공

</aside>

### Form class 정의

```python
# articles/forms.py

from django import forms

class ArticleForm(forms.Form):
	title = forms.CharField(max_length=10)
	content = forms.CharField()
```

### Form class를 적용한 new 로직

- view함수 new 변경
    
    ```python
    # articles/views.py
    
    from .forms import ArticleForm
    
    def new(request):
    	form = ArticleForm()
    	context = {
    		'form': form,
    	}
    	return render(request, 'articles/new.html', context)
    ```
    
- new 페이지에서 form 인스턴스 출력
    
    ```html
    <!-- articles/new.html -->
    
    <h1>NEW</h1>
    <form action="{% url 'articles:create' %}" method="POST">
    	{% csrf token %}
    	{{ form }}
    	<input type="submit">
    </form>
    ```
    

### Form rendering options

- label, input 쌍을 특정 HTML 태그로 감싸는 옵션
    
    ```html
    <!-- articles/new.html -->
    
    <h1>NEW</h1>
    <form action="{% url 'articles:create' %}" method="POST">
    	{% csrf_token %}
    	{{ form.as_p }}
    	<input type="submit">
    </form>
    ```
    

## Widgets

<aside>
✅

HTML ‘input’ element의 표현을 담당

</aside>

### widget 적용

- Widget은 단순히 input 요소의 속성 및 출력 되는 부분을 변경하는 것
    
    ```python
    # articles/forms.py
    
    from django import forms
    
    class ArticleForm(forms.Form):
    	title = forms.CharField(max_length=10)
    	content = forms.CharField(widget=forms.Textarea)
    ```
    

## Django ModelForm

- Form
    - 사용자 입력 데이터를 DB에 저장하지 않을 때
    - ex. 검색, 로그인
- ModelForm
    - 사용자 입력 데이터를 DB에 저장해야 할 때
    - ex. 게시글 작성, 회원 가입

### ModelForm

Model과 연결된 Form을 자동으로 생성해주는 기능을 제공

→ Form + Model

### ModelForm class 정의

- 기존 ArticleForm 클래스 수정
    
    ```python
    # articles/forms.py
    
    from django import forms
    from .models import Article
    
    class ArticleForm(forms.ModelForm):
    	class Meta:
    		model = Article
    		fields = '__all__'
    ```
    

### Meta class

<aside>
📖

Model Form의 정보를 작성하는 곳

</aside>

- ‘fields’ 및 ‘exclude’ 속성
    - exclude 속성을 사용하여 모델에서 포함하지 않을 필드를 지정할 수도 있음
    
    ```python
    # articles/forms.py
    
    class ArticleForm(forms.ModelForm):
    	class Meta:
    		model = Article
    		fields = ('title',)
    ```
    
    ```python
    # articles/forms.py
    
    class ArticleForm(forms.ModelForm):
    	class Meta:
    		model = Article
    		exclude = ('title',)
    ```
    
- 주의 사항
    - Django에서 ModelForm에 대한 추가 정보나 속성을 작성하는 클래스 구조를 Meta 클래스로 작성 했을 뿐이며, 파이썬의 inner class와 같은 문법적인 관점으로 접근하지 말 것

### ModelForm 적용

- ModelForm을 적용한 create 로직
    
    ```python
    # articles/views.py
    
    from .forms import ArticleForm
    
    def create(request):
    	form = ArticleForm(request.POST)
    	if form.is_vaild():
    		article = form.save()
    		return redirect('articles:detail', article.pk)
    	context = {
    		'form': form,
    	}
    	return render(request, 'articles/new.html', context)
    ```
    
    - 제목 input에 공백을 입력 후 제출 시 에러 메시지 출력 확인
        - 유효성 검사의 결과!
    - 공백 데이터가 유효하지 않은 이유와 에러 메시지가 출력 되는 과정
        - 별도로 명시하지 않았지만 모델 필드에는 기본적으로 빈 값은 허용하지 않는 제약 조건이 설정 되어있음
        - 빈 값은 is_valid()에 의해 False로 평가되고 form 객체에는 그에 맞는 에러 메시지가 포함되어 다음 코드로 진행됨
- ModelForm을 적용한 edit 로직
    
    ```python
    # articles/views.py
    
    def edit(request, pk):
    	article = Article.objects.get(pk=pk)
    	form = ArticleForm(instance=artice)  # 수정할 때 원래 내용 보이게 하기
    	context = {
    		'article': article,
    		'form': form,
    	}
    	return render(request, 'articles/edit.html', context)
    ```
    
    ```html
    <!-- articles/edit.html -->
    
    <h1>EDIT</h1>
    <form action="{% url 'articles:update' article.pk %}" method="POST">
    	{% csrf_token %}
    	{{ form.as_p }}
    	<input type="submit">
    </form>
    ```
    
- ModelForm을 적용한 update 로직
    
    ```python
    # articles/views.py
    
    def update(request, pk):
    	article = Article.objects.get(pk=pk)
    	form = ArticleForm(request.POST, instance=article)
    	if form.is_valid():
    		form.save()
    		return redirect('articles:detail', article.pk)
    	context = {
    		'article': article,
    		'form': form,
    	}
    	return render(request, 'articles/edit.html', context)
    ```
    

## save 메서드

<aside>
📖

데이터베이스 객체를 만들고 저장하는 ModelForm의 인스턴스 메서드

</aside>

### save() 메서드가 생성과 수정을 구분하는 법

키워드 인자 instance 여부를 통해 생성할 지, 수정할 지를 결정

```python
# CREATE

form = ArticleForm(request.POST)
form.save()
```

```python
# UPDATE

form = ArticleForm(request.POST, instance=article)
form.save()
```

## Django Form 정리

- “사용자로부터 데이터를 수집하고 처리하기 위한 강력하고 유연한 도구”
- HTML form의 생성, 데이터 유효성 검사 및 처리를 쉽게 할 수 있도록 도움

## HTTP 요청 다루기

### new & create view 함수간 공통점과 차이점

- 공통점
    - 데이터 생성을 구현하기 위함
- 차이점
    - new는 GET method 요청만을, create는 POST method 요청만을 처리

HTTP request method 차이점을 활용해 동일한 목적을 가지는 2개의 view 함수를 하나로 최소화

### new & create 함수 결합

new와 create view 함수의 공통점과 차이점을 기반으로 하나의 함수로 결합

```python
def create(request):
	if request.method == 'POST':
		form = ArticleForm(request.POST)
		if form.is_valid():
			article = form.save()
			return redirect('articles:detail', article.pk)
	else:
		form = ArticleForm()
	context = {
		'form': form,
	}
	return render(request, 'articles/new.html', context)
```

- 두 함수의 유일한 차이점이었던 request method에 따른 분기
    - `if request.method == 'POST':`
    - `else:`
- POST 일 때는 과거 create 함수 구조였던 객체 생성 및 저장 로직 처리
    
    ```python
    form = ArticleForm(request.POST)
    if form.is_valid():
    	article = form.save()
    	return redirect('articles:detail', article.pk)
    ```
    
- POST가 아닐 때는 과거 new 함수에서 진행 했던 form 인스턴스 생성
    - `form = ArticleForm()`
- context에 담기는 form은
    1. is_valid()를 통과하지 못해 에러메시지를 담은 form이거나
    2. else 문을 통한 form 인스턴스
        
        ```python
        context = {
        	'form': form,
        }
        return render(request, 'articles/new.html', context)
        ```
        

### 기존 new 관련 코드 수정

1. 사용하지 않게 된 new url 제거
    
    ```python
    # articles/urls.py
    
    app_name = 'articles'
    urlpatterns = [
    	path('', views.index, name='index'),
    	path('<int:pk>/', views.detail, name='detail'),
    	# path('new/', views.new, name='new'),
    	path('create/', views.create, name='create'),
    	...
    	path('<int:pk>/update/', views.update, name='update'),
    ]
    ```
    
2. new 관련 키워드를 create로 변경 (html)
3. render에서 new 템플릿을 create 템플릿으로 변경 (view)

### request method에 따른 요청의 변화

- (GET) articles/create/
    - 게시글 생성 페이지를 줘!
- (POST) articles/create/
    - 게시글을 생성해줘!

### edit & update 함수 결합

기존 edit과 update view 함수 결합

```python
# articles/views.py

def update(request, pk):
	article = Article.objects.get(pk=pk)
	if request.method == 'POST'
		form = ArticleForm(request.POST, instance=article)
		if form.is_valid():
			form.save()
			return redirect('articles:detail', article.pk)
		else:
			form = ArticleForm(instance=article)
		context = {
			'article': article,
			'form': form,
		}
		return render(request, 'articles/update.html', context)
```

### 기존 edit 관련 코드 수정

1. 사용하지 않는 edit url 제거
2. edit 관련 키워드를 update

## 참고

### ModelForm의 키워드 인자 구성

```python
# ModelForm의 상위 클래스인 BaseModelForm의 생성자 함수 모습

class BaseModelForm(BaseFrom):
	def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None, initial=None,
							 error_class=ErrorList, label_suffix=None, empty_permitted=False,
							 instance=None, use_required_attribute=None, renderer=None):
```

- data는 첫번째에 위치한 키워드 인자이기 때문에 생략 가능
- instance는 9번째에 위치한 키워드 인자이기 때문에 생략할 수 없었음

```python
# articles/views.py

form = ArticleForm(request.POST, instance=article)
```

### Widgets 응용

```python
# articles/forms.py

class ArticleForm(forms.ModelForm):
	title = forms.CharField(
		label='제목',
		widget=forms.TextInput(
			attrs={
				'class': 'my-title',
				'placeholder': 'Enter the title',
			}
		),
	)
	
	class Meta:
		model = Article
		fields = '__all__'
```

### 필드를 수동으로 렌더링 하기

```html
{{ form.non_field_errors }}
<form action="..." method="POST">
	{% csrf_token %}
	<div>
		{{ form.title.errors }}
		<label for="{{ form.title.id_for_label }}">Title:</label>
		{{ form.title }}
	</div>
	<div>
		{{ form.content.errors }}
		<label for="{{ form.content.id_for_label }}">Content:</label>
		{{ form.content }}
	</div>
	<input type="submit">
</form>
```