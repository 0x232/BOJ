n = int(input())
num = [0]*10
if n == 0:
    num[0] += 1
while n > 0:
    num[n%10] += 1
    n = n//10
num[6] = (num[6] + num[9] + 1) // 2
num[9] = 0
print(max(num))
