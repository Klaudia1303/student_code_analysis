w = True

while w:
    s = str(input())
    if s.lower() == s:
        print(s[0],s[-1])
        w = False
