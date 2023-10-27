def gcd2(a,b):
    while(b > 0):
        a, b = b, a % b

    return a

# 최소공배수
def lcm(a, b):
    return a * b / gcd2(a,b)

lcm(4, 6)