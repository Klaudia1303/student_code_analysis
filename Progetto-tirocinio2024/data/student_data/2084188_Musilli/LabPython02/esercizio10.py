print("ESERCIZIO 10: inserita l\'età di un cane, convertirla in età umana\n")
e=float(input("Inserisci età del cane per convertirla in età umana: \t"))
x=10.5
if e>0:
    if e==1:
        y=x
    elif e==2:
        y=x*2
    elif e>2:
        y=((e-2)*4)+21
    elif e>1 and e<2:
        y=(x*(e-1))+x
    elif e<1:
        y=(x*e)
    print("L'età del cane risulta ",y," anni umani")
else:
    print("\bInput non ammesso")
