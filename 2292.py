n = int(input())
idx = 1
n = n-1
while n > 0:
    n -= idx*6
    idx += 1
print(idx)
