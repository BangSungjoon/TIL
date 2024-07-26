import requests
from pprint import pprint

# 문제4. C번의 데이터를 활용하여, 섭씨 온도 데이터를 추가합니다.

def get_weather(api_key):
    city = "Seoul,KR"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    # 요구사항에 맞도록 이곳의 코드를 수정합니다.
    response = requests.get(url).json()
    temp_c = round(response['main']['temp'] - 273.15, 2)
    feels_like_c = round(response['main']['feels_like'] - 273.15, 2)
    temp_max_c = round(response['main']['temp_max']- 273.15, 2)
    temp_min_c = round(response['main']['temp_min']-273.15, 2)
    result = {
        '기본' : {'기압': response['main']['pressure'],
                '습도' : response['main']['humidity'],
                '온도': response['main']['temp'],
                '온도 (섭씨)': temp_c,
                '체감온도': response['main']['feels_like'],
                '체감온도 (섭씨)': feels_like_c,
                '최고온도': response['main']['temp_max'],
                '최고온도 (섭씨)': temp_max_c,
                '최저온도': response['main']['temp_min'],
                '최저온도 (섭씨)': temp_min_c,},
                '날씨' : [{'식별자': response['weather'][0]['id'], '아이콘': response['weather'][0]['icon'], '요약': response['weather'][0]['description'], '핵심': response['weather'][0]['main']}]}

    return result



# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # 여러분의 OpenWeatherMap API 키를 설정하세요
    api_key = 'API_KEY'

    result = get_weather(api_key)
    pprint(result)
