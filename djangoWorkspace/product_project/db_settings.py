DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",  # 엔진
        "NAME": "django_db",  # 데이터베이스 이름
        "USER": "root",  # 사용자
        "PASSWORD": "1234",  # 비밀번호
        "HOST": "localhost",  # 호스트
        "PORT": "3306",  # 포트번호
    }
}

# SECRET_KEY
# settings.py에서 복사하고
# settings.py의 SECRET_KEY는 주석 처리함
SECRET_KEY = 'django-insecure-2c*m%g3=s_#^fx)4n@uz6d$utqblslresuh#f+#ma$4@-!q69$'