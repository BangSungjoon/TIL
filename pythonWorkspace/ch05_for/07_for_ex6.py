a = 0
for i in [90, 57, 88, 45, 78]:
    a += 1
    if i > 60:
        print(f'{a}번 {i}점 합격')
    else:
        print(f'{a}번 {i}점 불합격')