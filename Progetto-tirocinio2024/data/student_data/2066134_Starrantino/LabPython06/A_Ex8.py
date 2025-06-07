s1: str = input('> ')
s2: str = input('> ')
n = int(input('n: '))
out: str = ''
for i in range(len(s1)):
    left = max(i - n, 0)
    right = min(i + n + 1, len(s1))
    if s1[i] in s2[left:right]:
        out += s1[i]
        continue
    
print(out)
