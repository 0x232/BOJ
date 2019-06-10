word = input()
alphabet = [0] * 26
for char in word.upper():
    alphabet[ord(char)-65] += 1
if alphabet.count(max(alphabet)) > 1:
    print('?')
else:
    print(chr(alphabet.index(max(alphabet))+65))
