import collections


def find_island(h, w, row, col):
    # global grid, visited, direction
    
    queue = collections.deque([(row, col)])
    visited[row][col] = True
    while queue:
        r, c = queue.popleft()
        for i, j in direction:
            nr, nc = r+i, c+j
            if nr >= 0 and nr < h and nc >= 0 and nc < w and \
               grid[nr][nc] == '1' and not visited[nr][nc]:
                queue.append((nr, nc))
                visited[nr][nc] = True

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    grid = [input().split() for _ in range(h)]
    visited = [[False]*w for _ in range(h)]
    direction = [(-1, -1), (-1, 0), (-1, 1),
                 (0, -1), (0, 1),
                 (1, -1), (1, 0), (1, 1)]

    number_of_island = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '1' and not visited[i][j]:
                find_island(h, w, i, j)
                number_of_island += 1

    print(number_of_island)
