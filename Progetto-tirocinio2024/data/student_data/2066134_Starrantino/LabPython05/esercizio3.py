s1: str = input('> ')
s2: str = input('> ')
out: str = ''
for c in s1:
    if c not in s2:
        out += c
print(out)