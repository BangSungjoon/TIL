# Many to many relationships 1

## N:M or M:N

<aside>
💡

한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우

- 양쪽 모두에서 N:1 관계를 가짐
</aside>

### M:N 관계의 역할과 필요성 이해하기

- ‘병원 진료 시스템 모델 관계’를 만들며 M:N 관계의 역할과 필요성 이해하기
- 환자와 의사 2개의 모델을 사용하여 모델 구조 구상하기

### N:1의 한계

- 동일한 환자지만 다른 의사에게도 진료 받기 위해 예약하기 위해서는 객체를 하나 더 만들어 진행해야 함
- 외래 키 컬럼에 ‘1, 2’ 형태로 저장하는 것은 DB 타입 문제로 불가능
    - “예약 테이블을 따로 만들자”

### 예약 모델 생성

- 환자 모델의 외래 키를 삭제하고 별도의 예약 모델을 새로 생성
- 예약 모델은 의사와 환자에 각각 N:1 관계를 가짐
    
    ```python
    class Doctor(models.Model):
        name = models.TextField()
    
        def __str__(self):
            return f'{self.pk}번 의사 {self.name}'
    
    # 외래키 삭제
    class Patient(models.Model):
        name = models.TextField()
    
        def __str__(self):
            return f'{self.pk}번 환자 {self.name}'
    
    # 중개모델 작성
    class Reservation(models.Model):
        doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
        patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
        def __str__(self):
            return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
    ```
    

### 예약 데이터 생성

- 데이터베이스 초기화 후 Migration 진행 및 shell_plus 실행
- 의사와 환자 생성 후 예약 만들기
    
    ```python
    doctor1 = Doctor.objects.create(name='allie')
    patient1 = Patient.objects.create(name='carol')
    
    Reservation.objects.create(doctor=doctor1, patient=patient1)
    ```
    

### 예약 정보 조회

- 의사와 환자가 예약 모델을 통해 각각 본인의 진료 내역 확인
    
    ```python
    # 의사 -> 예약 정보 찾기
    doctor1.reservation_set.all()
    <QuerySet [<Reservation: 1번 의사의 1번 환자>]>
    
    # 환자 -> 예약 정보 찾기
    patient1.reservation_set.all()
    <QuerySet [<Reservation: 1번 의사의 1번 환자>]>
    ```
    

### 추가 예약 생성

- 1번 의사에게 새로운 환자 예약 생성
    
    ```python
    patient2 = Patient.objects.create(name='duke')
    
    Reservation.objects.create(doctor=doctor1, patient=patient2)
    ```
    

### 예약 정보 조회

- 1번 의사의 예약 정보 조회
    
    ```python
    # 의사 -> 환자 목록
    doctor1.reservation_set.all()
    <QuerySet [<Reservation: 1번 의사의 1번 환자>, <Reservation: 1번 의사의 2번 환자>]>
    ```
    

## ManyToManyField

<aside>
💡

Django에서는 ‘ManyToManyField’로 중개 모델을 자동으로 생성

</aside>

`ManyToManyField(to, **options)`

- M:N 관계 설정 모델 필드
- 양방향 관계
    - 어느 모델에서든 관련 객체에 접근할 수 있음
- 중복 방지
    - 동일한 관계는 한 번만 저장됨
1. 환자 모델에 ManyToManyField 작성
    - 의사 모델에 작성해도 상관 없으며 참조/역참조 관계만 잘 기억할 것
    
    ```python
    class Patient(models.Model):
        # ManyToManyField 작성
        doctors = models.ManyToManyField(Doctor)
        name = models.TextField()
    
        def __str__(self):
            return f'{self.pk}번 환자 {self.name}'
    
    # Reservation Class 주석 처리
    ```
    
2. 데이터베이스 초기화 후 Migration 진행 및 shell_plus 실행
3. 생성된 중개 테이블 hospitals_patient_doctors 확인
4. 의사 1명과 환자 2명 생성
    
    ```python
    doctor1 = Doctor.objects.create(name='allie')
    patient1 = Patient.objects.create(name='carol')
    patient2 = Patient.objects.create(name='duke')
    ```
    
5. 예약 생성 (환자가 예약)
    
    ```python
    # patient1이 doctor1에게 예약
    patient1.doctors.add(doctor1)
    
    # patient1 - 자신이 예약한 의사목록 확인
    patient1.doctors.all()
    <QuerySet [<Doctor: 1번 의사 alice>]>
    
    # doctor1 - 자신의 예약된 환자목록 확인
    doctor1.patient_set.all()
    <QuerySet [<Patient: 1번 환자 carol>]>
    ```
    
6. 예약 생성 (의사가 예약)
    
    ```python
    # doctor1이 patient2을 예약
    doctor1.patient_set.add(patient2)
    
    # doctor1 - 자신의 예약 환자목록 확인
    doctor1.patient_set.all()
    <QuerySet [<Patient: 1번 환자 carol>, <Patient: 2번 환자 duke>]>
    
    # patient1, 2 - 자신이 예약한 의사목록 확인
    patient1.doctors.all()
    <QuerySet [<Doctor: 1번 의사 alice>]>
    
    patient2.doctors.all()
    <QuerySet [<Doctor: 1번 의사 alice>]>
    ```
    
7. 예약 취소하기 (삭제)
    - 이전에는 Reservation을 찾아서 지워야 했다면, 이제는 .remove()로 삭제 가능
    
    ```python
    # doctor1이 partient1 진료 예약 취소
    
    doctor1.patient_set.remove(patient1)
    
    doctor1.patient_set.all()
    <QuerySet [<Patient: 2번 환자 duke>]>
    
    patient1.doctors.all()
    <QuerySet []>
    ```
    
    ```python
    # patient2가 doctor1 진료 예약 취소
    
    patient2.doctors.remove(doctor1)
    
    patient2.doctors.all()
    <QuerySet []>
    
    doctor1.patient_set.all()
    ```
    

<aside>
❓

만약 예약 정보에 병의 증상, 예약일 등 추가 정보가 포함되어야 한다면?

</aside>

### ‘through’ argument

중계 테이블에 ‘추가 데이터’를 사용해 M:N 관계를 형성하려는 경우에 사용

1. Reservation Class 재작성 및 through 설정
    - 이제는 예약 정보에 ‘증상’과 ‘예약일’이라는 추가 데이터가 생김
    
    ```python
    class Patient(models.Model):
        doctors = models.ManyToManyField(Doctor, through='Reservation')
        name = models.TextField()
    
        def __str__(self):
            return f'{self.pk}번 환자 {self.name}'
    
    class Reservation(models.Model):
        doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
        patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
        symptom = models.TextField()
        reserved_at = models.DateTimeField(auto_now_add=True)
    
        def __str__(self):
            return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'
    ```
    
2. 데이터베이스 초기화 후 Migration 진행 및 shell_plus 실행
    - 의사 1명과 환자 2명 생성
    
    ```python
    doctor1 = Doctor.objects.create(name='allie')
    patient1 = Patient.objects.create(name='carol')
    patient2 = Patient.objects.create(name='duke')
    ```
    
3. 예약 생성 방법 - 1
    - Reservation class를 통한 예약 생성
    
    ```python
    # 1. Reservation class를 통한 예약 생성
    reservation1 = Reservation(doctor=doctor1, patient=patient1, symptom='headache')
    reservation1.save()
    
    doctor1.patient_set.all()
    <QuerySet [<Patient: 1번 환자 carol>]>
    
    patient1.doctors.all()
    <QuerySet [<Doctor: 1번 의사 alice>]>
    ```
    
4. 예약 생성 방법 - 2
    - Patient 또는 Doctor의 인스턴스를 통한 예약 생성 (through_defaults)
    
    ```python
    # 2. Patient 객체를 통한 예약 생성
    patient2.doctors.add(doctor1, through_defaults={'symptom': 'flu'})
    
    doctor1.patient_set.all()
    <QuerySet [<Patient: 1번 환자 carol>, <Patient: 2번 환자 duke>]>
    
    patient2.doctors.all()
    <QuerySet [<Doctor: 1번 의사 alice>]>
    ```
    
5. 생성과 마찬가지로 의사와 환자 모두 각각 예약 삭제 가능
    
    ```python
    doctor1.patient_set.remove(patient1)
    
    patient2.doctors.remove(doctor1)
    ```
    

### M:N 관계 주요 사항

- M:N 관계로 맺어진 두 테이블에는 물리적인 변화가 없음
- ManyToManyField는 중개 테이블을 자동으로 생성
- ManyToManyField는 M:N 관계를 맺는 두 모델 어디에 위치해도 상관 없음
    - 대신 필드 작성 위치에 따라 참조와 역참조 방향을 주의할 것
- N:1은 완전한 종속의 관계였지만 M:N은 종속적인 관계가 아니며 ‘의사에게 진찰받는 환자 & 환자를 진찰하는 의사’ 이렇게 2가지 형태 모두 표현 가능

### ManyToManyField의 대표 인자 3가지

1. ‘**related_name**’ arguments
    - 역참조시 사용하는 manager name을 변경
    
    ```python
    class Patient(models.Model):
    	doctors = models.ManyToManyField(Doctor, related_name='patients')
    	name = models.TextField()
    ```
    
    ```python
    # 변경 전
    doctor.patient_set.all()
    
    # 변경 후 (변경 후 이전 manager name은 사용 불가)
    doctor.patients.all()
    ```
    
2. ‘**symmetrical**’ arguments
    - 관계 설정 시 대칭 유무 설정
    - ManyToManyField가 동일한 모델을 가리키는 정의에서만 사용
    - 기본 값 : True
    
    ```python
    # 예시
    
    class Person(models.Model):
    	friends = models.ManyToManyField('self')
    	# friends = models.ManyToManyField('self', symmetrical=False)
    ```
    
    - True일 경우
        - source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면 자동으로 target 모델 인스턴스도 source 모델 인스턴스를 자동으로 참조하도록 함(대칭)
        - 즉, 내가 당신의 친구라면 자동으로 당신도 내 친구가 됨
    - False일 경우
        - True와 반대 (대칭되지 않음)
3. ‘**through**’ arguments
    - 사용하고자 하는 중개모델을 지정
    - 일반적으로 “추가 데이터를 M:N 관계와 연결하려는 경우”에 활용

### M:N에서의 대표 조작 methods

- add()
    - 관계 추가
    - “지정된 객체를 관련 객체 집합에 추가”
- remove()
    - 관계 제거
    - “관련 객체 집합에서 지정된 모델 객체를 제거”

## 좋아요 기능 구현

### Article(M) - User(N)

0개 이상의 게시글은 0명 이상의 회원과 관련

- 게시글은 회원으로부터 0개 이상의 좋아요를 받을 수 있고, 회원은 0개 이상의 게시글에 좋아요를 누를 수 있음

### 모델 관계 설정

1. Article 클래스에 ManyToManyField 작성
    
    ```python
    # articles/models.py
    
    class Article(models.Model):
    	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    	like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    	title = models.CharField(max_length=10)
    	content = models.TextField()
    	created_at = models.DateTimeField(auto_now_add=True)
    	updated_at = models.DateTimeField(auto_now=True)
    ```
    
2. Migration 진행 후 에러 발생
    - 역참조 매니저 충돌
        - N:1
            - “유저가 작성한 게시글”
            - user.article_set.all()
        - M:N
            - “유저가 좋아요 한 게시글”
            - user.article_set.all()
        - like_users 필드 생성 시 자동으로 역참조 매니저 **.article_set**가 생성됨
        - 그러나 이전 N:1(Article-User) 관계에서 이미 같은 이름의 매니저를 사용 중
            - **user.article_set.all()** → 해당 유저가 작성한 모든 게시글 조회
        - ‘user가 작성한 글 (user.article_set)’과 ‘user가 좋아요를 누른 글(user.article_set)’을 구분할 수 없게 됨
            
            → user와 관계된 ForeignKey 혹은 ManyToManyField 둘 중 하나에 **related_name** 작성 필요
            
3. related_name 작성 후 Migration 재진행
    
    ```python
    # articles/models.py
    
    class Article(models.Model):
    	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    	like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    	title = models.CharField(max_length=10)
    	content = models.TextField()
    	created_at = models.DateTimeField(auto_now_add=True)
    	updated_at = models.DateTimeField(auto_now=True)
    ```
    

### User - Article간 사용 가능한 전체 related manager

- article.user
    - 게시글을 작성한 유저 - N:1
- user.article_set
    - 유저가 작성한 게시글(역참조) - N:1
- article.like_users
    - 게시글을 좋아요 한 유저 - M:N
- user.like_articles
    - 유저가 좋아요 한 게시글(역참조) - M:N

### 기능 구현

1. url 작성
    
    ```python
    # articles/urls.py
    
    urlpatterns = [
    	...
    	path('<int:article_pk>/likes/', views.likes, name='likes'),
    ]
    ```
    
2. view 함수 작성
    
    ```python
    # articles/views.py
    
    @login_required
    def likes(request, article_pk):
    	article = Article.objects.get(pk=article_pk)
    	if request.user in article.like_users.all():
    		article.like_users.remove(request.user)
    	else:
    		article.like_users.add(request.user)
    	return redirect('articles:index')
    ```
    
3. index 템플릿에서 각 게시글에 좋아요 버튼 출력
    
    ```html
    <!-- articles/index.html -->
    
    {% for article in articles %}
    	...
    	<form action="{% url 'articles:likes' article.pk %}" method="POST">
    		{% csrf_token %}
    		{% if request.user in article.like_users.all %}
    			<input type="submit" value="좋아요 취소">
    		{% else %}
    			<input type="submit" value="좋아요">
    		{% endif %}
    	</form>
    	<hr>
    {% endfor %}
    ```