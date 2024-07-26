# 02_PJT

## 목표
- 캐글을 활용하여 데이터를 다운로드 받기
  - [넷플릭스 주식 가격 데이터](https://www.kaggle.com/datasets/jainilcoder/netflix-stock-price-prediction)
  - 2018-02-05 ~ 2022-02-04 까지의 일별 데이터
- 데이터 전처리
- 데이터 분석 / 시각화
- 생성형 AI를 활용하여 주가 예측하기

## 학습한 내용
### 데이터 사이언스
- 다양한 데이터로부터 새로운 지식과 정보를 추출하기 위해 과학적 방법론, 프로세스, 알고리즘, 시스템을 동원하는 융합 분야
- 컴퓨터 과학, 통계학, 수학 등 다양한 학문의 원리와 기술을 활용
### Jupyter notebook이란?
- 데이터 사이언스 작업에 많이 활용되는 파이썬 개발 환경
- 웹 브라우저에서 실행
- 코드 실행, 텍스트 문서 작성, 시각화 등을 하나의 문서에 통합하여 작업 가능
- 데이터 사이언스 작업에 많이 쓰이는 이유
  - 셀 단위 코드 실행으로 결과를 바로 확인할 수 있다.
  - 문서를 작성할 수 있는 마크다운 기능을 제공한다.
  - 개별적인 코드 블록을 실행할 수 있다.
### CSV란?
- 몇 가지 필드를 쉼표(,)로 구분한 텍스트 데이터 및 텍스트 파일
- 일반적으로 표 형식의 데이터를 CSV 형태로 많이 사용
- 저장, 전송 및 처리 속도가 빠르며, 처리 가능한 프로그램이 다양하다.
### 데이터 전처리
데이터 전처리 단계를 분석을 진행하기 전 데이터를 정제하는 단계
- 불완전하거나 오류가 있는 데이터를 제거하여 데이터의 품질을 개선
- 중복 데이터 제거
- 분석하기 적절한 형식으로 데이터를 변환
> Numpy
>- 다차원 배열을 쉽게 처리하고 효율적으로 사용할 수 있도록 지원하는 파이썬 패키지
>- 장점
>  - Numpy 행렬 연산은 데이터가 많을수록 Python 반복문에 비해 훨씬 빠르다.
>  - 다차원 행렬 자료 구조를 제공하여 개발하기 편하다.
>- 특징
>  - CPython(공식 사이트의 Python)에서만 사용 가능
>  - 행렬 인덱싱(Array Indexing) 기능 제공 <br>
 
> Pandas
>- Numpy의 한계
>   - 유연성(데이터에 레이블을 붙이거나, 누락된 데이터로 작업)이 부족함
>   - 그룹화, 피벗 등 구조화가 부족함
>- Pandas는 마치 프로그래밍 버전의 엑셀을 다루듯 고성능의 데이터 구조를 만들 수 있음
>- Numpy 기반으로 만들어진 패키지로, <br>Series(1차원 배열)과 DataFrame(2차원 배열)이라는 효율적인 자료구조 제공

> Matplotlib
>- Python에서 데이터 시각화를 위해 가장 널리 사용되는 라이브러리
>- 다양한 종류의 그래프와 도표를 생성하고 데이터를 시각적으로 표현할 수 있다.

## 해결
데이터 전처리를 오랜만에 만났다. <BR>Numpy와 Pandas, Matplotlib은 정말 질리도록 했었는데 기억이 가물가물해서 당황스러웠다.<BR> 검색을 열심히 해보며 메서드를 찾아 사용했고 여전히 메서드 사용법을 전부 외우고 있지는 않지만 사용하는데 익숙해 질 수 있었다.<br>또한 전에 데이터 분석을 공부 할 때는 파이썬 데이터 구조를 잘 모르기에 단순 암기였다면, 이제는 데이터 형식과 구조를 알고있어서 공식 문서를 읽을 때도 이해가 쉬웠다. <br>잊은 것도 있지만 성장한 점도 보이는 PJT였다.
### A. 데이터 전처리–데이터 읽어오기
```python
def file_open_by_numpy():
    # np.loadtxt(구분자 = ',', 데이터 타입: string)
    np_arr = np.loadtxt('archive/NFLX.CSV', delimiter=",", encoding='cp949', dtype=str)
    return np_arr

arr = file_open_by_numpy()

column = arr[0]
arr = np.delete(arr, 0, 0)
df = pd.DataFrame(arr, columns=column)[['Date','Open', 'High', 'Low', 'Close']]
df
```
데이터 읽어오는 과정부터 기억이 안나, 수업시간에 실행한 코드를 참고했다. <BR>원하는 필드만 읽어오도록 구성할 땐 꼭 대괄호 [[]] 두개를 쓰는 것을 잊지말자!
### B. 데이터 전처리–2021년 이후의 종가 데이터 출력하기
```python
# 데이터 프레임 구성하기
df2 = pd.read_csv('archive/NFLX.csv')
df2 = df2[['Date','Open', 'High', 'Low', 'Close']].copy()
```
`df2['Date'] = pd.to_datetime(df2['Date'])` 날짜를 필터링이 가능하게 datetime 형식으로 바꿔 진행했다. <br>
```python
# 2021년 이후의 데이터만 필터링
df2 = df2.loc[df2['Date']>='2021-01-01']

# 필터링이 완료된 DataFrame의 종가 데이터를 Matplotlib를 사용하여 시각화
# 데이터 생성
x = df2['Date']  # x 좌표값
y = df2['Close']  # y 좌표값

# 그래프 그리기
plt.plot(x, y)

# 그래프에 제목과 축 레이블 추가
plt.title('NFLX Close Price')
plt.xlabel('Date')
plt.ylabel('Close Price')

# 그래프 표시
plt.show()
```
데이터 필터링이 필요할 땐 그에 맞는 데이터 형식으로 바꿔주는 걸 잊지말자!
###  C. 데이터 분석 –2021년 이후 최고, 최저 종가 출력하기
```python
# 데이터 읽어와 필터링 하기
df3 = pd.read_csv('archive/NFLX.csv')
df3 = df3[['Date','Open', 'High', 'Low', 'Close']].copy()
df3['Date'] = pd.to_datetime(df3['Date'])
df3 = df3.loc[df3['Date']>='2021-01-01']

max_price = df3['Close'].max()
min_price = df3['Close'].min()
print('최고 종가:', max_price)
print('최저 종가:', min_price)
```
pandas의 슬라이싱과 여러 매서드를 공부해볼 수 있는 문제였다.

### D. 데이터 분석 -2021년 이후 월 별 평균 종가 출력하기
```python
# 데이터 읽어와 2021년 이후의 데이터만 필터링 하기
df4 = pd.read_csv('archive/NFLX.csv')
df4 = df4[['Date','Open', 'High', 'Low', 'Close']].copy()
df4['Date'] = pd.to_datetime(df4['Date'])
df4 = df4.loc[df4['Date']>='2021-01-01']

# 월별로 그룹화한 뒤 평균값을 매긴다.
df4['YearMonth'] = df4['Date'].dt.to_period('M')
monthly_avg_close = df4.groupby('YearMonth')['Close'].mean().reset_index()

# 데이터 생성
x = monthly_avg_close['YearMonth'].astype(str)  # x 좌표값
y = monthly_avg_close['Close']  # y 좌표값

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(x, y)

# 그래프에 제목과 축 레이블 추가
plt.title('Monthly Average Close Price')
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.ylabel('Average Close Price')

# 그래프 표시
plt.show()
```
월별로 그룹화하기가 어려웠던 문제이다. 그룹화에 대해 이해가 부족한 것 같아 향후 추가 공부가 필요하다.

### E. 데이터 시각화 –2022년 이후 최고, 최저, 종가 시각화하기
```python
# 데이터 읽어와 2022년 이후의 데이터만 필터링 하기
df5 = pd.read_csv('archive/NFLX.csv')
df5 = df5[['Date', 'High', 'Low', 'Close']].copy()
df5['Date'] = pd.to_datetime(df4['Date'])
df5 = df5.loc[df5['Date']>='2022-01-01']

# 데이터 생성
x = df5['Date'] # x 좌표값
y = df5['High']  # y 좌표값
y2 = df5['Low'] # y2 좌표값
y3 = df5['Close'] # y3 좌표값

# 그래프 그리기
plt.plot(x, y, label='High')
plt.plot(x, y2, label='Low')
plt.plot(x, y3, label='Close')

# 범례 추가
plt.legend()

# 그래프에 제목과 축 레이블 추가
plt.title('High, Low, and Close Prices since january 2022')
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.ylabel('Price')

# 그래프 표시
plt.show()
```
그래프에 여러 줄을 그려보는게 중요한 문제. 그냥 plt.plot을 늘리면 된다!
