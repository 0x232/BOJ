import sys

arr = []
for _ in range(9):
    arr.append(list(map(int, input().split())))


def check(arr, row, col, value):
    # check row
    if value in arr[row]:
        # print('row is not valid')
        return False
    # check col
    if value in [arr[i][col] for i in range(9)]:
        # print('col is not valid')
        return False
    # check box
    row, col = (row//3)*3, (col//3)*3
    for i in range(row, row+3):
        for j in range(col, col+3):
            if arr[i][j] == value:
                # print('box is not valid')
                return False
    return True


def empty(arr):
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                return (i, j)
    return ()


def solve():
    if not empty(arr):
        for i in range(9):
            print(' '.join(map(str, arr[i])))
        sys.exit()
        
    while empty(arr):
        i, j = empty(arr)
        for value in range(1, 10):
            if check(arr, i, j, value):
                arr[i][j] = value
                solve()
                arr[i][j] = 0
        return

solve()
