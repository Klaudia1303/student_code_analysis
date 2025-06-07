positivo=0
n=3
while n!='*':
    n=input('Inserisci un numero intero(* per terminare): ')
    if n=='*':
        print(positivo)
    elif int(n)>0:
        positivo=positivo+1
        
