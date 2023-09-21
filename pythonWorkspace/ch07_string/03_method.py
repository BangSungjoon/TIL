# 문자열 관련 메소드

string = 'programming'

# len() : 문자열 길이 반환 함수
print(len(string))

# count() : 특정 문자 개수 반환
print(string.count('m')) # 2

# find() : 특정 문자열 위치 반환. 없으면 -1 반환
crawling = 'Data crawling is fun'

print(crawling.find('fun')) # 17
print(crawling.find('f'))   # 17
print(crawling.find('parsing')) # -1 (없음)

# index
print(crawling.index('fun')) # 17
print(crawling.index('f'))   # 17
print(crawling.index('parsing')) # 못 찾으면 오류