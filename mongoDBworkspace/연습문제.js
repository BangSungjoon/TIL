// 연습문제
// 1. 강릉시(county 값) 교차로 내에서 일어난 
// 총 사고 숫자를 출력한다(프로젝션 이용)
use('new_db')
db.by_road_type.find({county: '강릉시'}, {'교차로내.accident_count': 1})

// 2. 전국에서 도로 종류 중에 "기타단일로"에서 사망자수가 0인 지역을 출력한다
use('new_db')
db.by_road_type.find({'기타단일로.death_toll':0},{city_or_province: 1, county: 1})

// 3. 전국의 '차대차' 사고에서 100회 이상 사고가 났지만 사망자 수가 0회인 지역을 출력한다
use('new_db')
db.by_type.find