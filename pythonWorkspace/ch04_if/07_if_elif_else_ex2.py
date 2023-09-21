a = int(input("도형 입력(1: 사각형, 2: 삼각형, 3: 원) : "))

if a == 1 :
    row = eval(input("가로 입력 : "))
    height = eval(input("세로 입력 : "))
    print('사각형의 면적 : %.2f' %(row * height))
elif a == 2 :
    row = eval(input("밑변 입력 : "))
    height = eval(input("높이 입력 : "))
    print('삼각형의 면적 : %.2f' %(row * height / 2))
else:
    rr = eval(input("반지름 입력 : "))
    print('원의 면적 : %.2f' %(rr * rr * 3.141592))