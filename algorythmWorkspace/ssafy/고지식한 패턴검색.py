t = 'TTTTTABC'
p = 'TTA'
N = len(t)
M = len(p)
for i in range(N-M+1): # 비교 시작위치
    for j in range(M):
        if t[i+j] != p[j]:
            break # for j, 다음 글자부터 비교 시작
        else:       # for j가 중단없이 반복되면
            cnt += 1    # 패턴 개수 증가
print(cnt)