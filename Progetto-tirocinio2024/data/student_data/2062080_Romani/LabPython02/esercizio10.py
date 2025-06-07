e=float(input('Inserire età del cane: '))
if e<=2 and e>=0:
      print(e*10.5)
elif e>2:
    print(2*10.5+(e-2)*4)
else: print('input non valido')
