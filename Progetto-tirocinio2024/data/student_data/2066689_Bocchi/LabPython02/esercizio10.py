c= int(input('età cane: '))

if c>0:
    if c<=2:
        print(c*10.5)
    elif c>2:
        print((c-2)*4+21)
else:
    print('input non valido')
