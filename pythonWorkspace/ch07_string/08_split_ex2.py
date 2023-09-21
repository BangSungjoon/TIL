str_data = "{a1 : 20}, {a2 : 30}, {a3 : 15}, \
            {a4 : 50}, {a5 : -15}, {a6 : 80}, \
            {a7 : 0}, {a8 : -110}"

# 문자열을 콤마(,)로 분할
str_data_split = str_data.split(',')

# 숫자만 추출해서 총 합계 구하기
total = 0
for data in str_data_split:
    result = data.split(':')[1].split('}')[0]

    total += int(result)

print(total)

##################################################
# (2) split() 여러 번 나눠서 적용할 경우
total = 0
for data in str_data_split:
    result = data.split(':')[1]
    result2 = result.split('}')[0]

    total += int(result2)

print(total)