from django.shortcuts import render, redirect
from first_app.form import DataForm

# Create your views here.

# (1) 요청 받고
# (2) 화면에 표시 (렌더링)
def index(request):
    return render(request, 'first_app/index.html', {})

# 이미지 페이지 출력
def show_img(request):
    # 데이터 전송 
    # 변수에 값 저장 :  dict 형식
    # member = {}
    # member['name'] = '홍길동'
    # member['age'] = 20

    members = [
        {'name' : '홍길동', 'age':20},
        {'name' : '이몽룡', 'age':30},
        {'name' : '성춘향', 'age':25}
    ]
    return render(request, 'first_app/img.html', {'members':members})
    # return render(request, 'first_app/img.html', {'member':member})
    # return render(request, 'html 페이지', 데이터)

def data_form(request):
    # 전송된 데이터 받기
    # POST 방식으로 전달됐는지 확인 후 변수에 저장
    if request.method == "POST":
        print(request.POST)
        # 데이터 추출해서 변수에 저장
        name = request.POST['name']
        age = request.POST['age']
        print('이름 : ', name)
        print('나이 : ', age)

    return render(request, 'first_app/data_form.html')

def data_form2(request):
    # 전송된 데이터 받기
    # POST 방식으로 전달됐는지 확인 후 변수에 저장
    form = DataForm
    if request.method == "POST":
        print(request.POST)
        form = DataForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name', None)
            age = request.POST.get('age', None)
            print('이름 : ', name)
            print('나이 : ', age)
            # index 페이지로 포워딩 : redirect
            return redirect('/')

    return render(request, 'first_app/data_form2.html', {'form':form})