N = int(input())
dp = [0, 0, 1, 1]
for i in range(4, N+1):
    if i % 6 == 0:
        v = min(dp[i//3]+1, dp[i//2]+1, dp[i-1]+1)
    elif i % 3 == 0:
        v = min(dp[i//3]+1, dp[i-1]+1)
    elif i % 2 == 0:
        v = min(dp[i//2]+1, dp[i-1]+1)
    else:
        v = dp[i-1]+1
    dp.append(v)
print(dp[N])
