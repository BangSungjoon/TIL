def get_average(ko, en, math):
    avg = (ko + en + math) / 3
    print('평균 : ', avg)

a = int(input('국어 점수 입력 : '))
b = int(input('영어 점수 입력 : '))
c = int(input('수학 점수 입력 : '))

get_average(a, b, c)