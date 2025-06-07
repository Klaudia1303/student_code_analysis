a = input('Inserisci l\'età del cane: ')
a1 = float(a)
if a.isdecimal() and a1>0:
    if a1 <= 2:
        print(10.5*a1)
    elif a1 > 2:
        print(21+((a1-2)*4))
