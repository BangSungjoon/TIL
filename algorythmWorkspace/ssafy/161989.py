def solution(n, m, section):
    answer = 0      # 몇번 칠했는가?
    current = 0     # 현재 마지막으로 칠해진 위치
    for sec in section: # 칠해야 하는 영역 순회
        if sec > current:   # 칠해야 하는 위치가 현재 칠해진 위치보다 크다면
            current = sec + m-1 # 칠해야 하는 칸부터 칠해버려
            answer += 1 # 칠했으니깐 칠한 횟수 추가
    return answer