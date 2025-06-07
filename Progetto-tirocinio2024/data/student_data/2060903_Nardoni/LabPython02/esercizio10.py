e=int(input("Inserisci l'età del cane per convertirla in età umana"))
if e>0:
    if e<=2:
        e*=10.5
        print(e)
    else:
        e=2*10.5+(e-2)*4
        print(e)
else:
    print("Non è possibile")
        
    
    
