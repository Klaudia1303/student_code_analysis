stop = False
while not stop:
    s =str(input('Insert characters here: '))
    print(s[0]+s[-1])
    if s.isalpha() and s.islower():
        stop = True
