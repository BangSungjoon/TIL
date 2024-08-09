# 간단한 소인수분해
T = int(input())

for test_case in range(1, T+1):
    N = int(input())                # 숫자 N
    prime_num = [2, 3, 5, 7, 11]    # 주어진 소수
    abcde = [0]*5                   # abcde를 담은 리스트

    for i in range(len(prime_num)): # 소수의 수 만큼 순회
        while N % (prime_num[i] ** abcde[i]) == 0:  # 소수로 나눠서 나머지가 0인 동안 반복
            abcde[i] += 1           # 해당 abcde 증가
        abcde[i] -= 1               # 각 소수의 0제곱(=1)에도 abcde가 증가했으니깐 하나 빼주기
    print(f'#{test_case}', *abcde)  # 출력