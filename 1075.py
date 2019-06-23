N = int(input())
F = int(input())
temp = N - N % 100
if temp % F == 0:
    result = temp % 100
else:
    result = (temp + (F - temp % F)) % 100
print('0'+str(result) if result < 10 else result)
