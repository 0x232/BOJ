import collections


def is_in_range(n, m, row, col):
    return row >= 0 and row < n and col >= 0 and col < m


def BFS(n, m, row, col):
    global board, visited

    q = collections.deque([(row, col, 0)])
    visited[row][col] = True
    while q:
        r, c, s = q.popleft()
        if board[r][c] == 1:
            return s
        next_direction = [(-1, -2), (-2, -1), (-1, 2), (-2, 1),
                          (1, -2), (2, -1), (1, 2), (2, 1)]
        for i, j in next_direction:
            if is_in_range(n, m, r+i, c+j) and \
               not visited[r+i][c+j]:
                q.append((r+i, c+j, s+1))
                visited[r+i][c+j] = True

for _ in range(int(input())):
    l = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    board = [[0]*l for _ in range(l)]
    visited = [[False]*l for _ in range(l)]

    board[x2][y2] = 1
    print(BFS(l, l, x1, y1))
