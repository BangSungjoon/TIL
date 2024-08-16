# 1860. 진기의 최고급 붕어빵
T = int(input())

for test_case in range(1, T+1):
    # N: 자격을 얻은 자..., M: 붕어빵 만드는 시간, K: 만들 수 있는 붕어빵의 수
    N, M, K = map(int, input().split())
    # N명의 손님이 도착하는 각각의 시간
    arr_time = list(map(int, input().split()))

    # time: 시간, bbang: 붕어빵 잔고
    time = -1
    bbang = 0
    result = 'Possible'
    cnt = 0         # 사간 손님의 수

    while cnt < N:  # 사간 손님이 전체 손님의 수가 될 때 까지
        time += 1   # 시간은 1초씩 흐른다.
        if time != 0 and time % M == 0:   # 시간이 0이 아니고 M의 배수라면
            bbang += K      # 붕어빵 잔고 추가
        for i in range(len(arr_time)):   # 도착 시간 리스트 중에 현재시간과 일치하는 시간이 있다면
            if time == arr_time[i]:
                bbang -= 1
                cnt += 1                 # 사간 손님 하나 추가욧
        if bbang < 0:   # 만약 빵이 음수라면
            result = 'Impossible'
            break

    print(f'#{test_case} {result}')
