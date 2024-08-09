# 16466. 4866. 괄호검사
T = int(input())
for test_case in range(1, T+1):
    string = input()
    size = 0
    for char in string:
        if char == '(' or char == '[' or char == '{':
            size += 1
    stack = ['']*size

    idx = -1
    answer = 1

    for char in string:
        if char == '(' or char == '[' or char == '{':
            idx += 1
            stack[idx] = char
        elif char == ')':
            if stack[idx] != '(' or idx == -1:
                answer = 0
                break
            else:
                stack[idx] = ''
                idx -= 1
        elif char == ']':
            if stack[idx] != '[' or idx == -1:
                answer = 0
                break
            else:
                stack[idx] = ''
                idx -= 1
        elif char == '}':
            if stack[idx] != '{' or idx == -1:
                answer = 0
                break
            else:
                stack[idx] = ''
                idx -= 1
    if idx != -1:
        answer = 0
    print(f'#{test_case} {answer}')
