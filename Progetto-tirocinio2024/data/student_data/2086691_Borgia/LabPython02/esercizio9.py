mese=int(input('Inserire un mese (luinguaggio numerico) '))
anno=int(input('Inserire un anno '))
if mese>=12 or mese<1:
    print('input non valido')
else:
    print(mese+1,anno+1)
