# 완전 탐색 / 탐욕 알고리즘

## 부분 집합

<aside>
💡

집합에 포함된 원소들을 선택하는 것이다.

</aside>

### 예시

- 오른쪽 표는 집합 {A, B, C}로 만들 수 있는 부분집합의 예시이다.
- 부분집합에는 아무것도 선택하지 않은 경우도 집합에 포함된다. (= 공집합)

| {A, B, C} |
| --- |
| {} |
| {A} |
| {B} |
| {A, B} |
| {C} |
| {A, C} |
| {B, C} |
| {A, B, C} |

### 집합에서 부분 집합을 찾아내는 구현 방법

1. 완전탐색
    - 재귀 호출을 이용한 완전 탐색으로, 부분 집합을 구할 수 있다.
    - 실전 보다는 완전 탐색 학습용으로 추천하는 방법
2. Binary Counting
    - 2진수 & 비트연산을 이용하여, 부분 집합을 구할 수 있다.
    - 부분 집합이 필요할 때 사용하는 추천 방법

### 완전 탐색으로 부분 집합 구하기

민철이에게는 세 명의 친구가 있다. {MIN, CO, TIM}
함께 영화관에 갈 수 있는 멤버를 구성 하고자 한다. 모든 경우를 출력해보자.

- O, X로 집합에 포함 시킬지 말지 결정하는 완전 탐색을 이용하여 구현한다.
- 구현 방법
    - Branch : 2개
    - Level : 3개
    
    ```python
    arr = ['O', 'X']
    path = []
    name = ['MIN', 'CO', 'TIM']
    
    def print_name():
    	print('{ ', end = '')
    	for i in range(3):
    		if path[i] == 'O':
    			print(name[i], end=' ')
    	print('}')
    
    def run(lev):             # lev번째 요소
    	if lev == 3:            # 원소 3개를 모두 고려함
    		print_name()
    		return
    		
    	for i in range(2):      # 후보군 (데려갈지 말지)
    		path.append(arr[i])   # 경로 추가
    		run(lev + 1)          # 다음 lev을 고려해라
    		path.pop()            # 경로 삭제
    
    run(0)
    ```
    

### 바이너리 카운팅(Binary Countion)

- 원소 수에 해당하는 N개의 비트열을 이용한다.
- 0 0 1 이면 {A} 임을 나타냄
- 1 1 0 이면 {B, C} 임을 나타냄
- 집합의 총 개수
    - 만들 수 있는 집합의 총 개수는 2^n이며 n=3이기에, 총 8개 집합이다.
    - $2^n$은 1 << n 공식을 이용하여 빠르게 구할 수 있음.
    
    ```python
    print(pow(2, 3))   # 8
    print(1 << 3)      # 8
    ```
    
- 0b110 이 주어지면, BC 출력하는 함수
    - 6 (0b110)에서 비트 연산을 이용하여 마지막 한 자리가 1인지 0인지 검사한다.
    - 검사한 한 자리를 제거한다. (tar >>= 1)
    
    ```python
    arr = ['A', 'B', 'C']
    n = len(arr)
    
    def get_sub(tar):
    	for i in range(n):
    		if tar & 0x1:
    			print(arr[i], end=' ')
    		tar >>= 1
    
    get_sub(6)  # A B
    ```
    

### [도전] 친구와 카페 방문

민철이는 친구 {A, B, C, D, E}가 있다.

이 중 최소 2명 이상의 친구를 선정하여 함께 카페에 가려고 한다.

총 몇 가지가 경우가 가능할까?

```python
arr = ['A', 'B', 'C', 'D', 'E']
n = len(arr)

# 총 몇개의 bit가 1로 되어있는지 확인하는 함수
def get_count(tar):
    cnt = 0     # 1의 개수
    for i in range(n):
        if tar & 0x1:
            cnt += 1
        tar >>= 1
    return cnt

result = 0
for tar in range(0, 1 << n):    # range(0, 8)
    if get_count(tar) >= 2:
        result += 1
print(result)
```

## 조합

서로 다른 n개의 원소 중 r개를 순서 없이 골라낸 것을 조합(combination)이라고 부른다.

### 순열과 조합 차이

- 순열 : {A, B, C, D, E} 5명 중 1등, 2등, 3등 뽑기
    - A B C 와 C B A 는 다른 경우이다.
- 조합 : 5명 중 3명 뽑기
    - A B C 와 C B A 는 같은 경우이다.

### [도전] {A, B, C, D, E} 5명 중 3명을 뽑을 수 있는 모든 경우를 메모장에 적어보자.

- 힌트 : ABC ~ CDE
- 메모장에 모든 경우를 적으면서, 규칙을 찾아 내보자.
    - k개를 찾을 때까지 후보군이 하나씩 감소한다.
- For문으로 조합 구현하기
    - 5명중 3명 뽑는 조합은 3중 for문으로 구현이 가능하다.
    
    ```python
    arr = ['A', 'B', 'C', 'D', 'E']
    
    for a in range(5):
    	start1 = a + 1
    	for b in range(start1, 5):
    		start2 = b + 1
    			for c in range(start2, 5):
    				print(arr[a], arr[b], arr[c])
    ```
    
- 만약 5명 중 n명을 뽑는 코드는 몇 중 for문이 필요할까?
    - n중 for문으로 구현이 가능하다. 즉, 재귀 호출 구현이 필요
    - Branch : 최대 5개
    - Level : n
    
    ```python
    arr = ['A', 'B', 'C', 'D', 'E']
    path = []
    
    n = 3
    def run(lev, start):
    	if lev == n:
    		print(path)
    		return
    	
    	for i in range(start, 5):
    		path.append(arr[i])
    		run(lev + 1, i + 1)
    		path.pop()
    
    run(lev:0, start:0)
    ```
    

### [도전] 주사위 던지기

주사위 눈금 N개를 던져서 나올 수 있는 모든 조합을 출력하시오.

N = 3  일때 출력 결과

```python
path = []

n = 3

def run(lev, start):
    if lev == n:
        print(path)
        return

    for i in range(start, 7):
        path.append(i)
        run(lev + 1, i)
        path.pop()

run(0, 1)
```

## Greedy

### Greedy (욕심장이기법, 알고리즘) 이란?

- 결정이 필요할 때, 현재 기준으로 가장 좋아 보이는 선택지로 결정하여 답을 도출하는 알고리즘
- 탐욕적 선택 조건(Greedy Choice Property) : 각 단계의 선택이 이후 선택에 영향을 주지 않는다.
- 최적 부분 구조(Optimal Substructure) :  각 단계의 최선의 선택이, 전체 문제의 최선의 해가 된다.

### 대표적인 문제 해결 기법

1. 완전 탐색 (Brute-Force)
    - 답이 될 수 있는 모든 경우를 시도해보는 알고리즘
2. Greedy
    - 결정이 필요할 때 가장 좋아 보이는 선택지로 결정하는 알고리즘
3. DP (차후 학습 예정)
    - 현재에서 가장 좋아 보이는 것을 선택하는 것이 아니라, 과거의 데이터를 이용하여, 현재의 데이터를 만들어내는 문제 해결 기법
4. 분할 정복 (차후 학습 예정)
    - 큰 문제를 작은 문제로 나누어 해결하는 문제 해결 기법

### [문제] 동전 교환

1,730원을 거슬러 줄 수 있는 최소 동전의 수

- 큰 동전부터 최대한 거슬러 주면 된다. 이 처럼, 좋아 보이는 값을 먼저 선택하는 것을 그리디(Greedy), 욕심장이 알고리즘이라고 한다.
- 500원 = 3개 = 누적 1,500원
- 100원 = 2개 = 누적 1,700원
- 10원 = 3개 = 누적 1,730원
1. 각 단계에서 최적해를 찾아야 한다.
2. 단계의 결과들을 합하는 방법을 찾아야 한다.
3. 각 단계의 합 == 전체 문제의 합이라는 것을 증명해야 한다.

```python
coin_list = [500, 100, 50, 10]
target = 1730
cnt = 0

for coin in coin_list:
	passible_cnt = target // coin
	
	cnt += possible_cnt
	target -= coin * possible_cnt

print(cnt)
```

### [도전] 화장실 문제

이 문제는 그리디로 풀 경우, 어떤 기준으로 접근해야, 대기 시간의 누적 합이 최소가 될지 고민해보고 직접 구현해보자. (제한시간 : 5분)

### 0-1 Knapsack

도둑은 보물들이 있는 창고에 침입하였다. 도둑은 최대 30KG 까지 짐을 담아갈 수 있다.

물건의 개수(N) 그리고 물건 별 무게(W)와 가격(P)이 주어질 때, 어떤 물건을 담아야, 도둑이 최대 이득을 볼 수 있을지 구하시오.

이 문제는 kg 당 가치가 가장 높은 것을 먼저 담으면 안된다.

- 0-1 Knapsack을 그리디로 접근하면 안되는 예외 케이스가 존재한다.
- 0-1 Knapsack 문제는 그리디로 해결할 수 없다. 완전 탐색 or DP로 접근해야 한다.

### Fractional Knapsack 문제

- 0-1 Knapsack과 달리, 물건을 원하는 만큼 자를 수 있는 Knapsack 문제
- 그리디가 성립한다.
- Kg 당 가격이 가장 높은 물건을 최대한 담으면 된다.
    
    ```python
    n = 3
    targe = 30
    things = [(5, 50), (10, 60), (20, 140)] # (kg, price)
    
    # (price / kg) 기준으로 내림차순 sort
    things.sort(key=lambda x: (x[1] / x[0], reverse=True)
    # sort 결과 = [(5, 50), (20, 140), (10, 60)]
    print(things)
    
    total = 0
    for kg, price in things:
    	per_price = price / kg
    	
    	# 만약 가방에 남은 용량이 얼마되지 않는다면,
    	# 물건을 잘라 가방에 넣고 끝낸다.
    	if target < kg:
    		total += target * per_price
    		break
    		
    	total += price
    	target -= kg
    	
    print(int(total))
    ```