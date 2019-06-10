s = input()
for x in [s.count(chr(i+97)) for i in range(26)]:
    print(x, end=' ')
