n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
    
count = 0
while k != 0:
    if arr[-1] > k:
        arr.pop()
    else:
        n = k // arr[-1]
        k -= n * arr[-1]
        count += n
    
print(count)
