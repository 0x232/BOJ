for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    queue = [(i, arr[i]) for i in range(n)]
    idx = 0
    while queue:
        if queue[0][1] < max(queue, key=lambda x: x[1])[1]:
            queue.append(queue.pop(0))
        else:
            idx += 1
            if queue.pop(0)[0] == m:
                break
    print(idx)
