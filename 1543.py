text = input()
word = input()
t = len(text)
w = len(word)
i = 0
count = 0
while i < t:
    if text[i:i+w] == word:
        count += 1
        i += w
    else:
        i += 1
print(count)
