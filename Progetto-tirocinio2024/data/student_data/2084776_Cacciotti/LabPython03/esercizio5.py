A = True

while A:
    s = str(input('inserire stringa'))
    if s.lower()==s:
        print(s[0],s[-1])
        A = False
