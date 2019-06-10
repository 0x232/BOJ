f = [1]
for i in range(1, int(input())+1):
    f.append(i*f[i-1])
print(f[-1])