s = input('> ')
b: bool = False
for c in s:
    if not b:
        b = s.count(c) > 1
    if b:
        break
print(b)