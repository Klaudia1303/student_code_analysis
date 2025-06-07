n=0
for i in range(9):
    for u in range(9):
        k=format(i,'02o')
        h=format(u,'02o')
        n=format(i*u,'02o')
        print(f'{k}x{h}={n}')
