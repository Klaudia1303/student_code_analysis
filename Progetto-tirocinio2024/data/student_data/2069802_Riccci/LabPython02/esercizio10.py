n = float(input("Inserisci età cane --> "))
if(n>=0):
    if(n<=2):
        print("equivale a ",n*(10.5))
    else:
        print("equivale a ",2*10.5+(n-2)*4)
else:
    print("input non valido")
