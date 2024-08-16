# 16520. 4874. Forth
T = int(input())

for test_case in range(1, T+1):
    # 문자열을 받는다.
    string = input().split()
    stack = []
    result = 'error'

    for s in string:
        # 숫자는 스택에 넣는다.
        if s.isdigit():
            stack.append(int(s))
        # . 을 만났다면 반환
        elif s == '.':
            if len(stack) == 1:
                result = stack.pop()
        # 연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.
        else:
            if len(stack) >= 2:
                n1 = stack.pop()
                n2 = stack.pop()
                if s == '+':
                    stack.append(n1 + n2)
                elif s == '*':
                    stack.append(n1 * n2)
                elif s == '-':
                    stack.append(n2 - n1)
                elif s == '/':
                    if n1 == 0 or n2 == 0:
                        break
                    stack.append(n2 // n1)
            else:   # stack의 길이가 2보다 작을 때,
                break

    print(f'#{test_case} {result}')