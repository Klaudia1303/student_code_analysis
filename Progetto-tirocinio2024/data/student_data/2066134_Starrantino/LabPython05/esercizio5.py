s: str = input('> ')
n: int = int(input('> '))
out: bool = False
for i in range(len(s)-n):
    if s[i] == s[i+n]:
        out = True
        break
print(out)