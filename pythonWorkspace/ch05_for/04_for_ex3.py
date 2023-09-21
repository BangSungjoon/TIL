a = int(input('숫자1 입력 : '))
b = int(input('숫자2 입력 : '))

sum = 0
if b > a :
    for i in range(a, b+1):
        sum += i # 누적 대입 연산자
    print(f'{a}부터 {b}까지의 합 : {sum}')
elif a > b :
    for i in range(b, a+1):
        sum += i # 누적 대입 연산자
    print(f'{b}부터 {a}까지의 합 : {sum}')
elif a == b :
    print(f'{a}부터 {b}까지의 합 : {a}')
else :
    exit()