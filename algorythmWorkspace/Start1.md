# Start 1

<aside>
💡 알고리즘 실력을 늘리려면 어떻게 해야 하는가?

</aside>

### SW 문제 해결 역량이란 무엇인가?

- 프로그램을 하기 위한 많은 제약 조건과 요구사항을 이해하고 최선의 방법을 찾아내는 능력
- 프로그래머가 사용하는 언어나 라이브러리, 자료구조, 알고리즘에 대한 지식을 적재적소에 퍼즐을 배치하듯 이들을 연결하여 큰 그림을 만드는 능력이라 할 수 있다.
- 문제 해결 역량은 추상적인 기술이다.
    - 프로그래밍 언어, 알고리즘처럼 명확히 정의된 실체가 없다.
    - 무작정 알고리즘을 암기하고 문제를 풀어본다고 향상되지 않는다.
- 문제 해결 역량을 향상시키기 위해서 훈련이 필요하다.

### 문제 해결 과정

1. 문제를 읽고 이해한다.
2. 문제를 익숙한 용어로 재정의한다.
3. 어떻게 해결할지 계획을 세운다.
4. 계획을 검증한다.
    - 논리적인 허점을 찾자
        - 반례 찾기
        - 복잡도 계산
5. 프로그램으로 구현한다.
6. 어떻게 풀었는지 돌아보고, 개선할 방법이 있는지 찾아본다.

## 복잡도 분석

### 알고리즘?

- (명) 알고리즘 : 유한한 단계를 통해 문제를 해결하기 위한 절차나 방법이다.
주로 컴퓨터 용어로 쓰이며, 컴퓨터가 어떤 일을 수행하기 위한 단계적 방법을 말한다.
- 간단하게 다시 말하면 어떠한 문제를 해결하기 위한 절차라고 볼 수 있다.
- 예를 들어 1부터 100까지의 합을 구하는 문제를 생각해 보자
    - 1부터 100까지 다 더하는 방법
    - $100*(1+100)/2$

### 알고리즘의 효율

- 공간적 효율성과 시간적 효율성
    - 공간적 효율성은 연산량 대비 얼마나 적은 메모리 공간을 요하는 가를 말한다.
    - 시간적 효율성은 연산량 대비 얼마나 적은 시간을 요하는 가를 말한다.
    - 효율성을 뒤집어 표현하면 복잡도(Complexity)가 된다. 복잡도가 높을수록 효율성은 저하된다.

### 복잡도의 점근적 표기

- 시간 (또는 공간)복잡도는 입력 크기에 대한 함수로 표기하는데, 이 함수는 주로 여러개의 항을 가지는 다항식이다.
- 이를 단순한 함수로 표현하기 위해 점근적 표기 (Asymptotic Notation)를 사용한다.
- 입력 크기 n이 무한대로 커질 때의 복잡도를 간단히 표현하기 위해 사용하는 표기법이다.
    - O(Big-Oh) - 표기 → 최대 시간
    - **Ω**(Big-Omega) - 표기 → 최소 시간
    - Θ(Big-Theta) - 표기 → 평균 시간

### O(Big-Oh)-표기

- O-표기는 복잡도의 점근적 상한을 나타낸다.
- 복잡도가 f(n) = $2n^2-7n+4$ 이라면, f(n)의 O-표기는 O($n^2$)이다.
- 먼저 f(n)의 단순화된 표현은 $n^2$이다.
- 단순화된 함수 $n^2$에 임의의 상수 c를 곱한 $cn^2$이 n이 증가함에 따라 f(n)의 상한이 된다.
(단, c>0.)

```python
n = int(input())

for i in range(n):
	print(i, end = '')

for i in range(n):
	print(i, end = '')
	
for i in range(n):
	print(i, end = '')
```

- 빅-O 표기법으로 표현하면?
    - 실제 횟수 : 3N
    - 빅-O 표기법 : O(N)
- 대략적인 지표만 계산 가능!
- 상수 횟수 반복하는 코드는 빅오표기법으로 어떻게 표현할까?
    
    ```python
    n = int(input())
    
    for i in range(50):
    	print(i)
    ```
    
    - O(1)
- 알고리즘 성능을 미세하게 비교하고 싶은 경우
    - 예) 논문 등에서 몇 배 빠른지를 비교하고 싶을 때 N앞에 계수를 붙여주기도 한다.
    - O(5N) 이라고 적곤 한다.
- 무조건 시간 복잡도가 작다고 좋은 알고리즘은 아니다!
- 자주 사용하는 O-표기
    - O(1) 상수 시간
    - O($logn$) 로그 (대수) 시간
    - O(n) 선형 시간
    - O($nlogn$) 로그 선형 시간
    - O($n^2$) 제곱 시간
    - O($n^3$) 세제곱 시간
- 만약 O(log N) 라면?
    - 만약 N이 10,000 이고 O(log N)으로 짠 알고리즘이 있다면, 몇 번 반복하는 프로그램이라고 추정해도 될까?
    - 알고리즘 이론에서 Log의 밑 수는 10이 아니라 2이다.
    따라서, 2의 몇 승이 10,000이 되는지 계산기를 사용해서 알 수 있다.
- O($logN$)은 O(1) 보다는 느리지만, 유사한 성능을 보인다고 결론을 낼 수 있다.
- O($NlogN$)은 O(N) 보다는 느리지만, 유사한 성능을 보인다고 결론을 낼 수 있다.

## 진수

### 2진수, 8진수, 10진수, 16진수

- 10진수 : 사람이 사용하는 진수, 수 하나를 0~9 로 표현
- 2진수 : 컴퓨터가 사용하는 진수, 수 하나를 0, 1로 표현
- 8진수 : 2진수를 더 가독성 있게 사용
- 16진수 : 2진수를 더 가독성 있게 사용, 수 하나를 0, 1, … 8, 9, A, B, C, D, E, F 로 표현

### 왜 16진수를 사용하는 것인가?

- 2진수를 사람이 이해하기 편하도록, 10진수로 변환 시
    - 인간이 이해하기 편하지만, 연산이 오래 걸림
- 2진수를 사람이 이해하기 편하도록 16진수로 변환 시
    - 인간이 이해하기 어렵지만, 연산 속도가 매우 빠름