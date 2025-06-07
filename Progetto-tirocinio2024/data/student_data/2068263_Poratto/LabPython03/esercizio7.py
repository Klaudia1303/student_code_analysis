k=input('inserisci carattere ')
x=input('inserisci stringa: ')
while x.count(k)<=2:
    x=input('inserire nuova stringa: ')
print('il carattere',k,'è contenuto',x.count(k),'volte in',x)
