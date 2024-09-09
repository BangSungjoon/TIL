# 18863. 5208. [파이썬 S/W 문제해결 구현] 5일차 - 전기버스2
'''
3
5 2 3 1 1
10 2 1 3 2 2 5 4 2 1
10 1 1 2 1 2 2 1 2 1
'''
def change(start, energe, cnt):
    global N, min_cnt
    if energe < 0:
        return
    if min_cnt > cnt:
        if start == N-1:    # 도착했다면
            min_cnt = cnt
            return
        # 충전 안 할 경우
        change(start+1, energe-1, cnt)
        # 충전할 경우
        change(start+1, battery[start]-1, cnt+1)
        # 위치는 한칸 늘어나고, 배터리는 현재 위치에서 교체 했으니 현재 위치 값 - 1
        # 횟수 1회 증가

T = int(input())

for test_case in range(1, T+1):
    battery = list(map(int, input().split()))
    N = battery[0]
    battery = battery[1:] + [0]
    min_cnt = float('inf')

    change(0, battery[0], 0)
    print(f'#{test_case} {min_cnt}')