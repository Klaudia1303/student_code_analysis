s=input('Inserisci un numero intero ("*" per terminare): ')
n_positivi=0

while s!="*":
    n=int(s)
    if n>0:
        n_positivi+=1
    s=input('Inserisci un numero intero ("*" per terminare): ')
print(n_positivi)
