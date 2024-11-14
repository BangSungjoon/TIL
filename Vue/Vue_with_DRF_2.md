# Vue with DRF 2

## 인증 with DRF

### 개요

- user ForeignKey 추가 작성
    
    ```python
    # articles/models.py
    
    class Article(models.Model):
    	user = models.ForeignKey(
    		settigns.AUTH_USER_MODEL, on_delete=models.CASCADE
    	)
    	title = models.CharField(max_length=100)
    	content = models.TextField()
    	created_at = models.DateTimeField(auto_now_add=True)
    	updated_at = models.DateTimeField(auto_now=True)
    ```
    
- serializers의 read_only_fields 추가
    
    ```python
    # articles/serializers.py
    
    class ArticleSerializer(serializers.ModelSerializer):
    	class Meta:
    		model = Article
    		fields = '__all__'
    		read_only_fields = ('user',)
    ```
    
- article_list view 함수에서 게시글 생성 시 user 정보도 저장될 수 있도록 작성
    
    ```python
    # articles/views.py
    
    @api_view(['GET', 'POST'])
    # @permission_classes([IsAuthenticated])
    def article_list(request):
    	...
    	
    	elif request.method == 'POST':
    		serializer.is_valid(raise_exceiption=True):
    			# serializer.save()
    			serializer.save(user=request.user)
    			return Response(serializer.data, status=status.HTTP_201_CREATED)
    ```
    
- DB 초기화
    - db.sqlite3 삭제
    - migrations 파일 삭제
- Migration 과정 재진행

### 인증

- Authentication
    - 수신된 요청을 해당 요청의 사용자 또는 자격 증명과 연결하는 메커니즘
    - 누구인지를 확인하는 과정
- Permissions
    - 권한
    - 요청에 대한 접근 허용 또는 거부 여부를 결정
- 인증과 권한
    - 순서상 인증이 먼저 진행되며 수신 요청을 해당 요청의 사용자 또는 해당 요청이 서명된 토큰(token)과 같은 자격 증명 자료와 연결
    - 그런 다음 권한 및 제한 정책은 인증이 완료된 해당 자격 증명을 사용하여 요청을 허용해야 하는 지를 결정
- DRF에서의 인증
    - 인증은 항상 view 함수 시작 시, 권한 및 제한 확인이 발생하기 전, 다른 코드의 진행이 허용되기 전에 실행됨
    - 인증 자체로는 들어오는 요청을 허용하거나 거부할 수 없으며, 단순히 요청에 사용된 자격 증명만 식별한다는 점에 유의
- 승인되지 않은 응답 및 금지된 응답
    - 인증되지 않은 요청이 권한을 거부하는 경우 해당되는 두 가지 오류 코드를 응답
    1. HTTP 401 Unauthorized
        - 요청된 리소스에 대한 유효한 인증 자격 증명이 없기 때문에 클라이언트 요청이 완료되지 않았음을 나타냄 (누구인지를 증명할 자료가 없음)
    2. HTTP 403 Forbidden (Permission Denied)
        - 서버에 요청이 전달되었지만, 권한 때문에 거절되었다는 것을 의미
        - 401과 다른 점은 서버는 클라이언트가 누구인지 알고 있음

### 인증 정책 설명

1. 전역 설정
    - 프로젝트 전체에 적용되는 기본 인증 방식을 정의
    - DEFAULT_AUTHENTICATION_CLASSES를 사용
    - 기본 값 : SessionAuthentication과 BasicAuthentication
    - 사용 예시
        
        ```python
        REST_FRAMEWORK = {
        	'DEFAULT_AUTHENTICATION_CLASSES': [
        		'rest_framework.authentication.BasicAuthentication',
        		'rest_framework.authentication.TokenAuthentication',
        	],
        }
        ```
        
2. View 함수 별 설정
    - authentication_classes 데코레이터를 사용
    - 개별 view에 지정하여 재정의
    - 사용 예시
        
        ```python
        from rest_framework.decorators import authentication_classes
        from rest_framework.authentication import TokenAuthentication, BasicAuthentication
        
        @api_view(['GET', 'POST'])
        @authentication_classes([TokenAuthentication, BasicAuthentication])
        def article_list(request):
        	pass
        ```
        
- DRF가 제공하는 인증 체계
    1. BasicAuthentication
    2. **TokenAuthentication**
        - token 기반 HTTP 인증 체계
        - 기본 데스크톱 및 모바일 클라이언트와 같은 클라이언트-서버 설정에 적합
        - 서버가 인증된 사용자에게 토큰을 발급하고 사용자는 매 요청마다 발급받은 토큰을 요청과 함께 보내 인증 과정을 거침
    3. SessionAuthentication
    4. RemoteUserAuthentication

### Token 인증 설정 - TokenAuthentication 적용 과정

1. 인증 클래스 설정
    - TokenAuthentication 활성화 코드 작성
    - 전역 인증 정책을 Token 방식으로 설정
    
    ```python
    # settings.py
    
    REST_FRAMEWORK = {
    	# Authentication
    	'DEFAULT_AUTHENTICATION_CLASSES': [
    		'rest_framework.authentication.TokenAuthentication',
    	],
    }
    ```
    
2. INSTALLED_APPS 추가
    - rest_framework.authentoken 작성
    
    ```python
    # settings.py
    
    INSTALLED_APPS = [
    	'articles',
    	'accounts',
    	'rest_framework',
    	'rest_framework.authtoken',
    	...,
    ]
    ```
    
3. Migrate 진행
4. 토큰 생성 코드 작성
    - accounts/signals.py 작성
    - 인증된 사용자에게 자동으로 토큰을 생성해주는 역할
    
    ```python
    # accounts/signals.py
    
    from django.db.models.signals import post_save
    from django.dispatch import receiver
    from rest_framework.authentoken.models import Token
    from django.conf import settings
    
    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
    	if created:
    		Token.objects.create(user=instance)
    ```
    

### 토큰 인증 방식 과정

1. 사용자 로그인 (클라이언트)
2. 사용자 확인 (django, DB)
3. Token 발급 (django)
4. 응답 (+ Token) (django)
5. 데이터 요청 (+ Token) (클라이언트)
6. Token 검증 (django)
7. 응답 (+ 요청 데이터) (django)

### Dj-Rest-Auth 라이브러리

- 회원가입, 인증(소셜미디어 인증 등), 비밀번호 재설정, 사용자 세부 정보 검색, 회원 정보 수정 등 다양한 인증 관련 기능을 제공하는 라이브러리
- Dj-Rest-Auth 설치 및 적용
    1. 설치
        - `$ pip install dj-rest-auth`
    2. 추가 App 작성
        
        ```python
        # settings.py
        
        INSTALLED_APPS = [
        	'articles',
        	'accounts',
        	'rest_framework',
        	'rest_framework.authtoken',
        	'dj_rest_auth',
        	...,
        ]
        ```
        
    3. 추가 URL 작성
        
        ```python
        # my_api/urls.py
        
        urlpatterns = [
        	...
        	path('accounts/', include('dj_rest_auth.urls')),
        ]
        ```
        
- Dj-Rest-Auth의 Registration(등록) 기능 추가 설정
    1. 패키지 추가 설치
        - `$ pip install 'dj-rest-auth[with-social]'`
    2. 추가 App 등록
        
        ```python
        # settings.py
        
        INSTALLED_APPS = [
        	...
        	'django.contrib.sites',
        	'allauth',
        	'allauth.account',
        	'allauth.socialaccount',
        	'dj_rest_auth.registration',
        	...,
        ]
        
        SITE_ID = 1
        ```
        
    3. 관련 설정 코드 작성
        
        ```python
        # settings.py
        
        MIDDLEWARE = [
        	...
        	'allauth.account.middleware.AccountMiddleware',
        ]
        ```
        
    4. 추가 URL 등록
        
        ```python
        # my_api/urls.py
        
        urlpatterns = [
        	...
        	path('accounts/signup/', include('dj_rest_auth.registration.urls')),
        ]
        ```
        
    5. Migrate 진행

### Token 발급 및 활용

- Token 발급
    1. 회원 가입 및 로그인을 진행하여 토큰 발급 테스트하기
    2. 라이브러리 설치로 인해 추가 된 URL 목록 확인
        - http://127.0.0.1:8000/accounts/
    3. 회원 가입 진행 (DRF 페이지 하단 회원 가입 form 사용)
        - http://127.0.0.1:8000/accounts/signup/
    4. 로그인 진행 (DRF 페이지 하단 로그인 form 사용)
        - http://127.0.0.1:8000/accounts/login/
    5. 로그인 성공 후 DRF로 부터 발급 받은 Token 확인
        - 이제 이 Token을 Vue에서 별도로 저장하여 매 요청마다 함께 보내야 함
- Token 활용
    1. 게시글 작성 과정을 통해 Token 사용 방법 익히기
        - Postman을 활용해 게시글 작성요청
        - http://127.0.0.1:8000/api/v1/articles/
    2. Body에 게시글 제목과 내용 입력
        - http://127.0.0.1:8000/api/v1/articles/
    3. Headers에 발급받은 Token 작성 후 요청 성공 확인
        - Key: “Authorization”
        - Value: “Token 토큰 값”
- 클라이언트가 Token으로 인증 받는 방법
    1. “Authorization” HTTP Header에 포함
    2. 키 앞에는 문자열 “Token”이 와야 하며 “공백”으로 두 문자열을 구분해야 함

<aside>
💡

발급 받은 Token을 인증이 필요한 요청마다 함께 보내야 함

</aside>

## 권한 with DRF

### 권한 정책 설정

1. 전역 설정
    - 프로젝트 전체에 적용되는 기본 권한 방식을 정의
    - DEFAULT_PERMISSION_CLASSES를 사용
    - 기본 값 : rest_framework.permissions.AllowAny
    - 사용 예시
        
        ```python
        # settings.py
        REST_FRAMEWORK = {
        	'DEFAULT_PERMISSION_CLASSES': [
        		'rest_framework.permissions.IsAuthenticated',
        	],
        }
        ```
        
2. View 함수 별 설정
    - permission_classes 데코레이터를 사용
    - 개별 view에 지정하여 재정의
    - 사용 예시
        
        ```python
        from rest_framework.decorators import permission_classes
        from rest_framework.permissions import IsAuthenticated
        
        @api_view(['GET', 'POST'])
        @permission_classes(['IsAuthenticated])
        def article_list(request):
        	pass
        ```
        

### IsAuthenticated 설정

- IsAuthenticated
    - DRF가 제공하는 권한 정책 중 하나
    - 인증되지 않은 사용자에 대한 권한을 거부하고 그렇지 않은 경우 권한을 허용
    - 등록된 사용자만 API에 엑세스 할 수 있도록 하려는 경우에 적합
- IsAuthenticated 권한 설정
    1. DEFAULT_PERMISSION_CLASSES 작성
        - 기본적으로 모든 View 함수에 대한 접근을 허용
            
            ```python
            # settings.py
            
            REST_FRAMEWORK = {
            	'DEFAULT_AUTHENTICATION_CLASSES': [
            		'rest_framework.authentication.TokenAuthentication',
            	],
            	'DEFAULT_PERMISSION_CLASSES': [
            		'rest_framework.permissions.AllowAny',
            	],
            }
            ```
            
    2. permission_classes 관련 코드 주석 해제
        - 전체 게시글 조회 및 생성시에만 인증된 사용자만 진행 할 수 있도록 권한 설정
            
            ```python
            # articles/views.py
            
            from rest_framework.decorators import permission_classes
            from rest_framework.permissions import IsAuthenticated
            
            @api_view(['GET', 'POST'])
            @permission_classes([IsAuthenticated])
            def article_list(request):
            	pass
            ```
            
- 권한 활용
    1. 만약 관리자만 전체 게시글 조회가 가능한 권한이 설정 되었을 때, 인증된 일반 사용자가 조회 요청을 할 경우 어떻게 되는지 응답 확인하기
        - 테스트를 위해 임시로 관리자 관련 클래스 IsAdminUser로 변경
            
            ```python
            # articles/views.py
            
            from rest_framework.permissions import IsAuthenticated, IsAdminUser
            
            @api_view(['GET', 'POST'])
            @permission_classes([IsAdminUser])
            def article_list(request):
            	pass
            ```
            
    2. 전체 게시글 조회 요청
        - http://127.0.0.1:8000/api/v1/articles/
        - 403 Forbidden 응답 확인
    3. IsAdminUser 삭제 후 IsAuthenticated 권한으로 복구
        
        ```python
        # articles/views.py
        
        from rest_framework.permissions import IsAuthenticated
        
        @api_view(['GET', 'POST'])
        @permission_classes([IsAuthenticated])
        def article_list(request):
        	pass
        ```
        

## 인증 with Vue

- 정상 작동하던 게시글 전체 조회가 작동하지 않는다.
    - 401 status code 확인
- 게시글 조회 요청 시 인증에 필요한 수단(token)을 보내지 않고 있으므로 게시글 조회가 불가능해진 것

### 회원가입

1. SignUpView route 관련 코드 작성
    
    ```jsx
    // router/index.js
    
    import SignUpView from '@/views/SignUpView.vue'
    
    const router = createRouter({
    	history: createWebHistory(import.meta.env.BASE_URL),
    	routes: [
    		{
    			path: '/signup',
    			name: 'SignUpView',
    			component: SignUpView
    		}
    	]
    })
    ```
    
2. App 컴포넌트에 SignUpView 컴포넌트로 이동하는 RouterLink 작성
    
    ```html
    <!-- App.vue -->
    
    <template>
    	<header>
    		<nav>
    			<RouterLink :to="{ name: 'ArticleView' }">Articles</RouterLink> | 
    			<RouterLink :to="{ name: 'SingUpView' }">SignUpPage</RouterLink>
    		</nav>
    	</header>
    	<RouterView />
    </template>
    ```
    
3. 회원가입 form 작성
    
    ```html
    <!-- views/SignUpView.vue -->
    
    <template>
    	<div>
    		<h1>Sign Up Page</h1>
    		<form>
    			<label for="username">username : </label>
    			<input type="text" id="username" v-model.trim="username"><br>
    			
    			<label for="password1"> password : </label>
    			<input type="password" id="password1" v-model.trim="password1"><br>
    			
    			<label for="password2"> password confirmation : </label>
    			<input type="password" id="password2" v-model.trim="password2">
    			
    			<input type="submit" value="SignUp">
    		</form>
    	</div>
    </template>
    ```
    
4. 사용자 입력 데이터와 바인딩 될 반응형 변수 작성
    
    ```html
    <!-- views/SignUpView.vue -->
    
    <script setup>
    import { ref } from 'vue'
    
    const username = ref(null)
    const password1 = ref(null)
    const password2 = ref(null)
    </script>
    ```
    
5. SignUpView 컴포넌트 출력 확인
6. 회원가입 요청을 보내기 위한 signUp 함수가 해야 할 일
    1. 사용자 입력 데이터를 받아
    2. 서버로 회원가입 요청을 보냄
    
    ```jsx
    // stores/counter.js
    
    export const useCounterStore = defineStore('counter', () => {
    	const signUp = function () {
    		...
    	}
    	return { articles, API_URL, getArticles, signUp }
    }, { persist: true }
    ```
    
7. 컴포넌트에 사용자 입력 데이터를 저장 후 store의 signUp 함수를 호출하는 함수 작성
    
    ```jsx
    // views/SignUpView.vue
    import { useCounterStore } from '@/stores/counter'
    
    const store = useCounterStore()
    
    const signUp = function () {
    	const payload = {
    		username: username.value,
    		password1: password1.value,
    		password2: password2.value
    	}
    	store.signUp(payload)
    }
    ```
    
    ```html
    <!-- views/SignUpView.vue -->
    
    <form @submit.prevent="SignUp">
    	...
    </form>
    ```
    
8. 실제 회원가입 요청을 보내는 store의 signUp 함수 작성
    
    ```jsx
    // stores/counter.js
    
    const signUp = function (payload) {
    	const username = payload.username
    	const password1 = payload.password1
    	const password2 = payload.password2
    	// const { username, password1, password2 } = payload
    	
    	axios({
    		method: 'post',
    		url: `${API_URL}/accounts/signup/`
    		data: { 
    			username, password1, password2
    		}
    	})
    		.then(res => {
    			console.log('회원가입이 완료되었습니다.')
    		})
    		.catch(err => console.log(err))
    }
    ```
    
9. 회원가입 테스트
10. Djnago DB 확인

### 로그인

1. LogInView route 관련 코드 작성
    
    ```jsx
    // router/index.js
    
    import LogInView from '@/views/LoginView.vue'
    
    const router = createRouter({
    	history: createWebHistory(import.meta.env.BASE_URL),
    	routes: [
    		{
    			path: '/login',
    			name: LoginView,
    			component: LogInView
    		}
    	]
    })
    ```
    
2. App 컴포넌트에 LogInView 컴포넌트로 이동하는 RouterLink 작성
    
    ```jsx
    // App.vue
    
    <template>
    	<header>
    		<nav>
    			<RouterLink :to="{ name: 'ArticleView' }">Articles</RouterLink> | 
    			<RouterLink :to="{ name: 'SignUpView' }">SignUpPage</RouterLink> | 
    			<RouterLink :to="{ name: 'LoginView' }">LogInPage</RouterLink>
    		</nav>
    	</header>
    	<RouterView />
    </template>
    ```
    
3. 로그인 form 작성
    
    ```html
    <!-- views/LoginView.vue -->
    
    <template>
    	<div>
    		<h1>LogIn Page</h1>
    		<form>
    			<label for="username">username : </label>
    			<input type="text" id="username" v-model.trim="username"><br>
    			
    			<label for="password"> password : </label>
    			<input type="password" id="password" v-model.trim="password"><br>
    			
    			<input type="submit" value="logIn">
    		</form>
    	</div>
    </template>
    ```
    
4. 사용자 입력 데이터와 바인딩 될 반응형 변수 작성
    
    ```html
    <!-- views/LoginView.vue -->
    
    <script setup>
    import { ref } from 'vue'
    
    const username = ref(null)
    const password = ref(null)
    </script>
    ```
    
5. LogInView 컴포넌트 출력 확인
6. 로그인 요청을 보내기 위한 logIn 함수가 해야 할 일
    1. 사용자 입력 데이터를 받아
    2. 서버로 로그인 요청 및 응답 받은 토큰 저장
    
    ```jsx
    // stores/counter.js
    
    export const useCounterStore = defineStore('counter', () => {
    	const logIn = function () {
    		...
    	}
    	return { articles, API_URL, getArticles, signUp, logIn }
    }, { persist: true })
    ```
    
7. 컴포넌트에 사용자 입력 데이터를 저장 후 store의 logIn 함수를 호출하는 함수 작성
    
    ```jsx
    // views/LoginView.vue
    
    import { useCounterStore } from '@/stores/counter'
    
    const store = useCounterStore()
    
    const logIn = function () {
    	const payload = {
    		username: username.value,
    		password: password.value
    	}
    	store.logIn(payload)
    }
    ```
    
    ```html
    <!-- views/LoginView.vue -->
    
    <form @submit.prevent="logIn">
    	...
    </form>
    ```
    
8. 실제 로그인 요청을 보내는 store의 logIn 함수 작성
    
    ```jsx
    // stores/counter.js
    
    const logIn = function (payload) {
    	const username = payload.username
    	const password = payload.password
    	axios({
    		method: 'post',
    		url: `${API_URL}/accounts/login/`,
    		data: {
    			username, password
    		}
    	})
    			.then(res => {
    				console.log('로그인이 완료되었습니다.')
    				console.log(res.data)
    			})
    			.catch(err => console.log(err))
    }
    ```
    
9. 로그인 테스트
    - 응답 객체 안에 Django가 발급한 Token이 함께 온 것을 확인

### 요청과 토큰

<aside>
💡

Token을 store에 저장하여 인증이 필요한 요청마다 함께 보낸다.

</aside>

- 토큰 저장 로직 구현
    1. 반응형 변수 token 선언 및 토큰 저장
        
        ```jsx
        // stores/counter.js
        
        export const useCounterStore = defineStore('counter', () => {
        	const token = ref(null)
        	
        	const logIn = function (payload) {
        		...
        			.then(res => {
        				token.value = res.data.key
        			})
        			.catch(err => console.log(err))
        		}
        		return { articles, API_URL, getArticles, signUp, logIn, token }
        	}, { persist: true })
        ```
        
    2. 다시 로그인 요청 후 store에 저장된 토큰 확인
- 토큰이 필요한 요청
    1. 게시글 전체 목록 조회 시 
        1. 게시글 전체 목록 조회 요청 함수 getArticles에 token 추가
            
            ```jsx
            // stores/counter.js
            
            const getArticles = function () {
            	axios({
            		method: 'get',
            		url: `${API_URL}/api/v1/articles/`,
            		headers: {
            			Authorization: `Token ${token.value}`
            		}
            	})
            		.then(res => {
            			articles.value = res.data
            		})
            		.catch(err => console.log(err))
            }
            ```
            
        2. 401 상태 코드가 사라지고 게시글이 정상적으로 출력되는 것을 확인
    2. 게시글 작성 시
        1. 게시글 생성 요청 함수 createArticle에 token 추가
            
            ```jsx
            // views/CreateView.vue
            
            const createArticle = function () {
            	axios({
            		method: 'post',
            		url: `${store.API_URL}/api/v1/articles/`,
            		data: {
            			title: title.value,
            			content: content.value
            		},
            		headers: {
            			Authorization: `Token ${store.token}`
            		}
            	})...
            }
            ```
            
        2. 게시글 작성 확인

### 인증 여부 확인

- 인증 상태 여부를 나타낼 속성 값 지정
    - token 소유 여부에 따라 로그인 상태를 나타낼 isLogin 변수 작성
    - 그리고 computed를 활용해 token 값이 변할 때만 상태를 계산하도록 함
    
    ```jsx
    // stores/counter.js
    
    export const useCounterStore = defineStore('counter', () => {
    	const isLogin = computed(() => {
    		if (token.value === null) {
    			return false
    		} else {
    			 return true
    		}
    	})
    		return { articles, API_URL, getArticles, signUp, logIn, token, isLogin }
    	}, { persist: true })
    ```
    
- 사용자의 인증(로그인) 여부에 따른 추가 기능 구현
    1. 인증 되지 않은 사용자
        - 메인 페이지 접근 제한
            1. 전역 네비게이션 가드 beforeEach를 활용해 다른 주소에서 메인 페이지로 이동 시 인증 되지 않은 사용자라면 로그인 페이지로 이동시키기
                
                ```jsx
                // router/index.js
                
                import { useCounterStore } from '@/stores/counter'
                
                const router = createRouter({...})
                
                router.beforeEach((to, from) => {
                	const store = useCounterStore()
                	// 만약 이동하는 목적지가 메인 페이지면서
                	// 현재 로그인 상태가 아니라면 로그인 페이지로 보냄
                	if (to.name === 'ArticleView' && !store.isLogin) {
                		window.alert('로그인이 필요합니다.')
                		return { name: 'LoginView' }
                	}
                })
                ```
                
            2. 부라우저 local storage에서 token을 삭제 후 메인 페이지 접속 시도
    2. 인증 된 사용자
        - 회원가입 및 로그인 페이지에 접근 제한
            1. 다른 주소에서 회원가입 또는 로그인 페이지로 이동 시 이미 인증 된 사용자라면 메인 페이지로 이동시키기
                
                ```jsx
                // router/index.js
                
                router.beforeEach((to, from) => {
                	const store = useCounterStore()
                	if (to.name === 'ArticleView' && !store.isLogin) {
                		window.alert('로그인이 필요합니다.')
                		return { name: 'LoginView' }
                	}
                	if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin)) {
                		window.alert('이미 로그인이 되어있습니다.')
                		return { name: 'ArticleView' }
                	}
                })
                ```
                
            2. 로그인 후 회원가입, 로그인 페이지 접속 시도

## 참고

### 자연스러운 흐름을 위한 기타 기능 구현

1. 로그인 성공 후 자동으로 메인 페이지로 이동하기
    
    ```jsx
    // stores/counter.js
    
    import { useRouter } from 'vue-router'
    
    export const useCounterStore = defineStore('counter', () => {
    	const router = useRouter()
    	
    	const logIn = function (payload) {
    		...
    			.then(res => {
    				token.value = res.data.key
    				router.push({ name: 'ArticleView' })
    			})
    			.catch(err => console.log(err))
    	}
    ```
    
2. 회원가입 성공 후 자동으로 로그인까지 진행하기
    
    ```jsx
    // stores/counter.js
    
    const signUp = function (payload) {
    	...
    		.then(res => {
    			const password = password1
    			login({ username, password })
    		})
    		.catch(err => console.log(err))
    }
    ```
    

### Django Singals

- “이벤트 알림 시스템”
- 애플리케이션 내에서 특정 이벤트가 발생할 때, 다른 부분에게 신호를 보내어 이벤트가 발생했음을 알릴 수 있음
- 주로 모델의 데이터 변경 또는 저장, 삭제와 같은 작업에 반응하여 추가적인 로직을 실행하고자 할 때 사용
    - 예를 들어, 사용자가 새로운 게시글을 작성할 때마다 특정 작업 (예: 이메일 알림 보내기)을 수행하려는 경우

### 환경 변수 (environment variable)

<aside>
💡

애플리케이션의 설정이나 동작을 제어하기 위해 사용되는 변수

</aside>

- 환경 변수의 목적
    - 개발, 테스트 및 프로덕션 환경에서 다르게 설정되어야 하는 설정 값이나 민감한 정보(ex. API key)를 포함
    - 환경 변수를 사용하여 애플리케이션의 설정을 관리하면, 다양한 환경에서 일관된 동작을 유지하면서 필요에 따라 변수를 쉽게 변경할 수 있음
    - 보안적인 이슈를 피하고, 애플리케이션을 다양한 환경에 대응하기 쉽게 만들어 줌
- Vite에서 환경변수를 사용하는 법
    - .env.local 파일 생성 및 API 변수 작성
    - 주의사항
        - 변수명은 반드시 VITE_ 접두어를 작성해야 함
        - 변수명과 값 사이에 공백이 없어야 함
        - `const API_KEY = import.meta.env.VITE_TMDB_API_KEY`

### Vue 프로젝트 진행 시 유용한 참고 자료

- Awesome Vue.js
    - Vue와 관련하여 선별된 유용한 자료를 아카이빙 및 관리하는 프로젝트
    - [https://github.com/vuejs/awesome-vue](https://github.com/vuejs/awesome-vue)
    - [https://awesome-vue.js.org/](https://awesome-vue.js.org/)
- Vuetify
    - Vue를 위한 UI 라이브러리 (ex. ‘Bootstrap’)
    - [https://vuetifyjs.com/en/](https://vuetifyjs.com/en/)

### 설치한 라이브러리 정리

```bash
$ npm i pinia-plugin-persistedstate
$ npm i axios

$ pip install djangorestframework
$ pip install django-cors-headers
$ pip install dj-rest-auth
$ pip install 'dj-rest-auth[with-social]'
```