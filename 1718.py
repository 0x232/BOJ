a = 'abcdefghijklmnopqrstuvwxyz'
text = input()
key = input()
l = len(key)
for i in range(len(text)):
    if text[i] == ' ':
        print(' ', end='')
    else:
        k = key[i % l]
        p = text[i]
        print(a[ord(p)-ord(k)-1], end='')
