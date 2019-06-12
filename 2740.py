N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
M, K = map(int, input().split())
B = []
for _ in range(M):
    B.append(list(map(int, input().split())))

matrix = []
for i in range(N):
    matrix.append([])
    for k in range(K):
        matrix[i].append(sum(A[i][j]*B[j][k] for j in range(M)))
    print(' '.join(map(str, matrix[i])))
