# 16633. 5097. [파이썬 S/W 문제해결 기본] 6일차 - 회전
T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())    # N개의 숫자, M번 뒤로 보내기
    numbers = list(map(int, input().split()))   # N개의 숫자 받아오기
    arr = [0]*(N+M)                     # 뒤로 보내기를 구현할 새 배열
    for i in range(N):                  # N개의 숫자 채우기
        arr[i] = numbers[i]             # 인덱스 0부터 N-1까지는 원래의 배열
    front = 0                           # queue의 front
    rear = N-1                          # queue의 rear

    for _ in range(M):
        rear += 1
        arr[rear] = arr[front]
        front += 1

    print(f'#{test_case} {arr[front]}')