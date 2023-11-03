def fibo_recur(n):
    
    return fibo_recur(n-1) + fibo_recur(n-2)

def fibo_dp(n):
    table = []
    table += [1,1]

    if n < 1 : return -1
    if n <= 2:
        return table[-1]
    
    for i in range(2, n):
        table.append(table[i-2] + table[i-1])

    return table[-1]

print(fibo_dp(10))