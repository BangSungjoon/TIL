# 18730. 5202. 화물 도크
for test_case in range(1, int(input())+1):
    N = int(input())
    work = [list(map(int, input().split())) for _ in range(N)]
    work.sort(key=lambda x: x[1]-x[0])  # 작업에 걸리는 시간 순으로 배열
    cnt = 0
    done = []   # 완료한 작업을 저장할 배열
    while work:
        w = work.pop(0)     # 검사할 배열
        if done:            # 작업 완료 배열이 있을 경우
            for i in range(len(done)):
                if done[i][0] < w[0] < done[i][1] or done[i][0] < w[1] < done[i][1] or w[0] < done[i][0] < w[1] or w[0] < done[i][1] < w[1]:
                    # 정상 범위가 아닐 경우
                    break
                if w in done:   # 이미 완료한 작업과 같은거라면 불가능
                    break
            else:   # 무사히 순회를 돌았다면
                cnt += 1
                done.append(w)
        else:               # 작업 완료 배열이 없을 경우
            done.append(w)
            cnt += 1

    print(f'#{test_case} {cnt}')