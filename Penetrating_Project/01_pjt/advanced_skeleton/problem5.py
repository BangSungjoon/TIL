import requests

# API 키와 기본 URL 설정
api_key = 'YOUR_API_KEY'  # 여기에 자신의 API 키를 입력하세요
base_url = 'https://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'

# 요청 파라미터 설정
params = {
    'auth': api_key,
    'topFinGrpNo': '020000',  # 은행
    'pageNo': '1'
}

# API 요청 보내기
response = requests.get(base_url, params=params)

# 응답이 성공적일 때만 JSON 파싱 시도
if response.status_code == 200:
    data = response.json()

    # 국민은행 상품 중 금리가 가장 높은 상품 찾기
    kb_highest_rate_product = None
    highest_rate = 0

    for product in data['result']['baseList']:
        if product['kor_co_nm'] == '국민은행':  # 'fin_co_nm' 대신 'kor_co_nm' 사용
            for option in data['result']['optionList']:
                if option['fin_prdt_cd'] == product['fin_prdt_cd']:
                    rate = float(option['intr_rate2'])
                    if rate > highest_rate:
                        highest_rate = rate
                        kb_highest_rate_product = product['fin_prdt_nm']

    if kb_highest_rate_product:
        print(f"국민은행 상품 중 가장 금리가 높은 상품은 {kb_highest_rate_product}입니다. 사장님.")
    else:
        print("국민은행의 예금 상품을 찾을 수 없습니다.")
else:
    print("API 요청에 실패했습니다. 응답을 확인해주세요.")
