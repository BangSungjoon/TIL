T = int(input())
for tc in range(1, T+1):
    s = input()
    N = len(s)
    ans = 1
    for i in range(N//2):
        if s[i] != s[N-1-i]:
            ans = 0
            break
    print(f'#{tc} {ans}')