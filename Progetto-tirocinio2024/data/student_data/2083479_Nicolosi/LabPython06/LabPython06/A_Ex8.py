s1=input('Inserisci una stringa: ')
s2=input('Inserisci una stringa: ')
n=int(input('Inserisci un numero intero: '))
for c in s1:
    x=s1.find(c)
    if c in s2:
        y=s2.find(c)
        if abs(x-y)<=n:
            print(c,end='')