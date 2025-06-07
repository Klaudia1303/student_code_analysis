continua=True
s=0
counter=0
while continua==True:
    s=input("Inserisci un intero positivo: ")
    if s=='*':
        continua=False
    if continua==True and int(s)>0:
        counter=counter+1

print(counter)
