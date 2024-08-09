def f2(c, d):
    return c-d

def f1(a, b):
    c = a+b
    d = 10
    return f2(c, d)

a = 10
b = 20
print(f1(a, b))

# stack 구조로 코드가 구성 되어있다.