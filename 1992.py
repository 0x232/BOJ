def check(image, row, col, size):
    if size == 1:
        return True
    for i in range(row, row + size):
        for j in range(col, col + size):
            if image[i][j] != image[row][col]:
                return False
    return True


def compress(image, row, col, size):
    s = ''
    if check(image, row, col, size):
        s += str(image[row][col])
    else:
        s += '('
        for i in range(row, row + size, size//2):
            for j in range(col, col + size, size//2):
                s += compress(image, i, j, size//2)
        s += ')'
    return s

N = int(input())
image = [list(map(int, list(input()))) for _ in range(N)]
print(compress(image, 0, 0, N))
