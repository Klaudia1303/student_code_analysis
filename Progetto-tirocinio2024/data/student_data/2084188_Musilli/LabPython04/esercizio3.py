b=True; s=0
while b:
    n=input("Inserisci un numero: ")
    if n=="*":  print("Somma dei numeri negativi:",s); b=False
    elif int(n)<0:  s+=int(n)
