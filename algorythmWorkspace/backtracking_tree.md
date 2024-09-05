# 백트래킹 응용 & 그래프(트리)

## 백트래킹 응용

### Backtracking 개념

- 여러 가지 선택지(옵션)들이 존재하는 상황에서 한가지를 선택한다.
- 선택이 이루어지면 새로운 선택지들의 집합이 생성된다.
- 이런 선택을 반복하면서 최종 상태에 도달한다.
    - 올바른 선택을 계속하면 목표 상태(goal state)에 도달한다.
- 당첨 리프 노드 찾기
    - 루트에서 갈 수 있는 노드를 선택한다.
    - 꽝 노드까지 도달하면 최근의 선택으로 되돌아와서 다시 시작한다.
    - 더 이상의 선택지가 없다면 이전의 선택지로 돌아가서 다른 선택을 한다.
    - 루트까지 돌아갔을 경우 더 이상 선택지가 없다면 찾는 답이 없다.
- 백트래킹과 깊이 우선 탐색과의 차이
    - 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임. (Prunning 가지치기)
    - 깊이 우선 탐색이 모든 경로를 추적하는데 비해 백트래킹은 불필요한 경로를 조기에 차단.
    - 깊이 우선 탐색을 가하기에는 경우의 수가 너무나 많음. 즉, N! 가지의 경우의 수를 가진 문제에 대해 깊이 우선 탐색을 가하면 당연히 처리 불가능한 문제.
    - 백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 이 역시 최악의 경우에는 여전히 지수함수 시간(Exponential Time)을 요하므로 처리 불가능
- 루프 노드에서 리프(leaf) 노드까지의 경로는 해답후보(candidate solution)가 되는데, 깊이 우선 탐색을 하여 그 해답후보 중에서 해답을 찾을 수 있다.
- 그러나 이 방법을 사용하면 해답이 될 가능성이 전혀 없는 노드의 후손 노드(descendant)들도 모두 검색해야 하므로 비효율적이다.

<aside>
💡

- 어떤 노드의 유망성을 점검한 후에 유망(promising)하지 않다고 결정되면 그 노드의 부모로 되돌아가(backtracking) 다음 자식 노드로 감.
- 어떤 노드를 방문하였을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 하며, 반대로 해답의 가능성이 있으면 유망하다고 한다.
- 가지치기(prunning): 유망하지 않는 노드가 포함되는 경로는 더 이상 고려하지 않는다.
</aside>

- 백트래킹을 이용한 알고리즘은 다음과 같은 절차로 진행된다.
    1. 상태 공간 트리의 깊이 우선 검색을 실시한다.
    2. 각 노드가 유망한지를 점검한다.
        - 설계 단계에서 유망하지 않은 경우를 생각하고 구현해야 한다.
    3. 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색을 계속한다.

### 문제 제시 : N-Queen 문제

- nxn 서양 장기판에서 배치한 Queen들이 서로 위협하지 않도록 n개의 Queen을 배치하는 문제
    - 어떤 두 Queen도 서로를 위협하지 않아야 한다.
    - Queen을 배치한 n개의 위치는?
        - n값이 11이상인데 factorial로 계산해야 한다면 반 이상 가지치기 해야 한다.
- 후보 해의 수
    - $64!/8!(64 - 8)!$ = 4,426,165,368
- 실제 해의 수
    - 이 중에서 실제 해는 92개 뿐
- 즉, 44억 개가 넘는 후보 해의 수 속에서 92개를 최대한 효율적으로 찾아내는 것이 관건
- 4-Queens 문제로 축소해서 생각해 보자
    - 같은 행에 위치할 수 없다.
    - 모든 경우의 수 : 4x4x4x4 = 256

```python
checknode (node v)
	IF promising(v)
		IF there is a solution at v   # 유망한가?
			write the solution
		ELSE
			FOR each child u of v
				checknode(u)
```

- 코드
    
    ```python
    # 1차원 visited
    def check(row):
        for col in range(row):
            if visited[row] == visited[col]:
                return False
    
            # 열과 행의 차이가 같다 == 현재 col 의 좌우 대각선이다
            if abs(visited[row] - visited[col]) == abs(row - col):
                return False
    
        return True
    
    def dfs(row):
        global cnt
    
        if row == N:
            cnt += 1
            return
    
        for col in range(N):
            visited[row] = col
            if not check(row):
                continue
    
            dfs(row + 1)
    
    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        visited = [0] * N
        cnt = 0
    
        dfs(0)
        print(f'#{tc} {cnt}')
    ```
    
    ```python
    # 2차원 visited
    def check(row, col):
        # 현재 열에 퀸이 있는지 확인
        for i in range(row):
            if visited[i][col] == 1:
                return False
    
        # 왼쪽 대각선 확인
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if visited[i][j] == 1:
                return False
            i -= 1
            j -= 1
    
        # 오른쪽 대각선 확인
        i, j = row - 1, col + 1
        while i >= 0 and j < N:
            if visited[i][j] == 1:
                return False
            i -= 1
            j += 1
    
        # # 왼쪽 대각선 확인
        # for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        #     if visited[i][j] == 1:
        #         return False
        #
        # # 오른쪽 대각선 확인
        # for i, j in zip(range(row - 1, -1, -1), range(col + 1, N)):
        #     if visited[i][j] == 1:
        #         return False
    
        return True
    
    def dfs(row):
        global cnt
    
        if row == N:
            cnt += 1
            return
    
        for col in range(N):
            if check(row, col):
                visited[row][col] = 1
                dfs(row + 1)
                visited[row][col] = 0  # Backtracking
    
    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        visited = [[0] * N for _ in range(N)]
        cnt = 0
    
        dfs(0)
        print(f'#{tc} {cnt}')
    
    ```
    

### [연습 문제 2]

- {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}의 powerset 중 원소의 합이 10인 부분 집합을 모두 출력하시오.
    
    ```python
    # 1,2,3,4,5,6,7,8,9,10}의 powerset 중 원소의 합이 10인 부분집합을 모두 출력하시오.
    # 단, 순서에 따른 중복을 제거하세요
    arr = [i for i in range(1, 11)]
    visited = []
    
    # 버전1
    def dfs(level, sum, idx):
        # 가지치기 : 합이 10이면 종료
        if sum == 10:
            print(*visited)
            return
    
        # 가지치기 : 10이상의 숫자면 볼 필요 없음
        if sum > 10:
            return
    
        for i in range(idx, len(arr)):
            # 가지치기 : 이미 사용한 숫자라면 생략ㅉ
            if arr[i] in visited:
                continue
    
            visited.append(arr[i])
            dfs(level + 1, sum + arr[i], i)
            visited.pop()
    
    # 버전2
    # 트리 구조처럼 사용하면 훨씬 쉽고 빠르다
    def dfs2(level, sum):
        if sum > 10:
            return
    
        if sum == 10:
            print(*visited)
            return
    
        # 모두 선택하지 않으면 합이 10이 넘지 못하므로
        # 기저조건 추가
        if level == len(arr):
            return
    
        # 선택하는 경우
        visited.append(arr[level])
        dfs2(level + 1, sum + arr[level])
        visited.pop()
    
        # 현재 숫자를 선택하지 않는 경우
        dfs2(level + 1, sum)
    
    # dfs(0, 0, 0)
    dfs2(0, 0)
    ```
    

## 트리

[트리와 이진 트리](https://www.notion.so/Tree-1-ee30d3da4c264bb9956810038ff6e6b9?pvs=21)