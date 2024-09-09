# 4012. [모의 SW 역량테스트] 요리사
# N/2개의 부분집합을 만들어보자
def cook(lev, start):
    global result
    if lev == N//2:
        total1 = 0
        for i in range(N//2):
            for j in range(N//2):
                if i != j:
                    total1 += arr[stack1[i]][stack1[j]]
        # 2번 요리 재료 담기
        for i in range(N):
            if i not in stack1:
                stack2.append(i)
        total2 = 0
        for i in range(N//2):
            for j in range(N//2):
                if i != j:
                    total2 += arr[stack2[i]][stack2[j]]
        if result > abs(total2 - total1):
            result = abs(total2 - total1)
        while stack2:
            stack2.pop()

        return

    for i in range(start, N):
        # 1번 요리의 재료로 가질 경우
        stack1.append(i)
        cook(lev+1, i+1)
        stack1.pop()

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = float('inf')  # 최소 시너지 차이 초기값
    visited = [0]*N
    stack1 = []
    stack2 = []
    cook(0, 0)

    print(f'#{test_case} {result}')