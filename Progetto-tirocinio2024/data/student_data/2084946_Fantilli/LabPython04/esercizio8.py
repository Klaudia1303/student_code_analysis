s = input()
a = True
while a:
    x = input()
    if s[len(s)-1:] != x[:1]:
        s = input()
    elif s[len(s)-1:] == x[:1]:
        a = False
        print(s, x)
