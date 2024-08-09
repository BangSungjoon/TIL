# 계산기2
for test_case in range(1, 11):
    N = int(input())
    string = input()
    back_string = ''
    stack = []
    lady_first = {'+':1, '*':2}

    for s in string:
        if s in '+*':
            while stack and lady_first[s] <= lady_first[stack[-1]]:
                back_string += stack.pop()
            stack.append(s)
        else:
            back_string += s
    while stack:
        back_string += stack.pop()

    for s in back_string:
        if s in '+*':
            n1 = stack.pop()
            n2 = stack.pop()
            if s == '+':
                stack.append(n1 + n2)
            else:
                stack.append(n1 * n2)
        else:
            stack.append(int(s))
    result = stack.pop()

    print(f'#{test_case} {result}')