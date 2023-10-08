nums = [1, 2, 3, 4, 5]
x = [n*10 if n % 2 == 0 else n*100 for n in nums]
print(x)