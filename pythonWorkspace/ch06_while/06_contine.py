# continue 문

x = 0

while x < 10:
    x += 1
    if x % 2 == 0: # 짝수이면
        continue   # 다음의 print(x) 건너뛰고 다음반복으로 계속 진행

    print(x)