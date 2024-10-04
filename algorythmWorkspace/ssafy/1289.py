# 원재의 메모리 복구하기
T = int(input())

for test_case in range(1, T+1):
    memory = input()
    current = ['0']*len(memory)
    cnt = 0

    for i in range(len(memory)):
        if current == memory:
            break
        if current[i] != memory[i]:     # 현재의 i번째 칸과 원본의 i번째 칸이 같지 않다면
            cnt += 1                    # 수정할거임 횟수 하나 추가욧
            current[i:] = memory[i]*len(current[i:])     # 바꿔버려잇

    print(f'#{test_case} {cnt}')