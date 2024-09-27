# 관통 PJT (Django에서 DataScience활용)

## Django에서 [Data Science](https://www.notion.so/PJT-4eb7a468c5ca452caa17748f79cb308f?pvs=21) 활용하기

<aside>
💡

Matplotlib, Pandas, Numpy를 Django에서 구동함

</aside>

### 필수 라이브러리

- 가상환경을 설정하여 아래 라이브러리 설치 후 요구사항을 구현합니다.
    - Django 4.2 +
    - Pandas
    - Numpy
    - Matplotlib

### View에서 Template으로 이미지 전달하기

- View에서 Template으로 이미지 형식의 데이터를 직접 전달할 수 없다.
- 저장된 이미지의 경로를 전달하여 Template에서 출력해야 한다.
- matplotlib의 그래프를 버퍼에 이미지 형식으로 저장 후 저장된 경로를 전달한다.
    - 버퍼(buffer): 임시로 데이터를 저장하는 공간
- Python “BytesIO” 클래스
    - 파이썬의 내장 모듈인 “io” 모듈에 포함된 클래스
    - 메모리 내에 데이터를 저장 및 조작할 수 있는 기능 제공

```python
# firsts/views.py

import matplotlib.pyplot as plt
# io: 입출력 연산을 위한 Python 표준 라이브러리
# BytesIO: 메모리 내에서 이진 데이터를 파일처럼 다룰 수 있는 버퍼를 제공함
from io import BytesIO

# 텍스트 <-> 이진 데이터 변환할 수 있는 모듈
import base64

# [참고 터미널 에러]
# Starting a Matplotlib GUI outside of the main thread will likely fail.
# plt 생성과 실제 화면을 그리는 곳이 서로 다른 곳에서 동작하여
# 오류가 날 수 있다는 경고문
# 백엔드를 Agg 로 설정하여 해결할 수 있다.
# - Agg 설정: GUI 없이 서버 환경에서 그래프를 생성하겠다.
plt.switch_backend('Agg')

def index(request):
    x = [1, 2, 3, 4, 5]
    y = [1, 2, 3, 4, 5]

    plt.clf()  # 그래프 초기화

    plt.plot(x, y)  # 그래프 그리기
    plt.title('Test Graph')
    plt.ylabel('y label')
    plt.xlabel('x label')

    # 1. 비어있는 버퍼 생성
    buffer = BytesIO()

    # 2. 버퍼에 그래프를 저장
    plt.savefig(buffer, format='png')

    # 3. 버퍼의 내용을 base64 를 활용하여 인코딩
    # - 이미지 데이터(경로를 포함하고 있다.)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    # 1. 그려진 객체를 반환받아서 넘기는 방법 -> X
    # 2. 이미지로 저장하기 -> 간단하지만, 용량이 감당 X
    # 3. 버퍼(임시 저장 공간)를 활용
    context = {
        # 저장된 이미지의 경로를 전달
        'chart_image': f'data:image/png;base64,{image_base64}'
    }
    return render(request, "firsts/index.html", context)
```

```html
<!-- test.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
    <h1>메인 페이지</h1>
    <img src="{{ chart_image }}" alt="이미지 없음">
</body>
</html>
```

## DB를 활용한 웹 페이지 구현

```python
# firsts/views.py
from django.shortcuts import render
from .models import Weather
import pandas as pd

def example(request):
    # 1. csv 파일을 읽기(pandas)
    csv_path = 'firsts/data/test_data.csv'
    df = pd.read_csv(csv_path)

    # 2. DB에 저장(복습용이다!!!)
    #  - 필드를 데이터를 보고 생성하는 연습
    #  - DB 관련 로직을 구현하는 연습
    #  - 중복된 데이터는 저장하지 않도록 구성
    for index, row in df.iterrows():
        # 저장하는 로직을 바로 구현 -> 중복 저장
        # 이미 해당 날짜에 데이터가 저장되어 있는가 ?
        # 왜 하필 날짜 데이터일까? : 유일하게 구분가능한 필드
        if Weather.objects.filter(date=row['Date']).exists():
            continue

        weather = Weather(
            date=row['Date'],
            temp_avg_f=row['TempAvgF'],
            # Events 필드는 결측치를 포함
            # - 결측치 포함 필드는 아래처럼 여러 조건을 활용
            events=row['Events'] if pd.notna(row['Events']) else ""
        )
        weather.save()

    weathers = Weather.objects.all()
    context = {
        'weathers': weathers
    }
    return render(request, 'firsts/example.html', context)
```

```html
<!-- example.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
    {% for weather in weathers %}
      <p>{{ weather.date|date:"Y-m-d" }} / {{ weather.temp_avg_f }} / {{ weather.events }}</p>
      <hr>
    {% endfor %}
</body>
</html>

```