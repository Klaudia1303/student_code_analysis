s=input('inserisci una stringa: ')
parola1=s
x=len(parola1)
s=input('inserisci una stringa: ')
parola2=s
y=len(parola2)
finito=False
while not finito:
    s=input('inserisci una stringa: ')
    parola3=s
    if x+y==len(parola3):
        print(parola1, parola2, parola3)
        finito=True
    parola1=parola2
    x=len(parola1)
    parola2=parola3
    y=len(parola2)
    parola3=s
