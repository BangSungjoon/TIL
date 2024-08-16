# 연속한 1의 개수
T = int(input())

for test_case in range(1, T+1):
    N = int(input())    # 수열의 길이
    arr = str(input())  # 문자열로 0과 1을 받기
    max_one_cnt = 0
    cnt = 0

    # 문자열을 순회
    for a in arr:
        # 만약 1이라면 cnt += 1
        if a == '1':
            cnt += 1
        else:   # 0을 만났다면 초기화
            cnt = 0
        # cnt가 최대 길이라면 갱신
        if cnt > max_one_cnt:
            max_one_cnt = cnt

    print(f'#{test_case} {int(max_one_cnt)}')