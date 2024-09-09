# 18729. 5201. 컨테이너 운반
for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    total = 0

    for i in truck:
        container.sort(reverse=True)
        for j in range(N):
            # 최대 적재용량 이하라면
            if container[j] <= i:
                total += container[j]
                container[j] = 0
                break

    print(f'#{test_case} {total}')