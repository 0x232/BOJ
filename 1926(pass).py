import queue


def is_in_range(n, m, row, col):
    return row >= 0 and row < n and col >= 0 and col < m

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
        if paper[i][j] == '1':
            number_of_picture += 1
            size_of_picture = 1
            q = queue.Queue()
            q.put((i, j))
            visited[i][j] = True
            while not q.empty():
                r, c = q.get()
                dr = [1, -1, 0, 0]
                dc = [0, 0, -1, 1]
                for i in range(4):
                    if is_in_range(n, m, r+dr[i], c+dc[i]) and\
                        paper[r+dr[i]][c+dc[i]] == '1' and\
                            not visited[r+dr[i]][c+dc[i]]:
                        size_of_picture += 1
                        q.put((r+dr[i], c+dc[i]))
                        visited[r+dr[i]][c+dc[i]] = True
        if size_of_picture > max_size_of_picture:
            max_size_of_picture = size_of_picture
        
print(number_of_picture, max_size_of_picture)
