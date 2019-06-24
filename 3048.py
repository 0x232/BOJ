N1, N2 = map(int, input().split())
first = list(input())
second = list(input())
T = int(input())

group = [1]*(26)
for x in second:
    group[ord(x)-65] = 2

first.reverse()
ant = first + second

for _ in range(T):
    jump = []
    for i in range(N1+N2-1):
        # first group < second group
        if group[ord(ant[i])-65] < group[ord(ant[i+1])-65]:
            jump.append((i, i+1))
    for i, j in jump:
        ant[i], ant[j] = ant[j], ant[i]

print(''.join(ant))
