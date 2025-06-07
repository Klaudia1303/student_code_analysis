mese=int(input('Inserisci un mese '))
anno=int(input('Inserisci un anno '))
x=mese+1
if 1<=mese<=12 and x!=13:
    print(x,anno)
elif 1<=mese<=12 and x==13:
    print(1, anno+1)
else:
    print('Input non valido')
