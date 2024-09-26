# Django Static files

## Static files

<aside>
📖

정적 파일

- 서버 측에서 변경되지 않고 고정적으로 제공되는 파일
- 이미지, JS, CSS 파일 등
</aside>

### 웹 서버와 정적 파일

- 웹 서버의 기본 동작은 특정 위치(URL)에 있는 자원을 요청(HTTP request) 받아서 응답(HTTP response)을 처리하고 제공하는 것
- 이는 “자원에 접근 가능한 주소가 있다.”라는 의미
- 웹 서버는 요청 받은 URL로 서버에 존재하는 정적 자원을 제공함
    - 정적 파일을 제공하기 위한 경로(URL)가 있어야 함

### Static files 기본 경로

app 폴더/static/

- articles/static/articles/ 경로에 이미지 파일 배치
- static files 경로는 DTL의 static tag를 사용해야 함
- built-in tag가 아니기 때문에 load tag를 사용해 import 후 사용 가능
    - HTML 최상단에 위치해야 한다.
    - 상속 불가!
    
    ```html
    <!-- articles/index.html -->
    
    {% load static %}
    
    <img src="{% static 'articles/sample-1.png' %}" alt="img">
    ```
    

### STATIC_URL

기본 경로 및 추가 경로에 위치한 정적 파일을 참조하기 위한 URL

- 실제 파일이나 디렉토리 경로가 아니며, URL로만 존재

```python
# settings.py

STATIC_URL = 'static/'
```

- URL + STATIC_URL + 정적 파일 경로

### Static files 추가 경로

<aside>
📖

STATICFILES_DIRS에 문자열 값으로 추가 경로 설정

</aside>

- STATICFILES_DIRS
    - 정적 파일의 기본 경로 외에 추가적인 경로 목록을 정의하는 리스트
- 추가 경로 static file 제공하기
    - 임의의 추가 경로 설정
        
        ```python
        # settings.py
        # 기본적으로 없으니 추가 작성해야 한다.
        STATICFILES_DIRS = [
        	BASE_DIR / 'static',
        ]
        ```
        
    - 추가 경로에 이미지 파일 배치
        - static/image-1.png
    - static tag를 사용해 이미지 파일에 대한 경로 제공
        
        ```python
        <!-- articles/index.html -->
        
        <img src="{% static 'sample-2.png' %}" alt="img">
        ```
        
    - 이미지를 제공 받기 위해 요청하는 Request URL 확인
        - http://127.0.0.1:8000/static/image-1.png

<aside>
💡

정적 파일을 제공하려면 요청에 응답하기 위한 URL이 필요

</aside>

## Media files

<aside>
📖

사용자가 웹에서 업로드하는 정적 파일

- user-uploaded
- static files의 한 종류 이다.
</aside>

### ImageField()

이미지 업로드에 사용하는 모델 필드

<aside>
💡

이미지 객체가 직접 DB에 저장되는 것이 아닌 ‘이미지 파일의 경로’ 문자열이 저장됨

</aside>

### 미디어 파일을 제공하기 전 준비 사항

1. [settings.py](http://settings.py)에 MEDIA_ROOT, MEDIA_URL 설정
2. 작성한 MEDIA_ROOT와 MEDIA_URL에 대한 URL 지정
    
    ### MEDIA_ROOT
    
    미디어 파일들이 위치하는 디렉토리의 절대 경로
    
    ```python
    # settings.py
    # 기본적으로 없음. 직접 추가해야 함
    MEDIA_ROOT = BASE_DIR / 'media'
    ```
    
    ### MEDIA_URL
    
    MEDIA_ROOT에서 제공되는 미디어 파일에 대한 주소를 생성
    
    - STATIC_URL과 동일한 역할
    
    ```python
    # settings.py
    # 기본적으로 없음. 직접 추가해야 함
    MEDIA_URL = 'media/'
    ```
    
    ### MEDIA_ROOT와 MEDAI_URL에 대한 URL 지정
    
    - 업로드 된 파일의 URL == settings.MEDIA_URL
    - MEDIA_URL을 통해 참조하는 파일의 실제 위치 == settings.MEDIA_ROOT
    
    ```python
    # crud/urls.py
    # crud는 프로젝트 폴더 이름
    
    from django.conf import settings
    from django.conf.urls.static import static
    
    urlpatterns = [
    	path('admin/', admin.site.urls),
    	path('articles/', include('articles.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```
    

### 이미지 업로드

1. blank=True 속성을 작성해 빈 문자열이 저장될 수 있도록 제약 조건 설정
    - 게시글 작성 시 이미지 업로드 없이도 작성 할 수 있도록 하기 위함
    
    ```python
    # articles/models.py
    
    class Article(models.Model):
    	title = models.CharField(max_length=10)
    	content = models.TextField()
    	image = models.ImageField(blank=True)  
    	# 빈 값을 허용해야 이미지를 업로드 하지 않아도 글 작성이 가능하다.
    	# 기존 필드 사이에 작성해도 실제 테이블 생성 시에는 가장 우측(뒤)에 추가됨
    	created_at = models.DateTimeField(auto_now_add=True)
    	updated_at = models.DateTimeField(auto_now=True)
    ```
    
2. migration 진행
    
    <aside>
    💡
    
    ImageField를 사용하려면 반드시 Pillow 라이브러리가 필요
    
    </aside>
    
    ```
    $ pip install pillow
    
    $ python manage.py makemigrations
    $ python manage.py migrate
    
    $ pip freeze > requirements.txt
    ```
    
3. form 요소의 enctype 속성 추가
    
    ```html
    <!-- articles/create.html -->
    
    <h1>CREATE</h1>
    <form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data">
    	{% csrf_token %}
    	{{ form.as_p }}
    	<input type="submit">
    </form>
    ```
    
    <aside>
    💡
    
    entype은 데이터 전송 방식을 결정하는 속성
    
    - encoding type
    - form은 기본적으로 텍스트 형태의 데이터만 보낼 수 있게 설정이 되어있다.
    - 파일을 보낼 수 있게 속성을 설정해 줘야 함.
    </aside>
    
4. Model Form의 2번째 인자로 요청 받은 파일 데이터 작성
    - ModelForm의 상위 클래스 BaseModel Form의 생성자 함수의 2번째 위치 인자로 파일을 받도록 설정되어 있음
        
        ```python
        # articles/views.py
        
        def create(request):
        	if request.method == 'POST':
        		form = ArticleForm(request.POST, request.FILES)
        ...
        ```
        
5. 이미지 업로드 input 확인
6. 이미지 업로드 결과 확인
    
    <aside>
    💡
    
    DB에는 파일 자체가 아닌 “파일 경로”가 저장
    
    - MEDIA ROOT 이후의 경로가 저장된다.
    </aside>
    

### 업로드 이미지 제공

- **‘url’** 속성을 통해 업로드 파일의 경로 값을 얻을 수 있음
- **article.image.url**
    - 업로드 파일의 경로
- **article.image**
    - 업로드 파일의 파일 이름
    
    ```html
    <!-- articles/detail.html -->
    
    <img src="{{ article.image.url }}" alt="img">
    ```
    
- 이미지를 업로드하지 않은 게시물은 detail 템플릿을 렌더링 할 수 없음
- 이미지 데이터가 있는 경우만 이미지를 출력할 수 있도록 처리하기
    
    ```html
    <!-- articles/detail.html -->
    
    {% if article.image %}
    	<img src="{{ article.image.url }}" alt="img">
    {% endif %}
    ```
    

### 업로드 이미지 수정

1. 수정 페이지 form 요소에 enctype 속성 추가
    
    ```html
    <!-- articles/update.html -->
    
    <h1>UPDATE</h1>
    <form action="{% url 'articles:update' article.pk %}" method="POST" enctype="multipart/form-data">
    	{% csrf_token %}
    	{{ form.as_p}}
    	<input type="submit">
    </fomr>
    ```
    
2. update view 함수에서 업로드 파일에 대한 추가 코드 작성
    
    ```python
    # articles/views.py
    
    def update(request, pk):
    	article = Article.objects.get(pk=pk)
    	if request.method == 'POST':
    		form = ArticleForm(request.POST, request.FILES, instance=article)
    	...
    ```
    

## 참고

### 미디어 파일 추가 경로

- **‘upload_to’ argument**
    - ImageField()의 upload_to 속성을 사용해 다양한 추가 경로 설정
    
    ```python
    # articles/models.py
    
    # 1. 기본 경로 설정
    # media root 이후에 images/ 경로를 추가하겠다.
    image = models.ImageField(blank=True, upload_to='images/')
    
    # 2. 업로드 날짜로 경로 설정
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
    
    # 3. 함수 형식으로 경로 설정
    def articles_image_path(instance, filename):
    	return f'images/{instance.user.username}/{filename}'
    
    image = models.ImageField(blank=True, upload_to=articles_image_path)
    ```
    

### request.FILES가 두 번째 위치 인자인 이유

- ModelForm의 상위 클래스 BaseModelForm의 생성자 함수 키워드 인자 참고
    
    ```python
    class BaseModelForm(BaseForm):
    	def __init__(
    		self,
    		data=None,
    		files=None,
    		auto_id="id_%s",
    		prefix=None,
    		initial=None,
    		error_class=ErrorList,
    		label_suffix=None,
    		empty_permitted=False,
    		instance=None,
    		user_required_attribute=None,
    		renderer=None,
    	):
    ```
    

### Django static files 공식 문서

[How to manage static files (e.g. images, JavaScript, CSS) | Django documentation](https://docs.djangoproject.com/en/5.1/howto/static-files/)