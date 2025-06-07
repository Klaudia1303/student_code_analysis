stop = False
w = str(input('Insert word: '))
l = w[-1]
while not stop:
    s = str(input('Insert word: '))
    c = s[0]
    if l==c:
        print(w,s)
        stop = True
    else:
        w = s
        l = s[-1]
