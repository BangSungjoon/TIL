# 초심자의 회문 검사
T = int(input())

for test_case in range(1, T + 1):
    word = input().strip()
    if word == word[::-1]:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')