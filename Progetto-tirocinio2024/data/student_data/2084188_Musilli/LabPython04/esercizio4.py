b=True; s=0
while b:
    n=int(input("Inserisci un numero (se inserito 0 termina): "))
    if n==0:  print("Somma dei numeri divisibili per 3:",s); b=False
    elif n%3==0:  s+=n
