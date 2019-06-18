N = int(input())
A = list(map(int, input().split()))
dp = [A[0]]
for i in range(1, N):
    dp.append(max(A[i], dp[i-1]+A[i]))
print(max(dp))
