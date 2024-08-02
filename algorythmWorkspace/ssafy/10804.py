T = int(input())

for test_case in range(1, T + 1):
    word = list(input().strip())
    mirror = [0] * len(word)
    for i in range(len(word)):
        if word[-i-1] == 'b':
            mirror[i] = 'd'
        elif word[-i-1] == 'd':
            mirror[i] = 'b'
        elif word[-i-1] == 'p':
            mirror[i] = 'q'
        elif word[-i-1] == 'q':
            mirror[i] = 'p'
    mirror = ''.join(mirror)
    print(f'#{test_case} {mirror}')