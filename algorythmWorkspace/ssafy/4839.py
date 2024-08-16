# 16284. 4839. 이진탐색
def bi_search(I, r, target_page):   # 재귀함수로 풀어보기!
    c = int((I + r)/2)
    global cnt
    cnt += 1
    if c == target_page:
        return cnt
    elif c > target_page:   # 찾고자 하는 페이지보다 중간 페이지가 더 크다면
        return bi_search(I, c, target_page) # 검색 구간의 왼쪽은 유지, 오른쪽은 중간 페이지
    else:                   # 중간 페이지가 찾고자 하는 페이지보다 크다면
        return bi_search(c, r, target_page) # 반대

T = int(input())

for test_case in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    cnt = 0 # cnt 초기화
    a_cnt = bi_search(1, P, Pa)
    cnt = 0 # cnt 초기화
    b_cnt = bi_search(1, P, Pb)

    if a_cnt < b_cnt:
        print(f'#{test_case} A')
    elif a_cnt > b_cnt:
        print(f'#{test_case} B')
    else:
        print(f'#{test_case}', 0)