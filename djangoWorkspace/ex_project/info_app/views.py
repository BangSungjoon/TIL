from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'info_app/index.html')

def info(request):
    return render(request, 'info_app/info.html')

def board_list(request):
    return render(request, 'board_app/board_list.html')