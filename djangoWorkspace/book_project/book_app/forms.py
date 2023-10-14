from django import forms
from .models import Book

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
            'pubno'
        )

        labels = {
            'bookno': '도서번호',
            'bookname': '도서명',
            'bookauthor': '저자',
            'bookprice': '도서가격',
            'bookdate': '출간일',
            'bookstock': '재고',
            'pubno':'출판사번호'
        }