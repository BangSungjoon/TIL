T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    n_list = list(map(int, input().split()))
    n_max = n_list[0]
    n_min = n_list[0]  # 첫 번째 요소로 초기화

    for i in range(1, n):
        if n_max < n_list[i]:
            n_max = n_list[i]
        if n_min > n_list[i]:
            n_min = n_list[i]

    print(f'#{test_case} {n_max - n_min}')

'''
input
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175
'''