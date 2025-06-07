n=input('inserisci una serie di numeri: ')
p=0
while n!='*':
    if(int(n))<0:
        p=p+int(n)
    n=input('inserisci una serie di numeri: ')
print(p)
