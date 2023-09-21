def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return int(x / y)

a = 9
b = 3

print(f'{a} + {b} = {add(a,b)}')
print(f'{a} - {b} = {sub(a,b)}')
print(f'{a} * {b} = {mul(a,b)}')
print(f'{a} / {b} = {div(a,b)}')