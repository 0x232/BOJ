arr = [[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]]
for a in range(1,15):
    arr.append([])
    for b in range(0,15):
        arr[a].append(sum(arr[a-1][1:b+1]))
    print(arr[a])
for _ in range(int(input())):
    n = int(input())
    k = int(input())
    print(arr[n][k])
