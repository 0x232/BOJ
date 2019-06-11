arr = []
for _ in range(int(input())):
    arr.append(list(map(int, input().split())))

rank = []
for x in arr:
    count = 1
    for y in arr:
        if x[0] < y[0] and x[1] < y[1]:
            count += 1
    rank.append(count)

print(' '.join(map(str, rank)))
