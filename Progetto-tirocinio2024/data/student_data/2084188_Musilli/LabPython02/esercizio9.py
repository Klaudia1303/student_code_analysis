print("ESERCIZIO 9: inserimento di un mese e di un anno (es. 9 2016)\
e stampa uguale ma con mese aumentato di 1\n\n")
mese=int(input("Inserire il mese: \t"))
anno=int(input("Inserire l\'anno: \t"))
if mese>0 and mese<13:
    if mese==12:
        mese=1
        anno+=1
    print("\nRisulato:\t",mese,anno)
else:
    print("Input non valido: Il mese non è stato inserito \
nel modo giusto (deve essere compreso tra 1 e 12 inclusi)")
