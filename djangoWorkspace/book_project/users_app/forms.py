from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# 회원가입 폼 : 빌트인 폼
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()

        # password는 built-in에 자동으로 포함되어 있어서
        # 여기서 넣으면 두줄이 들어감
        fields = ('username', 'email', 'user_name', 'user_phone', 'user_address')

        labels = {
            'username': 'ID',
            'email': '이메일',
            'user_name': '성명',
            'user_phone': '전화번호',
            'user_address': '주소',
        }