N = int(input())
first, second, third = [], [], []
number = [[0]*(101) for _ in range(3)]
score = [0]*N
for i in range(N):
    x, y, z = map(int, input().split())
    first.append(x)
    second.append(y)
    third.append(z)

for i in range(N):
    number[0][first[i]] += 1
    number[1][second[i]] += 1
    number[2][third[i]] += 1

for i in range(N):
    if number[0][first[i]] == 1:
        score[i] += first[i]
    if number[1][second[i]] == 1:
        score[i] += second[i]
    if number[2][third[i]] == 1:
        score[i] += third[i]

print('\n'.join(map(str, score)))