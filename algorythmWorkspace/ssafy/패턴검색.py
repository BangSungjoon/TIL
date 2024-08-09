target = 'Hello SSAFY 12th!' # target 패턴을 찾을 대상
pattern = 'SSA' # 우리가 찾을 패턴

def BruteForce(pat, text):
    N = len(text)
    M = len(pat)
    i = 0 # text의 인덱스
    j = 0 # 패턴의 인덱스

    while j < M and i < N:
        # 틀린 곳을 발견했다면, index 값을 초기화 시킴.
        if text[i] != pat[j]:
            # text의 현재 위치에서 일치하지 않는 곳을 발견!
            # 지금위치 -j
            i = i - j
            j = -1
        i = i + 1
        j = j + 1

        # 검색 성공
        if j == M:
            return i - M
        else:
            return -1


# 심플 버전
text = "This is simple version"
pattern = 'vision'
def BruteForceV2(pat, text):
    for idx in range(len(text) - len(pat) + 1):
        # 패턴을 처음부터 끝까지 순회
        for j in range(len(pattern)):
            # 1. 다르면
            if text[idx + j] != pat[j]:
                break
        # 같다면(다른게 없다면)
        else:
            return idx
    else:
        return -1

a = BruteForceV2(pattern, text)
print(a)