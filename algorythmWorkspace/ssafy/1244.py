# 1244. [S/W 문제해결 응용] 2일차 - 최대 상금
def brute(cnt):
    global chance, max_total, visited
    # 기저조건
    if cnt == chance:
        total = int(''.join(num))
        if total > max_total:
            max_total = total
        return

    n = len(num)
    total = ''.join(num)

    if (total, cnt) in visited:     # 이미 방문했던 합계라면 pass
        return
    visited.add((total, cnt))

    # 순회하며 자리 바꾸기
    for i in range(n):
        for j in range(n):
            if i != j:
                num[i], num[j] = num[j], num[i]
                brute(cnt+1)
                num[i], num[j] = num[j], num[i]

T = int(input())

for test_case in range(1, T+1):
    num, chance = map(int, input().split())
    num = list(str(num))
    max_total = -999999999999
    visited = set()
    brute(0)
    print(f'#{test_case} {max_total}')
