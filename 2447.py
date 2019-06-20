def fill(row, col, size):
    if size == 1:
        arr[row][col] = '*'
    else:
        size = size//3
        for i in range(3):
            fill(row+i*size, col, size)
            fill(row+i*size, col+2*size, size)
        fill(row, col+size, size)
        fill(row+2*size, col+size, size)

N = int(input())
arr = [[' ']*N for _ in range(N)]
fill(0, 0, N)
for i in range(N):
    print(''.join(map(str, arr[i])))
