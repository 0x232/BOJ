from itertools import groupby

for _ in range(int(input())):
    arr = []
    for _ in range(int(input())):
        arr.append(input().split())

    arr.sort(key=lambda x: x[1])
    answer = 1
    for _, l in groupby(arr, key=lambda x: x[1]):
        answer *= len(list(l)) + 1
    print(answer - 1)
    