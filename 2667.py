def check(r, c, size):
    return r >= 0 and r < size and c >= 0 and c < size


def DFS(r, c, n):
    arr[r][c] = n
    x = [0, 0, -1, 1]
    y = [1, -1, 0, 0]
    for i in range(4):
        if check(r+x[i], c+y[i], N) and arr[r+x[i]][c+y[i]] == 1:
            DFS(r+x[i], c+y[i], n)

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

n = 2
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            DFS(i, j, n)
            n += 1

arr = [arr[i][j] for i in range(N) for j in range(N)]
print(max(arr)-1)
house = list(map(arr.count, range(2, max(arr)+1)))
for x in sorted(house):
    print(x)
