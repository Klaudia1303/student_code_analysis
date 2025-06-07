ac=float(input('età cane: '))
if 0<=ac<=2:
    print('età umana:',10.5*ac)
elif ac>2:
    print('età cane:',10.5*2+(ac-2)*4)
elif ac<0:
    print('input non valido')
