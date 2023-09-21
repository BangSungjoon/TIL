i = 1 # 초기값
sum = 0
while i <= 100 :
    if i % 3 == 0 :
        sum += i
    i += 1 # 증감식 : 1씩 증가

print(f'1부터 {i-1}까지 모든 3의 배수의 합은 {sum}입니다.')