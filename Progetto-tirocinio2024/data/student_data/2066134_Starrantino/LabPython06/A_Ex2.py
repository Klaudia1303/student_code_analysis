s: str = input('> ')
if s == s[::-1]:
    print(len(s))
else:
    i: int = 0
    while s[i] == s[-1-i]:
        i += 1  
    print(i)
