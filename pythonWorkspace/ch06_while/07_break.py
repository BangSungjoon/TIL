# break

# (1) 가까운 for문 중단. 바깥 for문 계속 수행
count = 0

for i in range(5):
    for j in range(5):
        count += 1
        print(i, j, count)

        if j == 2:
            print('break')
            break  # 안의 for 문만 중단

# (2) 바깥 for문도 중단 : flag 사용
flag = True
count = 0

for i in range(5):
    for j in range(5):
        count += 1
        print(i, j, count)

        if j == 2:
            print('break')
            flag = True
            break # 안의 for문 중단
    if(flag):
        break # 바깥 for문 중단