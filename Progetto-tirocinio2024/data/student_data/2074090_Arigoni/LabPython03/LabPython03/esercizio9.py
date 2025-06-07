finito=True
i=2
while finito:
    a=int(input("Inserisci un numero>> "))
    if a==2:
        print("Si tratta di un numero primo")
        finito=False
    if a%1==0 and a%a==0 and a%i>0:
        print("Si tratta di un numero primo")
        finito=False
    elif a!=2:
        print("Non si tratta di un numero primo")
        
