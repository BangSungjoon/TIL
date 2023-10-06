
// 도시별 총인구수 출력
// 인구수 기준 내림차순 정렬
// 도시 : city_or_province
// 총인구수 : population
// $group, $sum
// $sort, -1

use("new_db")
db.population.aggregate(
    [
        {
            '$group' :
            {
                '_id':{'도시' : '$city_or_province'},
                '총인구수' : {$sum : '$population'}
            }
        },
        {
            '$sort' : {'총인구수' : -1}
        }
    ]
)

// _id 출력 안 되게 : 프로젝션 0 ($project 사용)
use("new_db")
db.population.aggregate(
    [
        {
            '$group' :
            {
                '_id':{'도시' : '$city_or_province'},
                '총인구수' : {$sum : '$population'}
            }
        },
        {
            $project: {'_id': 0 }
        },
        {
            '$sort' : {'총인구수' : -1}
        }
    ]
)

// 도시별 총인구수 출력
// 인구수 기준 내림차순 정렬 : Top5만 출력 ($limit 사용)
// 상위 5개
use("new_db")
db.population.aggregate(
    [
        {
            '$group' :
            {
                '_id':{'도시':'$city_or_province'},
                '총인구수' : {$sum : '$population'}
            }
        },
        {
          '$sort': {'총인구수':-1}
        }
        ,{
          '$limit': 5
        },
    ]
)


// 도시별 총인구수 출력
// 하위 5개 도시 출력 
use("new_db")
db.population.aggregate(
    [
        {
            '$group' :
                {
                    '_id': {'도시': '$city_or_province'},
                    '총인구수' : {$sum: '$population'}
                }
        },
        {
            '$sort' : {'총인구수': 1}
        },
        {
            '$limit': 5
        }
    ]
)

// 도시별로 총인구수를 구한 후 서울 지역만 출력 
// 조건 : city_or_province = '서울'
// $match 사용
use('new_db')
db.population.aggregate(
    [   
        {
            '$match': {city_or_province : '서울'}
        },
        {
            '$group':
            {
                '_id':{'도시':'$city_or_province'},
                '총인구수' : {$sum : '$population'}
            }
        }
    ]
)

// 스테이지 순서를 다르게 했는데 결과가 동일 
use("new_db")
db.population.aggregate([
    {
        '$group':{
            '_id': {'도시': '$city_or_province'},
            '총인구수' : {$sum : '$population'}
        }
    },
    // {'$match': },
    {'$match': {'_id.도시' : '서울'}}
])


// 조검 : 총 인구수가 3,000,000이상인 도시와 총인구수 출력
// 총합 후 3,000,000 이상 추출
use('new_db')
db.population.aggregate(
    [
        {
            '$group':
            {
                '_id':{'도시':'$city_or_province'},
                '총인구수':{$sum: '$population'}
            }
        },
        {
            '$match' : {'총인구수':{$gte:3000000}}
        }
    ]
)

// 주의! 
// 집계 파이프라인 단계 순서에 따라 결과가 달라짐
// 3,000,000 이상을 먼저 추출한 후 총합
// 조건 : 총인구수가 3,000,000 이상인 도시와 총인구수 출력
use("new_db")
db.population.aggregate(
    [
        {
            '$match' : {'population': {'$gte' : 3000000}}
        },
        {
            '$group' :
                {
                    '_id': {'도시': '$city_or_province'},
                    '총인구수' : {$sum: '$population'}
                }
        }
    ]
)

// 서울의 local_government 수 출력
use("new_db")
db.population.aggregate(
    [
        {
            '$match' : {city_or_province : '서울'}
        },
        {
            '$group' :
            {
                '_id': {'도시' : '$city_or_province'},
                'local_government' : {$sum : 1}
            }
        }
    ]
)

use("new_db")
db.population.aggregate(
    [
        {
            '$match' : {city_or_province : '서울'}
        },
        {
            '$group' :
            {
                '_id': '서울',
                'local_government' : {$sum : 1}
            }
        }
    ]
)

use("new_db")
db.population.aggregate(
    [
        {
            '$match' : {city_or_province : '서울'}
        },
        {
            '$group' :
            {
                '_id': '서울',
                'local_government' : {'$count' : {}}}
            }
        
    ]
)

use("new_db")
db.population.aggregate([
    {
        '$match' : { city_or_province : "서울"} 
    },
    {
        '$group' :{
            _id:{'local':'$local_government'}
        }
    },
    {
        '$count' : "count"
    }
])

use("new_db")
db.population.aggregate(
    [    
        {
            '$match' : 
            {
                'city_or_province' : '서울' 
            }
        }
    ]
).toArray().length


use("new_db")
db.population.find({city_or_province:'서울'}).count()


// 인구수 500,000 이상인 local_government 찾아서
// 도시(city_or_province)와 local_government, 평균 인구수 출력
// 10개만 출력
use("new_db")
db.population.aggregate([
    {
        '$match': { population: { $gte: 500000 } }
    },
    {
        '$group': {
            '_id': { '도시': '$city_or_province', 'local_government': '$local_government' },
            '평균인구수': { $avg: '$population' }
        }
    },
    {
        '$limit': 10
    }
])

// 교재 P162
// 2차 지방자치단체의 올해(당해 연도) 시도별 의회비 평균 구하기 
// 내림차순
use("new_db")
db.local.aggregate([
    {
        '$match': { 'sub_category': "의회비"}
    },
    {
        '$group': {
            '_id':'$city_or_province',
            '의회비 평균': { $avg: '$this_term_expense' }
        }
    },
    {
        '$sort': {'의회비 평균':-1}
    }
])