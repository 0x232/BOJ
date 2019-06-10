n = int(input())
m = 1000000
p = 1500000
n = n % p
fib = [0,1]
for i in range(2,n+1):
    fib.append((fib[i-1]+fib[i-2]) % m)
print(fib[n] % m)
