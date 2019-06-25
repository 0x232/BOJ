burger = []
soda = []
for _ in range(3):
    burger.append(int(input()))
for _ in range(2):
    soda.append(int(input()))
print(min(burger)+min(soda)-50)