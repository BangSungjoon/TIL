from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm
from .models import User

# Create your views here.

# 로그인 : AuthenticationForm 사용
def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect('index') # index를 불러오는 담당자를 호출한다
        
    else:
        form = AuthenticationForm()

    return render(request, 'users_app/sign_in.html', {'form':form})

# 로그아웃
def sign_out(request):
    logout(request)
    return redirect('index')

# 회원가입
def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('sign_in') # 회원가입 후 로그인화면으로 이동
    else:
        form = CustomUserCreationForm()

    return render(request, 'users_app/sign_up.html', {'form':form})