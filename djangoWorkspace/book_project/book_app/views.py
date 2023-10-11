from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

# Create your views here.
def index(request):
    return render(request, 'book_app/index.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_app/book_list.html', {'books':books})

def book_detail(request, bookno):
    book = get_object_or_404(Book, pk=bookno)
    return render(request, 'book_app/book_detail.html', {'book':book})

# 도서 등록
def book_insert(request):
    # (1) 요청이 POST 인지 확인하고
    if request.method == 'POST':
        # (2) 폼 데이터의 내용을 form 변수에 저장
        form = BookForm(request.POST)
        # (3) Django의 기본 기능인 is_valid() 사용해서 데이터 유효성 확인
        if form.is_valid():
            # (4) form에 저장된 데이터를 아직 완전 저장하지 않고
            # (현재는 이 부분 없어도 됨)
            book = form.save(commit=False)
            # 수행할 작업이 있다면 여기서 수행 (우리는 현재 다른 작업 없음)

            # (5) 여기에서 DB 저장
            book.save()
            # (6) DB에 저장 후 결과 확인하기 위해 상품조회 화면으로 이동 (포워딩)
            # redirect() 사용
            return redirect('book_list')
    else:
        form = BookForm()    

    # (7) else : POST 요청이 아니라면 입력 폼 그대로 출력
    return render(request, 'book_app/book_form.html', {'form':form})
