s = input()
a = [s[i:] for i in range(len(s))]
for x in sorted(a):
    print(x)