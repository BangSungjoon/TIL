# 5432. 쇠막대기 자르기
T = int(input())

for test_case in range(1, T+1):
    factory = input()
    stack = []
    cnt = 0
    result = 0

    for i in range(len(factory)):
        if factory[i] == '(':
            cnt += 1
        else:
            cnt -= 1
            # 이전의 인덱스가 열린괄호(즉,레이저) 일 때
            if i-1 >= 0 and factory[i-1] =='(':
                result += cnt
            # 레이저가 아니라면
            else:
                result += 1

    print(f'#{test_case} {result}')