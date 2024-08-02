T = int(input())

for test_case in range(1, T + 1):
    # "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
    tc, n = input().split()
    n = int(n)
    num_list = list(input().split())
    new_list = [0]*n
    k = 0

    for num in num_list:
        if num == 'ZRO':
            new_list[k] = 'ZRO'
            k += 1
    for num in num_list:
        if num == 'ONE':
            new_list[k] = 'ONE'
            k += 1
    for num in num_list:
        if num == 'TWO':
            new_list[k] = 'TWO'
            k += 1
    for num in num_list:
        if num == 'THR':
            new_list[k] = 'THR'
            k += 1
    for num in num_list:
        if num == 'FOR':
            new_list[k] = 'FOR'
            k += 1
    for num in num_list:
        if num == 'FIV':
            new_list[k] = 'FIV'
            k += 1
    for num in num_list:
        if num == 'SIX':
            new_list[k] = 'SIX'
            k += 1
    for num in num_list:
        if num == 'SVN':
            new_list[k] = 'SVN'
            k += 1
    for num in num_list:
        if num == 'EGT':
            new_list[k] = 'EGT'
            k += 1
    for num in num_list:
        if num == 'NIN':
            new_list[k] = 'NIN'
            k += 1
    print(tc, *new_list)