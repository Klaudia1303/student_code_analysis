sBefore: str = 'a'
s = ' '
while sBefore[-1] != s[0]:
    sBefore = s
    s = input('> ')

print(sBefore, s)
