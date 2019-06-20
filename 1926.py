import queue


def is_in_range(n, m, row, col):
    return row >= 0 and row < n and col >= 0 and col < m


def BFS(n, m, row, col):
    q = queue.Queue()
    size_of_picture = 1
    q.put((row, col))
    visited[row][col] = True
    while not q.empty():
        r, c = q.get()
        dr = [1, -1, 0, 0]
        dc = [0, 0, -1, 1]
        for i in range(4):
            if is_in_range(n, m, r+dr[i], c+dc[i]) and \
               not visited[r+dr[i]][c+dc[i]] and \
               paper[r+dr[i]][c+dc[i]] == '1':
                size_of_picture += 1
                q.put((r+dr[i], c+dc[i]))
                visited[r+dr[i]][c+dc[i]] = True
    return size_of_picture

paper = []
visited = []

n, m = map(int, input().split())
for _ in range(n):
    paper.append(input().split())
    visited.append([False] * m)

number_of_picture = 0
max_size_of_picture = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j] and paper[i][j] == '1':
            number_of_picture += 1
            max_size_of_picture = max(max_size_of_picture, BFS(n, m, i, j))

print(number_of_picture, max_size_of_picture, sep='\n')
