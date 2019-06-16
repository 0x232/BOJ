def star(r, c, n):
    if n > 1:
        star(r, c, n//2)
        star(r+n, c-n, n//2)
        star(r+n, c+n, n//2)
    else:
        triangle[r][c+2] = '*'
        triangle[r+1][c+1] = '*'
        triangle[r+1][c+3] = '*'
        for i in range(c, c+5):
            triangle[r+2][i] = '*'

N = int(input())
triangle = [[' ' for _ in range(N*2-1)] for _ in range(N)]

star(0, N-3, N//2)

for i in range(N):
    print(''.join(map(str, triangle[i])))
