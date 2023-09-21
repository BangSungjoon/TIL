# 날짜 출력
from datetime import date, datetime, timedelta

today = date.today()
year = today.year
month = today. month
day = today.day

print('오늘 날짜 :', today)
print('연도 :', year)
print('월 :', month)
print('일 :', day)

now = datetime.now() # 날짜 시간
print('now : ', now)

current_time = datetime.now().time() # 시간만 출력
print('current_time : ', current_time)

# now() : 연월일 시분초 추출
now = datetime.now() # 날짜 시간
year = now.year
month = now.month
day = now.day

hour = now.hour
minute = now.minute
second = now.second
microsecond = now.microsecond

print('오늘 날짜 :', now)
print('연도 :', year)
print('월 :', month)
print('일 :', day)

print('시 :', hour)
print('분 :', minute)
print('초 :', second)
print('마이크로초 :', microsecond)

# current_time = datetime.now().time()에서 시분초 추출 가능