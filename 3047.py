arr = sorted(list(map(int, input().split())))
for x in input():
    print(arr[ord(x)-65], end=' ')
