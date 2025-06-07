s=input('Inserisci una stringa: ')
p=input('Inserisci una stringa di lunghezza uguale alla prima: ')
while len(s)!=len(p):
    s=input('Le due stringhe non hanno la stessa lunghezza. Inserisci una stringa: ')
    p=input('Inserisci una stringa di lunghezza uguale alla prima: ')
n=0
while n<len(p):
    for i in s:
        print(i+p[n],end='')
        n+=1