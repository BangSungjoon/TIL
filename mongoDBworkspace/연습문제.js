use('new_db')

// 1. 강릉시(county 값) 교차로 내에서 일어난 총 사고 숫자를 출력한다(프로젝션 이용)
db.by_road_type.find({county:"강릉시"}, {"교차로내.accident_count":1})
// 사고건수 : 375
// 375만 출력
// (1) findOne() 사용 : 반환값 1개
use('new_db')
db.by_road_type.findOne({county:"강릉시"}, {"교차로내.accident_count":1}).교차로내.accident_count
// (2) find() 사용 : 배열 반환 (반복문 사용해서 추출)
use('new_db')
let accident = db.by_road_type.find({county:"강릉시"});
accident.forEach(accident => {
    console.log(accident.교차로내.accident_count);
});

// 2. 전국에서 도로 종류 중에 "기타단일로"에서 사망자수가 0인 지역을 출력한다
db.by_road_type.find({"기타단일로.death_toll":0},{city_or_province:1,county:1})

// 3. 전국의 '차대차' 사고에서 100회 이상 사고가 났지만 사망자 수가 0회인 지역을 출력한다
db.by_type.find({"type":"차대차", "accident_count":{$gte:100}, death_toll:0},{city_or_province:1,county:1})

// 4. 전국의 '차대사람' 사고 중에서 사망자수가 0회이거나 중상자수가 0회인 지역을 출력한다
db.by_type.find({"type":"차대사람", 
    $or :
    [ 
        {death_toll:0},
        {heavy_injury:0}
    ] },{city_or_province:1, county:1})
db.by_type.find()

// 5. 2차 지역명(county)이 시라는 이름으로 끝나는 지역의 수 출력
db.area.find({county:/시$/}).count()

// 6. 2차 지역명이 군이면서 인구수가 10만 이상인 곳 출력
db.area.find({county:/군$/, population: {$gte:100000}})

// 7.  2차 지역명이 구로 끝나면서, 이름의 첫 글자의 초성이 "ㅇ"인 2차 지역명 출력
db.area.find({county:/군$/,county : {$gte:"아", $lt:"자"}},{county:1})

// 8. 서울시에서 한달에 200회 이상 교통사고가 일어난 적이 있는 지역을 출력한다
db.by_month.find({city_or_province:"서울", "month_data.accident_count":{$gte:200}},{county:1})

// 9. 1월에 중상자 수가 0명이고, 2월에 사망자 수가 0명인 지역을 출력한다
db.by_month.find({
    $and :[
        {month_data : {$elemMatch: {month:"01월", heavy_injury:0}}},
        {month_data : {$elemMatch: {month:"02월", death_toll:0}}},
    ]
},{county:1})

// 10. 전국에서 도로 종류 중에 "기타단일로"에서 사망자수가 0인 도큐먼트 출력. 
// 단 해당 지역의 지역명과 관련된 필드와 "기타단일로"의 사망자수 필드, _id 필드만 출력)
db.by_road_type.find({"기타단일로.death_toll":0},{_id:1,city_or_province:1,county:1, "기타단일로.death_toll":1})

// 11. 다음 조건을 만족하는 도큐먼트 출력
// - 2차 지역명이 구로 끝나는 도큐먼트
// - 동시에 2차 지역명의 첫 글자 초성이 "ㅇ"인 도큐먼트
// - 찾은 도큐먼트에서 1,2차 지역명과 _id 필드, 매월 사고 횟수가 150회 이상인 달의 이름(month 필드) 출력
db.by_month.find({
    $and: [
        { county: { $regex: /구$/ } },
        { county: { $gte: "아" } },
        { county: { $lt: "자" } },
        { month_data: { $elemMatch: { accident_count: { $gte: 150 } } } }
    ]
},
{
    city_or_province: 1,
    county: 1,
    "month_data.month": 1
})

// 12. 다음 조건을 만족하는 도큐먼트 출력
// - 서울시에서 한달에 200회 이상 사고가 일어난 적이 있는 도큐먼트 출력
// - 단, 200회 이상 사고가 난 달의 정보가 도큐먼트에 한달치만 출력되어야 함
// - 또한 "month_data" 필드와 2차 지역명 관련 필드, _id 필드만 도큐먼트에 표시
db.by_month.find({"city_or_province":"서울", "month_data.accident_count": {$gte : 200}},{"month_data.$":true,county:1})