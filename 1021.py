from collections import deque
n, m = map(int, input().split())
d = deque([i+1 for i in range(n)])
num = map(int, input().split())

left, right = 0, 0
for x in num:
    n = len(d)
    idx = d.index(x)
    if idx < n-idx:
        d.rotate(-idx)
        left += idx
    else:
        d.rotate(n-idx)
        right += n-idx
    d.popleft()
print(left+right)
