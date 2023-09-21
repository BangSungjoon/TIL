# 날짜 및 시간 계산
from datetime import date, datetime, timedelta
today = date.today()

print('오늘 : ', today)
print('어제 : ', today + timedelta(days=-1))
print('내일 : ', today + timedelta(days=1))

print('일주일 전 : ', today + timedelta(days=-7))
print('일주일 후 : ', today + timedelta(days=7))

# (2) 시간 계산
current_time = datetime.now()
print('현재 시간 : ', current_time)
print('현재 시간 : ', current_time +timedelta(hours=-1))

# 날짜와 시간 동시 계산
print('1일 2시간 후 : ', current_time + timedelta(days=1, hours=2))

# strftime() 함수 : 날짜 형식을 문자열로 변환
today = datetime.today()

print(today)
# 대문자 Y : 4자리
# 소문자 y : 2자리
# H : 24시간제
# I : 12시간제
# p : AM PM
print(today.strftime('%Y-%m-%d %H:%M:%S'))
print(today.strftime('%y-%m-%d %I:%M:%S %p'))

# strptime() 함수 : 문자열을 날짜 형식으로 반환
str_date = '2023-09-06 14:55:20'
print(type(str_date))

date = datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S')
print(date)
print(type(date))