n = int(input())
stairs = []
for _ in range(n):
    stairs.append(int(input()))
dp = []
dp.append(stairs[0])
dp.append(stairs[0] + stairs[1])
dp.append(max(stairs[0] + stairs[2], stairs[1] + stairs[2]))
for i in range(3, n):
    dp.append(max(stairs[i]+stairs[i-1]+dp[i-3], stairs[i]+dp[i-2]))
print(dp[n-1])
