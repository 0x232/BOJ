def num(x, n):
    i = 0
    while x % n == 0:
        i += 1
        x = x // n
    return i
    
i, j = 0, 0
for x in range(1, int(input())+1):
    i += num(x, 2)
    j += num(x, 5)
print(min(i, j))