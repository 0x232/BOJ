n, k = map(int, input().split())
factorial = [1]
for i in range(1, n+1):
    factorial.append(i*factorial[i-1])
print((factorial[n]//(factorial[k]*factorial[n-k])) % 10007)

