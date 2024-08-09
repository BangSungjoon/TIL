# Stack 4

## 백트래킹

### 부분 집합

<aside>
💡 어떤 집합의 공집합과 자기 자신을 포함한 모든 부분 집합을 powerset이라고 하며 구하고자 하는 어떤 집합의 원소 개수가 n일 경우 부분 집합의 개수는 2^n개 이다.

</aside>

- 백트래킹 기법으로 powerset을 만들어 보자.
    - 앞에서 설명한 일반적인 백트래킹 접근 방법을 이용한다.
    - n개의 원소가 들어있는 집합의 2^n개의 부분 집합을 만들 때는, true 또는 false값을 가지는 항목들로 구성된 n개의 배열을 만드는 방법을 이용.
    - 여기서 배열의 i번째 항목은 i번째의 원소가 부분 집합의 값인지 아닌지를 나타내는 값이다.
- 각 원소가 부분 집합에 포함 되었는지를 loop를 이용하여 확인하고 부분 집합을 생성하는 방법
    
    ```python
    bit = [0, 0, 0, 0]
    for i in range(2):
    	bit[0] = i
    	for j in range(2):
    		bit[1] = j
    		for k in range(2):
    			bit[2] = k
    			for I in range(2):
    				bit[3] = I
    				print(bit)
    ```
    
- powerset(멱집합: 모든 부분 집합의 집합)을 구하는 백트래킹 알고리즘
    
    ```python
    def backtrack(a, k, n):  # a 주어진 배열, k 결정할 원소, n 원소 개수
        c = [0] * MAXCANDIDATES  # camdodates 후보자
    
        if k == n:
            process_solution(a, k)  # 원하는 답이면 작업을 한다.
        else:
            ncandidates = construct_candidates(a, k, n, c)
            for i in range(ncandidates):
                a[k] = c[i]
                backtrack(a, k + 1, n)
    
    def construct_candidates(a, k, n, c):
        c[0] = True
        c[1] = False
        return 2
    
    def process_solution(a, k):
        for i in range(k):
            if a[i]:
                print(num[i], end=' ')
        print()
    
    MAXCANDIDATES = 2
    NMAX = 4
    a = [0] * NMAX
    num = [1, 2, 3, 4]
    backtrack(a, 0, NMAX)
    ```
    

### 순열

- 단순하게 순열을 생성하는 방법
    - 집합 {1, 2, 3}에서 모든 순열을 생성하는 함수
    - 동일한 숫자가 포함되지 않았을 때, 각 자리수 별로 loop을 이용해 아래와 같이 구현할 수 있다.
    
    ```python
    for i1 in range(1, 4):
    	for i2 in range(1, 4):
    		if i2 != i1:
    			for i3 in range(1, 4):
    				if i3 != i1 and i3 != i2:
    					print(i1, i2, i3)
    ```
    
- 백트래킹을 이용하여 {1, 2, 3, …, NMAX}에 대한 순열 구하기
    - 접근 방법은 앞의 부분 집합 구하는 방법과 유사하다.
    
    ```python
    def backtrack(a, k, n):
        c = [0] * MAXCANDIDATES
    
        if k == n:
            for i in range(0, k):
                print(a[i], end=" ")
            print()
        else:
            ncandidates = construct_candidates(a, k, n, c)
            for i in range(ncandidates):
                a[k] = c[i]
                backtrack(a, k + 1, n)
    
    def construct_candidates(a, k, n, c):
        in_perm = [False] * (NMAX + 1)
    
        for i in range(k):
            in_perm[a[i]] = True
    
        ncandidates = 0
        for i in range(1, NMAX + 1):
            if in_perm[i] == False:
                c[ncandidates] = i
                ncandidates += 1
        return ncandidates
    
    MAXCANDIDATES = 3
    NMAX = 3
    a = [0]*NMAX
    backtrack(a, 0, 3)
    ```
    

## 가지치기

### [참고] 부분 집합의 합

- i원소의 포함 여부를 결정 하면 i까지의 부분 집합의 합 Si를 결정할 수 있음
- Si-1이 찾고자 하는 부분 집합의 합보다 크면 남은 원소를 고려할 필요가 없음
- 남은 원소의 합을 다 더해도 찾는 값 T 미만인 경우 중단
    
    ```python
    def f(i, k, s, t):  # i원소, k 집합의 크기, s i-1까지 고려된 합, t 목표
        global cnt
        global fcnt
        fcnt += 1
        if s > t:       # 고려한 원소의 합이 찾는 합보다 큰 경우
            return
        elif s == t:    # 남은 원소를 고려할 필요가 없는 경우
            cnt += 1
            return
        elif i == k:    # 모든 원소 고려
            return
        else:
            bit[i] = 1
            f(i + 1, k, s + A[i], t)    # A[i] 포함
            bit[i] = 0
            f(i + 1, k, s, t)           # A[i] 미포함
    
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    N = 10
    # A = [ i for i in range(1, N+1)]
    
    key = 10
    cnt = 0             # 합이 key와 같은 부분집합의 수
    bit = [0]*N
    fcnt = 0
    f(0, N, 0, key)
    print(cnt, fcnt)
    ```
    

### [참고] 순열

## 분할 정복