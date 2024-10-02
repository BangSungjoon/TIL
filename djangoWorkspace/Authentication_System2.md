# Authentication System 2

## 회원 가입

<aside>
💡

User 객체를 Create 하는 과정

</aside>

### UserCreationForm()

- 회원 가입 시 사용자 입력 데이터를 받는 built-in ModelForm

### 회원 가입 페이지 작성

```python
# accounts/urls.py

app_name = "accounts"
urlpatterns = [
	...,
	path('sighup/', views.signup, name='signup'),
]
```

```python
# accounts/views.py

from django.contrib.auth.forms import UserCreationForm

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('articles:index')
	else:
		form = UserCreationForm()
	context = {
		'form': form,
	}
	return render(request, 'accounts/signup.html', context)
```

```html
<!-- accounts/signup.html -->

<h1>회원가입</h1>
<form action="{% url 'accounts:signup' %}" method="POST">
	{% csrf_token %}
	{{ form.as_p }}
	<input type="submit">
</form>
```

### 회원 가입 로직 에러

- 회원 가입 시도 후 에러 페이지 확인
    - Manager isn’t available; ‘auth.User’ has been swapped for ‘accounts.User’
- 회원 가입에 사용하는 UserCreationForm이 대체한 커스텀 유저 모델이 아닌 과거 Django의 기본 유저 모델로 인해 작성된 클래스이기 때문
    
    ```python
    class Meta:
    	model = User
    	fields = ("username",)
    	field_classes = {"username": UsernameField}
    ```
    
- 커스텀 유저 모델을 사용하려면 다시 작성해야 하는 Form
    1. UserCreationForm
    2. UserChangeForm
    - 두 From 모두 `class Meta: model = User` 가 작성된 Form이기 때문에 재작성 필요

### UserCreationForm과 UserChangeForm 커스텀

- Custom User model을 사용할 수 있도록 상속 후 일부분만 재작성
    
    ```python
    # accounts/forms.py
    
    from django.contrib.auth import get_user_model
    from django.contrib.auth.forms import UserCreationForm, UserChangeForm
    
    class CustomUserCreationForm(UserCreationForm):
    	class Meta(UserCreationForm.Meta):
    		model = get_user_model()
    
    class CustomUserChangeForm(UserChangeForm):
    	class Meta(UserChangeForm.Meta):
    		model = get_user_model()
    ```
    
- `get_user_model()`
    - “현재 프로젝트에서 활성화된 사용자 모델(active user model)”을 반환하는 함수
- User 모델을 직접 참조하지 않는 이유
    - `get_user_model()`을 사용해 User 모델을 참조하면 커스텀 User 모델을 자동으로 반환해주기 때문
    - Django는 필수적으로 User 클래스를 직접 참조하는 대신 `get_user_model()`을 사용해 참조해야 한다고 강조하고 있음

### 회원 가입 로직 완성

- `CustomUserCreationForm`으로 변경
    
    ```python
    # accounts/views.py
    
    from .forms import CustomUserCreationForm
    
    def signup(request):
    	if request.method == 'POST':
    		form = CustomUserCreationForm(request.POST)
    		if form.is_valid():
    			form.save()
    			return redirect('articles:index')
    		else:
    			form = CustomUserCreationForm()
    		context = {
    			'form': form,
    		}
    		return render(request, 'accounts/signup.html', context)
    ```
    

## 회원 탈퇴

<aside>
💡

User 객체를 Delete 하는 과정

</aside>

### 회원 탈퇴 로직 작성

```python
# accounts/urls.py

app_name = 'accounts'
urlpatterns = [
	...,
	path('delete/', views.delete, name='delete'),
]
```

```python
# accounts/views.py

def delete(request):
	request.user.delete()
	return redirect('articles:index')
```

```html
<!-- accounts/index.html -->

<form action="{% url 'accounts:delete' %}" method="POST">
	{% csrf_token %}
	<input type="submit" value="회원탈퇴">
</form>
```

## 회원정보 수정

<aside>
💡

User 객체를 Update 하는 과정

</aside>

### UserChangeForm()

- 회원 정보 수정 시 사용자 입력 데이터를 받는 built-in ModelForm

### 회원정보 수정 페이지 작성

```python
# accounts/urls.py

app_name = 'accounts'
urlpatterns = [
	...,
	path('update/', views.update, name='update'),
]
```

```python
# accounts/views.py

from .forms import CustomUserChangeForm

def update(request):
	if request.method == 'POST':
		form = CustomUserChangeForm(request.POST, instance=request.user)
		# form = CustomUserChangeForm(data=request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('articles:index')
	else:
		form = CustomUserChangeForm(instance=request.user)
	context = {
		'form': form,
	}
	return render(request, 'accounts/update.html', context)
```

```html
<!-- accounts/update.html -->

<h1>회원정보 수정</h1>
<form action="{% url 'accounts:update' %}" method="POST">
	{% csrf_token %}
	{{ form.as_p }}
	<input type="submit">
</form>
```

```html
<!-- accounts/index.html -->

<a href="{% url 'accounts:update' %}">회원정보 수정</a>
```

### UserChangeForm 사용 시 문제점

- User 모델의 모든 정보들(fields)까지 모두 출력됨
- 일반 사용자들이 접근해서는 안되는 정보는 출력하지 않도록 해야 함

<aside>
💡

CustomUserChangeForm에서 출력 필드를 다시 조정하기

</aside>

### CustomUserChangeForm 출력 필드 재정의

- User Model의 필드 목록 확인
    
    ```python
    # accounts/forms.py
    
    class CustomUserChangeForm(UserChangeForm):
    	class Meta(UserChangeForm.Meta):
    		model = get_user_model()
    		fields = ('first_name', 'last_name', 'email',)
    ```
    

## 비밀번호 변경

<aside>
💡

인증된 사용자의 Session 데이터를 Update 하는 과정

</aside>

### PasswordChangeForm()

- 비밀번호 변경 시 사용자 입력 데이터를 받는 built-in Form

### 비밀번호 변경 페이지 작성

```python
# crud/urls.py

from accounts import views

urlpatterns = [
	...
	path('<int:user_pk>/password/', views.change_password, name='change_password'),
]]
```

```python
# accounts/views.py

from django.contrib.auth.forms import PasswordChangeForm

def change_password(request, user_pk):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		# form = PasswordChangeForm(user=request.user, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('articles:index')
	else:
		form = PasswordChangeForm(request.user)
	context = {
		'form': form,
	}
	return render(request, 'accounts/change_password.html', context)
```

```html
<!-- accounts/change_password.html -->

<h1>비밀번호 변경</h1>
<form action="{% url 'change_password' user.pk %}" method="POST">
	{% csrf_token %}
	{{ form.as_p }}
	<input type="submit">
</form>
```

### 암호 변경 시 세션 무효화

- 비밀번호가 변경되면 기존 세션과 회원 인증 정보가 일치하지 않게 되어 버려 로그인 상태가 유지되지 못하고 로그아웃 처리됨
- 비밀번호가 변경되면서 기존 세션과의 회원 인증 정보가 일치하기 때문
- `update_session_auth_hash(request, user)`
    - 암호 변경 시 세션 무효화를 막아주는 함수
    - 암호가 변경되면 새로운 password의 Session Data로 기존 session을 자동으로 갱신
    
    ```python
    # accounts/views.py
    from django.contrib.auth import update_session_auth_hash
    from django.contrib.auth.forms import PasswordChangeForm
    
    def change_password(request, user_pk):
    	if request.method == 'POST':
    		form = PasswordChangeForm(request.user, request.POST)
    		# form = PasswordChangeForm(user=request.user, data=request.POST)
    		if form.is_valid():
    			user = form.save()
    			update_session_auth_hash(request, user)
    			return redirect('articles:index')
    	else:
    		form = PasswordChangeForm(request.user)
    	context = {
    		'form': form,
    	}
    	return render(request, 'accounts/change_password.html', context)
    ```
    

## 인증된 사용자에 대한 접근 제한

로그인 사용자에 대해 접근을 제한하는 2가지 방법

1. is_authenticated 속성
2. login_required 데코레이터

### is_authenticated 속성

<aside>
💡

사용자가 인증 되었는지 여부를 알 수 있는 User model의 속성

</aside>

- 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성
- 비인증 사용자에 대해서는 항상 False
- is_authenticated 속성 적용하기
    1. 로그인과 비로그인 상태에서 화면에 출력되는 링크를 다르게 설정하기
        
        ```html
        <!-- articles/index.html -->
        
        {% if request.user.is_authenticated %}
        	<h3>Hello, {{ user.username }}</h3>
        	<a href="{% url 'articles:create' %}">NEW</a>
        	<form action="{% url 'accounts:logout' %}" method="POST">
        		{% csrf_token %}
        		<input type="submit" value="Logout">
        	</form>
        	<form action="{% url 'accounts:delete' %}" method="POST">
        		{% csrf_token %}
        		<input type="submit" value="회원탈퇴">
        	</form>
        	<a href="{% url 'accounts:update' %}">회원정보 수정</a>
        {% else %}
        	<a href="{% url 'accounts:login' %}">Login</a>
        	<a href="{% url 'accounts:signup' %}">Signup</a>
        {% endif %}
        ```
        
    2. 인증된 사용자라면 로그인/회원가입 로직을 수행할 수 없도록 하기
        
        ```python
        # accounts/views.py
        
        def login(request):
        	if request.user.is_authenticated:
        		return redirect('articles:index')
        	...
        
        def signup(request):
        	if request.user.is_authenticated:
        		return redirect('articles:index')
        	...
        ```
        

### login_required 데코레이터

<aside>
💡

인증된 사용자에 대해서만 view 함수를 실행시키는 데코레이터

</aside>

- 비인증 사용자의 경우 /accounts/login/ 주소로 redirect 시킴
- login_required 데코레이터 적용하기
    1. 인증된 사용자만 게시글을 작성/수정/삭제 할 수 있도록 수정
        
        ```python
        # articles/views.py
        
        from django.contrib.auth.decorators import login_required
        
        @login_required
        def create(request):
        	pass
        	
        @login_required
        def delete(request, article_pk):
        	pass
        
        @login_required
        def update(request, article_pk):
        	pass
        ```
        
    2. 인증된 사용자만 로그아웃/탈퇴/수정/비밀번호 변경 할 수 있도록 수정
        
        ```python
        # articles/views.py
        
        from django.contrib.auth.decorators import login_required
        
        @login_required
        def logout(request):
        	pass
        	
        @login_required
        def change_password(request, article_pk):
        	pass
        ```
        

## 참고

### is_authenticated 속성 코드

- 메서드가 아닌 속성 값임을 주의

### 회원 가입 후 자동 로그인까지 이어서 진행하려면?

- 회원 가입 성공한 user 객체를 활용해 login 진행
    
    ```python
    # accounts/views.py
    
    from django.contrib.auth.forms import UserCreationForm
    
    def signup(request):
    	if request.method == 'POST':
    		form = UserCreationForm(request.POST)
    		if form.is_valid():
    			form.save()
    			auth_login(request, user)  # 추가
    			return redirect('articles:index')
    	else:
    		form = UserCreationForm()
    	context = {
    		'form': form,
    	}
    	return render(request, 'accounts/signup.html', context)
    ```
    

### 탈퇴와 함께 기존 사용자의 Session Data 삭제 방법

- 사용자 객체 삭제 이후 로그아웃 함수 호출
- 단, “탈퇴(1) 후 로그아웃(2)”의 순서가 바뀌면 안됨
- 먼저 로그아웃이 진행되면 해당 요청 객체 정보가 없어지기 때문에 탈퇴에 필요한 유저 정보 또한 없어지기 때문
    
    ```python
    # accounts/views.py
    
    def delete(request):
    	request.user.delete()
    	auth_logout(request)
    ```
    

### PasswordChangeForm의 인자 순서

- PasswordChangeForm이 다른 Form과 달리 user 객체를 첫 번째 인자로 받는 이유
- 부모 클래스인 SetPasswordForm의 생성자 함수 구성을 따르기 때문