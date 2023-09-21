# 중첩 for ~ else 문
count = 0

for i in range(5):
    for j in range(5):
        count += 1
        print(i, j, count)

        if j == 2 :
            print('break')
            break
    
    else :
        continue # 아래 break 수행 안 함
    
    break

#################################################
x = 20
for i in range(5):
    for j in range(5):
        if j == x :
            print('break')
            break
    
    else :
        print('수행')
        continue # 아래 break 수행 안 함

    break