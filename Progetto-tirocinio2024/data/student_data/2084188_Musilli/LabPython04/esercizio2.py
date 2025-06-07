b=True; i=0
while b:
    n=input("Inserisci un numero: ")
    if n=="*":  print("Numero di interi:",i); b=False
    elif int(n)>0:  i+=1
