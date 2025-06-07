continua=True
counter=0
while continua==True:
    s=input("Inserisci un numero intero: ")
    if s=='*':
        continua=False
    if continua==True and int(s)<0:
        counter=int(s)+counter
print(counter)
