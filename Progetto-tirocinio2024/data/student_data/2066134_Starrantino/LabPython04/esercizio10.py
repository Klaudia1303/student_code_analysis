s1, s2, s = input('> '), input('> '), input('> ')

while (len(s1) + len(s2)) != len(s):
    s1 = s2
    s2 = s
    s: str = input('> ')

print(s1, s2, s)
