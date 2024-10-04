# 도넛과 막대 그래프

def solution(edges):
    answer = [0, 0, 0, 0]
    # root 노드를 찾기 -> 정점의 번호
    root_list = []
    for i in range(len(edges)):
        root = edges[i][0]
        cnt = 0                 # 루트의 자식 개수
        for e in edges:
            if e[1] == root:
                root = e[0]
        if root in root_list:   # 전에 등장한 루트라면
            continue            # pass혀
        root_list.append(root)
        # 제한사항
        # 도넛 모양 그래프, 막대 모양 그래프, 8자 모양 그래프의 수의 합은 2이상입니다.
        for e in edges:         # 자식이 2개 이상인지 check
            if e[0] == root:
                cnt += 1
        if cnt >= 2:
            break
    answer[0] = root
    # edges에서 root노드 빼주기
    new_edges = []
    for i in range(len(edges)):
        if edges[i][0] != root:
            new_edges.append(edges[i])


    return answer