N = int(input())
dp = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
for i in range(1, N):
    dp.append([])
    for j in range(10):
        dp[i].append(sum(dp[i-1][j:]) % 10007)
print(sum(dp[N-1]) % 10007)
