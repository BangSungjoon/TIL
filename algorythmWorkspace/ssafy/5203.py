# 18686. 5203. 베이비진 게임
def runcheck(arr, level, idx):
    # arr은 입력 받은 배열(player1 또는 player2), level은 재귀 횟수 기록
    # idx는 현재 패의 index
    global win
    # 기저조건
    if level == 3:
        win = True
        return

    if idx >= len(arr):  # idx가 배열의 길이를 초과하지 않도록 조건 추가
        return

    if level == 0:    # 첫 번째 입력일 경우
        runcheck(arr, level+1, idx+1)
    else:             # 첫 번째 입력이 아닐 경우
        if arr[idx] == arr[idx-1]+1:    # 연속하는 숫자일 경우 재귀
            runcheck(arr, level+1, idx+1)
        else:                           # 연속하는 숫자가 아니라면
            return                      # 반환

def triple(arr, level, idx):
    # arr은 입력 받은 배열(player1 또는 player2), level은 재귀 횟수 기록
    # idx는 현재 패의 index
    global win
    # 기저조건
    if level == 3:
        win = True
        return

    if idx >= len(arr):  # idx가 배열의 길이를 초과하지 않도록 조건 추가
        return

    if level == 0:    # 첫 번째 입력일 경우
        triple(arr, level+1, idx+1)
    else:             # 첫 번째 입력이 아닐 경우
        if arr[idx] == arr[idx-1]:    # 같은 숫자일 경우 재귀
            triple(arr, level+1, idx+1)
        else:                           # 연속하는 숫자가 아니라면
            return                      # 반환


for test_case in range(1, int(input())+1):
    cards = list(map(int, input().split()))
    player1 = []
    player2 = []
    win = False

    for i in range(12):
        if i % 2 == 0:  # 짝수 턴일때 -> player1 순서
            player1.append(cards[i])
            run_player1 = sorted(set(player1))
            tri_player1 = sorted(player1)
            if i >= 4:
                for j in range(len(run_player1)):
                    runcheck(run_player1, 0, j)
                    if win:
                        break
                for j in range(len(tri_player1)):
                    triple(tri_player1, 0, j)
                    if win:
                        break

                if win:
                    print(f'#{test_case} 1')
                    break
        else:
            player2.append(cards[i])
            run_player2 = sorted(set(player2))
            tri_player2 = sorted(player2)
            if i >= 5:
                for j in range(len(run_player2)):
                    runcheck(run_player2, 0, j)
                    if win:
                        break
                for j in range(len(tri_player2)):
                    triple(tri_player2, 0, j)
                    if win:
                        break

                if win:
                    print(f'#{test_case} 2')
                    break
    else:
        print(f'#{test_case} 0')