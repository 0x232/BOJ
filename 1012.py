import queue


def is_in_range(n, m, row, col):
    return row >= 0 and row < n and col >= 0 and col < m


def BFS(n, m, row, col):
    q = queue.Queue()
    # number_of_cabbage = 1
    q.put((row, col))
    visited[row][col] = True
    while not q.empty():
        r, c = q.get()
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        for i in range(4):
            if is_in_range(n, m, r+dr[i], c+dc[i]) and \
               not visited[r+dr[i]][c+dc[i]] and \
               field[r+dr[i]][c+dc[i]] == 1:
                # number_of_cabbage += 1
                q.put((r+dr[i], c+dc[i]))
                visited[r+dr[i]][c+dc[i]] = True
    # return number_of_cabbage

field = [[0]*50 for _ in range(50)]
visited = [[False]*50 for _ in range(50)]

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    # Initialization
    for i in range(N):
        for j in range(M):
            field[i][j] = 0
            visited[i][j] = False
    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1

    number_of_area = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1 and not visited[i][j]:
                BFS(N, M, i, j)
                number_of_area += 1

    print(number_of_area)
