from django import forms
from .models import Book, Publisher

class BookForm(forms.ModelForm):
    class Meta:
        model = Book  # 도서 정보만 포함하는 모델로 설정
        fields = (
            'bookno',
            'bookname',
            'bookauthor',
            'bookprice',
            'bookdate',
            'bookstock',
        )

        labels = {
            'bookno': '도서번호',
            'bookname': '도서명',
            'bookauthor': '저자',
            'bookprice': '도서가격',
            'bookdate': '출간일',
            'bookstock': '재고',
        }

    # Publisher 모델과의 관련 정보를 입력받을 추가 필드
    pubno = forms.CharField(label='출판사 번호')
    pubname = forms.CharField(label='출판사')

    # 폼 저장(logic) 로직도 추가해야 함