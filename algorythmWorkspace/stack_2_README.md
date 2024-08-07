# Stack 2

## Memorization

- 앞의 예에서 피보나치 수를 구하는 함수를 재귀 함수로 구현한 알고리즘은 문제점이 있다.
    - “엄청난 중복 호출이 존재한다”는 것이다.
- 메모이제이션(memoization)은 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술이다. 동적 계획법의 핵심이 되는 기술이다.
- ‘memoization’은 글자 그대로 해석하면 ‘메모리에 넣기(to put in memory)’라는 의미이며 ‘기억되어야 할 것’이라는 뜻의 라틴어 memorandum에서 파생되었다. 흔히 ‘기억하기’,’암기하기’라는 뜻의  memorization과 혼동하지만, 정확한 단어는 memoization이다. 동사형은 memoize이다.
- 피보나치 수를 구하는 알고리즘에서 fibo(n)의 값을 계산하자마자 저장하면(memoize), 실행시간을 Θ(n)으로 줄일 수 있다.
    
    ```python
    # memo를 위한 배열을 할당하고, 모두 0으로 초기화한다
    # memo[0]을 0으로 memo[1]는 1로 초기화 한다
    
    def fibo1(n):
    	global memo
    	if n >= 2 and memo[n] == 0:
    		memo[n] = fibo1(n-1) + fibo1(n-2)
    	return memo[n]
    
    def fibo(n):
        if n<2:
            return n
        else:
            return fibo(n-1) + fibo(n-2)
    
    n = 90
    memo = [0] * (n+1)
    memo[0] = 0
    memo[1] = 1
    print(fibo1(n))
    ```
    
    엄청난 속도 차이가 난다.
    

### DP(Dynamic Programming)

- 동적 계획(Dynamic Programming) 알고리즘은 그리디 알고리즘과 같이 최적화 문제를 해결하는 알고리즘이다.
- 동적 계획 알고리즘은 먼저 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘이다.
- 피보나치 수 DP 적용
    - 피보나치 수는 부분 문제의 답으로부터 본 문제의 답을 얻을 수 있으므로 최적 부분 구조로 이루어져 있다.
    1. 문제를 부분 문제로 분할한다.
    2. 부분 문제로 나누는 일을 끝냈으면 가장 작은 부분 문제부터 해를 구한다.
    3. 그 결과는 테이블에 저장하고, 테이블에 저장된 부분 문제의 해를 이용하여 상위 문제의 해를 구한다.
    
    ```python
    def fibo2(n):
    	f = [0] * (n+1)
    	f[0] = 0
    	f[1] = 1
    	for i in range(2, n+1):
    		f[i] = f[i-1] + f[i-2]
    	
    	return f[n]
    ```
    
- DP의 구현 방식
    - recursive 방식 : fibo1()
    - iterative 방식 : fibo2()
    - memoization을 재귀적 구조에 사용하는 것보다 반복적 구조로 DP를 구현한 것이 성능 면에서 보다 효율적이다.
    - 재귀적 구조는 내부에 시스템 호출 스택을 사용하는 오버헤드가 발생하기 때문이다.

### DFS(깊이우선탐색)

- 비선형구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요함.
- 두 가지 방법
    - 깊이 우선 탐색(Depth First Search, DFS) → 오늘의 주제
    - 너비 우선 탐색(Breadth First Search, BFS)
- 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳 까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회 방법
- 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 후입선출 구조의 스택 사용
    - 재귀를 사용해서도 구현할 수 있다.
1. 시작 정점 v를 결정하여 방문한다.
2. 정점 v에 인접한 정점 중에서
    1. 방문하지 않은 정점 w가 있으면, 정점 v를 스택에 push하고 정점 w를 방문한다. 그리고 w를 v로 하여 다시 2.를 반복한다.
    2. 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 2.를 반복한다.
3. 스택이 공백이 될 때까지 2.를 반복한다.

```python
sudo 코드
visited[], stack[] 초기화
DFS(v)
	시작점 v 방문;
	visited[v] <- true;
	while {
		if ( v의 인접 정점 중 방문 안 한 정점 w가 있으면)
			push(v);
			v <- w; (w에 방문)
			visited[w] <- true;
		else
			if (스택이 비어 있지 않으면)
				v <- pop(stack);
			else
				break
	}
end DFS()
```

```python
import sys
from pprint import pprint

sys.stdin = open('input.txt')

# 맨 앞이 빈 이유는 인덱스를 1부터 세고 싶기 때문이다.
node = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G']

'''
인접 행렬 (adjacency matrix)
- n x n 크기의 정사각형 행렬
- 노드들 간의 연결 관계를 행렬로 표현한 것
- 무방향 그래프에서는
    - 정점 i와 j 사이에 간선이 있다면 matrix[i][j] = matrix[j][i] = 1, 없으면 0
'''
# 인접 그래프를 행렬로 표현하는 방법
#       A  B  C  D  E  F  G
matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],   # A
    [0, 1, 0, 0, 1, 1, 0, 0],   # B
    [0, 1, 0, 0, 0, 1, 0, 0],   # C
    [0, 0, 1, 0, 0, 0, 1, 0],   # D
    [0, 0, 1, 1, 0, 0, 1, 0],   # E
    [0, 0, 0, 0, 1, 1, 0, 1],   # F
    [0, 0, 0, 0, 0, 0, 1, 0]    # G
]

# s: 시작 정점 V: 간선의 개수
def DFS(s, V):
    # stack에 시작 정점을 push
    stack = [s]
    # 방문 여부를 체크하는 리스트
    visited = [0] * (V+1)

    # 스택이 빌때까지 DFS 진행 (스택에 값이 있는 동안 진행)
    while stack:
        # 현재 조사할 노드
        current = stack.pop()

        # 방문하지 않은 노드라면
        if visited[current] == 0:
            # 방문 표시
            visited[current] = 1
            # 방문한 노드 출력
            print(node[current])

            # 현재 노드에서 갈 수 있는 다음 노드들을 스택에 추가
            # V부터 1까지 역순으로 확인 (작은 번호의 노드가 스택의 위쪽으로 위치하게 됨)
            for next in range(V, 0, -1):
                # 다음 노드가 간선이 연결이 되어있고 + 방문한 적이 없다면
                if matrix[current][next] == 1 and visited[next] == 0:
                    # stack에 push
                    stack.append(next)
            # 큰 번호 우선 탐색을 한다면 (C부터 탐색)
            # for next in range(1, V+1):

# 인접행렬 만들기
# V = 노드의 개수
# E = 간선의 개수
V, E = map(int, input().split())

adj_matrix = [[0] * (V+1) for _ in range(V+1)]

# 노드별 간선 정보
data = list(map(int, input().split()))

# 간선 정보를 넣기
# 간선의 개수만큼 반복하면서 넣기
for _ in range(E):
    # i, j = map(int, input().split())
    # adj_matrix[i][j] = 1
    # adj_matrix[j][i] = 1
    n1 = data[i * 2]
    n2 = data[i * 2 + 1]
    adj_matrix[n1][n2] = 1
    adj_matrix[n2][n1] = 1

DFS(1, 7)
```

---

## 연습 문제

- 다음은 연결되어 있는 두 개의 정점 사이의 간선을 순서대로 나열해 놓은 것이다. 모든 정점을 깊이 우선 탐색하여 화면에 깊이 우선 탐색 경로를 출력하시오. 시작 정점을 1로 시작하시오.
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
    - 출력 결과의 예는 다음과 같다.
    1 2 4 6 5 7 3
    
    ```python
    '''
    1
    7 8
    1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
    '''
    def DFS(s, V):          #s 시작정점, V 정점개수(1번부터인 정점의 마지막 정점)
        visited = [0] *(V+1) #방문한 정점을 표시
        stack = []    #스택생성
        print(s)
        visited[s] = 1      #시작 정점 방문 표시
        v = s
        while True:
            for w in adjL[v]: # v에 인접하고, 방문안한 w가 있으면
                if visited[w] == 0:
                    stack.append(v)#push(v) 현재 정점을 push하고
                    v = w  #w에 방문
                    print(v)
                    visited[w] = 1   #w에 방문 표시
                    break           #for w에 대한 break. v부터 다시 탐색
            else:                   #남은 인접 정점이 없어서 break가 걸리지 않은 경우
                if stack:  #이전 갈림길을 스택에서 꺼내서.. if TOP > -1
                    v = stack.pop()
                else: #되돌아갈 곳이 없으면, 남은 갈림길이 없으면 탐색 종료
                    break #while True: 에 대한 break
    
    T = int(input())
    for tc in range(1, T+1):
        V, E = map(int, input().split())
        adjL = [[] for _ in range(V+1)]
        arr = list(map(int, input().split()))
    
        for i in range(E): #두개씩 읽는 작업, E개의 쌍
            v1, v2 = arr[i*2], arr[i*2+1]
            adjL[v1].append(v2)
            adjL[v2].append(v1)
        # print(adjL) #[[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
    
        DFS(1, V)
    ```