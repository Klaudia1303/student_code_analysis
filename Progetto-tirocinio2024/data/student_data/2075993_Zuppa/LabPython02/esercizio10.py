a=float(input('inserire l età del cane   '))
if a<=0 :
    print('errore input')
else:
    if a<=2:
        print('l età del cane equivale a',a*10.5,' anni umani')
    else:
        print('l età del cane equivale a',21+((a-2)*4),'anni umani')
