import collections


def check_field():
    flag = False
    puyo = []
    for i in range(12):
        for j in range(6):
            if field[i][j] != '.' and not visited[i][j]:
                puyo += pop_puyo(i, j, field[i][j])
                if puyo:
                    flag = True
    drop_puyo()
    return flag


def pop_puyo(row, col, color):
    queue = collections.deque([(row, col)])
    visited[row][col] = True
    number_of_puyo = 1
    puyo = []
    while queue:
        r, c = queue.popleft()
        puyo.append((r, c))
        for i, j in direction:
            nr, nc = r+i, c+j
            if nr >= 0 and nr < 12 and nc >= 0 and nc < 6 and \
               field[nr][nc] == color and not visited[nr][nc]:
                queue.append((nr, nc))
                visited[nr][nc] = True
                number_of_puyo += 1

    if number_of_puyo >= 4:
        for i, j in puyo:
            field[i][j] = '.'
        return puyo
    else:
        return []


def drop_puyo():
    col = ['']*6
    for j in range(6):
        for i in range(12):
            col[j] += field[i][j]
    for j in range(6):
        col[j] = col[j].replace('.', '')
        col[j] = '.'*(12-len(col[j])) + col[j]
    for j in range(6):
        for i in range(12):
            field[i][j] = col[j][i]

field = [list(map(str, input())) for _ in range(12)]
visited = [[False]*6 for _ in range(12)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

number_of_chain = 0
while True:
    flag = check_field()
    visited = [[False]*6 for _ in range(12)]

    if not flag:
        break
    else:
        number_of_chain += 1

print(number_of_chain)
