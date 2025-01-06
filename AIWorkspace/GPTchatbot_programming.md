# ChatGPT 챗봇 programming

2024-07-10 SSAFY StartCamp 3일차

## API

Application Programming Interface
두 소프트웨어가 서로 통신할 수 있게 하는 
메커니즘
요청이 왔을 때, 응답을 한다

- 예시 1 - 소셜 로그인
- 예시 2 - 날씨 데이터 받기

## Interface

사용자가 기기를 쉽게 동작 시키는 데 도움을 주는 시스템

모니터, 키보드도 포함 될 수 있다.

## UI

user interface 사용자와 소프트웨어 간의 상호 작용 시스템

## GPT API를 이용하여 chatbot 만들기

seed : 같은 질문이면, 난수 값을 고정하여 AI가 항상 똑같은 답변만 한다.<br>
temperature : 다음 토큰 예측을 위한 확률 분포를 부드럽게 하는 역할(0에서 2 사이의 값을 가지며, 1.0 이상일 경우 확률 분포가 평탄해지며 더 창의적이고 예측할 수 없는 결과를 생성)<br>
top_p: 누적 확률을 기준으로 선택할 토큰의 범위를 제한 (0에서 1 사이의 값을 가지며, 1에 가까울수록 모델은 더 다양한 토큰을 고려)

```python
from openai import OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

# 페르소나 지정 및 기존 대화 내용 저장
conversation_history = [
    {"role": "system", "content": "당신은 사용자 질문에 답변하는 챗봇입니다."},
    {"role": "system", "content": "답변은 사용자가 읽기 쉽도록 마크다운 형태로 정리해서 출력해줘."},
]
# 질문
conversation_history.append(
    {
        "role": "user",
        "content": "오늘 달달하고 매콤한 것을 먹고 싶은데, 점심 메뉴 추천해줄래?",
    }
)

# API 호출
response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # 사용하려는 모델 (필수 지정)
    messages=conversation_history,  # 대화 메시지 목록 (필수 지정)
    max_tokens=500,  # 생성될 응답의 최대 토큰 수 (값의 범위: 1~모델 마다 최대값 ex> gpt-3.5-turbo: 16,385 tokens)
    temperature=1.0,  # 확률 분포 조정을 통한 응답의 다양성 제어 (값의 범위: 0~2)
    top_p=1.0,  # 누적 확률 값을 통한 응답의 다양성 제어 (값의 범위: 0~1)
    n=1,  # 생성할 응답 수 (1이상의 값)
    seed=1000 # 랜덤 씨드 값
)
# 응답 출력
for response in response.choices :
  print(f"Assistant: {response.message.content}")
```

```python
from openai import OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

conversation_history = [
{"role": "system",
"content":
'''
<페르소나>
# 역할
- 당신의 이름은 '김사피'입니다.
- 당신은 과학적인 질문에 재치 있게 답하는 천재 물리학자의 역할을 수행해야 합니다.

# 성격
- 유머러스하고 기발한, 때로는 약간 엉뚱한 느낌을 주어야 합니다.
- 지식이 풍부하며 설명할 때 친근하게 다가갑니다.

# 말투
- 매우 유머스럽고 친근한 느낌을 포함해야 합니다.
- 과학적인 설명을 할 때도 유머를 잃지 않고, 간단하고 이해하기 쉽게 설명합니다.
- 말투 예시: "내 이름은 김사피라네! 우주의 신비를 푸는 건 내 취미지! 뭐든 물어보게나, 내 해답은 항상 준비되어 있네!"
- 말투 예시: "그 질문은 마치 사과가 왜 땅으로 떨어지냐고 묻는 것과 같군! 자, 한 번 재미있게 풀어보자고!"
</페르소나>

<GPT 지침>
-당신은 위에서 정한 페르소나 인물입니다.
-사용자의 질문에 위에서 정한 말투와 지침을 준수하여 응답해야 합니다.
 <GPT 지침/>
 '''
}]

# '종료' 입력 전까지 대화
user_input = ''
while True:
    user_input = input("You: ")
    if "종료" in user_input : break
    conversation_history.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation_history,
        temperature=1.2,  # 확률 분포 조정을 통한 응답의 다양성 제어 (값의 범위: 0~2)
        top_p=0.6,  # 누적 확률 값을 통한 응답의 다양성 제어 (값의 범위: 0~1)
        max_tokens=500,# 생성될 응답의 최대 토큰 수,
    )

    assistant_reply = response.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": assistant_reply})

    print(f"Assistant: {assistant_reply}")
```

[파이썬트랙_GPT_API실습_기초[학생용].ipynb](GPT_API_practice.ipynb)