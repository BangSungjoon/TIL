import requests
import datetime

# API 키를 입력하세요
api_key = 'API_KEY'
# 날씨를 알고 싶은 도시를 입력하세요
city_name = 'Ansan, KR'
# 오늘 날짜와 밤 9시 이후 시간을 계산합니다
today_date = datetime.datetime.now().strftime('%Y-%m-%d')
target_time = '21:00:00'

# API 엔드 포인트
url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units=metric"

# GET 요청을 보냅니다
response = requests.get(url)
data = response.json()

# 오늘 밤 9시 이후의 날씨 정보를 찾습니다
forecasts = []
for entry in data['list']:
    if entry['dt_txt'].startswith(today_date) and entry['dt_txt'].endswith(target_time):
        forecasts.append(entry)

if forecasts:
    for forecast in forecasts:
        print(f"안산의 {forecast['dt_txt']} 날씨:")
        print(f"온도: {forecast['main']['temp']}°C")
        print(f"날씨: {forecast['weather'][0]['description']}")
else:
    print("오늘 밤 9시 이후의 날씨 정보를 찾을 수 없습니다.")

