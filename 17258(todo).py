N, M, K, T = map(int, input().split())
people = [0]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    for i in range(a, b):
        people[i] += 1
total = 0
for i in range(1, N+1):
    if people[i] < K:
        # TODO: complete code
        pass
    if people[i] >= K:
        total += 1
    print(people)
