import sys
import operator

# TODO: Reduce time complexty.


def check(row, col, size):
    if size == 1:
        return True
    for i in range(row, row + size):
        for j in range(col, col + size):
            if arr[i][j] != arr[row][col]:
                return False
    return True


def solve(row, col, size):
    if check(row, col, size):
        if arr[row][col] == -1:
            return (1, 0, 0)
        if arr[row][col] == 0:
            return (0, 1, 0)
        if arr[row][col] == 1:
            return (0, 0, 1)
    else:
        count = (0, 0, 0)
        for i in range(row, row + size, size//3):
            for j in range(col, col + size, size//3):
                count = tuple(map(operator.add, count, solve(i, j, size//3)))
        return count

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))
print('\n'.join(map(str, solve(0, 0, N))))
