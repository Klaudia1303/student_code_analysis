c=input('inserire carattere')
finito=False
while not finito:
    s=input('inserire stringa')
    if s.count('c')>2:
        print(s.count('c'))
        finito=True
