x = int(input())
n = 1
while n*(n+1)//2 < x:
    n += 1
i = n*(n+1)//2 - x
if n % 2 == 0:
    x1 = n - i
    x2 = i + 1
else:
    x2 = n - i
    x1 = i + 1
print('{}/{}'.format(x1, x2))
