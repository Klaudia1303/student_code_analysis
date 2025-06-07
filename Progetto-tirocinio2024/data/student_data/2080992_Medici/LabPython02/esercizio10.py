cane=input('inserire l\'età del cane: ')
cane=float(cane)
if cane<=2 and cane!=0:
    cane=cane*10.5
    print('il cane ha:',cane)
elif cane>2:
    cane=21+((cane-2)*4)
    print('il cane ha:',cane)
else:
    print('l\'età del cane non può essere inferiore a 0')
