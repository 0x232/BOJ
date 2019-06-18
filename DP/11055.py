N = int(input())
A = list(map(int, input().split()))
dp = A.copy()
for i in range(len(A)):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+A[i])
print(max(dp))
