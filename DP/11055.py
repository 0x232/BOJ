N = int(input())
A = list(map(int, input().split()))
dp = A.copy()
for i in range(len(A)):
    for j in range(i):
        if A[j] < A[i]:
            '''
            Test Case
            10
            1 100 55 50 60 3 5 6 7 8
            '''
            dp[i] = max(dp[i], dp[j]+A[i])
print(max(dp))
