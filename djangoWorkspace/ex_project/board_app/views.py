from django.shortcuts import render

# Create your views here.
def board_list(request):
    return render(request, 'board_app/board_list.html')

def board_form(request):
    # 전송된 데이터 받기
    # POST 방식으로 전달됐는지 확인 후 변수에 저장
    if request.method == 'POST':
        print(request.POST)
        # 데이터 추출해서 변수에 저장
        comment = {'title' : request.POST['title'], 'content' : request.POST['content']}

        return render(request, 'board_app/board_result.html', {'comment':comment})
    
    # else:
    return render(request, 'board_app/board_form.html')