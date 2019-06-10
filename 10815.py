import sys

N = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

card.sort()
result = []
for m in num:
    low, high = 0, N-1
    answer = 0
    while low <= high:
        mid = (low + high) // 2
        if card[mid] == m:
            answer = 1
            break
        if card[mid] > m:
            high = mid - 1
        if card[mid] < m:
            low = mid + 1
    result.append(answer)

print(' '.join(map(str, result)))
