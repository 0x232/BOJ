import sys
from collections import Counter
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
# 1. mean
print(round(sum(arr)/n))
# sorts the array
arr.sort()
# 2. median
print(arr[n//2])
# 3. mode
counter = Counter(arr).most_common()
if n == 1:
    print(arr[0])
else:
    if counter[0][1] == counter[1][1]:
        print(counter[1][0])
    else:
        print(counter[0][0])
# 4. range
print(max(arr)-min(arr))
