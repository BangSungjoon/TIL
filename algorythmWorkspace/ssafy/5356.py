# 의석이의 세로로 말해요
T = int(input())

for test_case in range(1, T + 1):
    word_list = [0]*5
    n=0
    max_len = 0
    cnt = 0

    for i in range(5):
        word_list[i] = input()
        n += len(word_list[i])
        if max_len < len(word_list[i]):
            max_len = len(word_list[i])

    result = [0]*n
    try:
        for j in range(max_len):
            for i in range(5):
                result[cnt] = word_list[i][j]
    except:
        continue

    print(result)