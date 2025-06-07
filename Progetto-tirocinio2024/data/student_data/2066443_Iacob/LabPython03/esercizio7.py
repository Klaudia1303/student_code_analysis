c = str(input('Insert character: '))
stop = False
while not stop:
    s = str(input('Insert word: '))
    if s.count(c)>2:
        print(s.count(c))
        stop = True
