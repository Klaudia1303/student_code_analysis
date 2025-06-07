finito=False
while not finito:
    i=int(input("inserisci un intero: "))
    if i%5!=0:
        print(i)
    else:
        print(i/5)
        finito=True
        
