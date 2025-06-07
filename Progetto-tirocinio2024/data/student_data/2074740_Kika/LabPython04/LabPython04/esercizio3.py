n='c'
k=0
while n!='*':
    n=input('inserisci intero: ')
    if n!='*':
        if int(n)<0:
            k=int(n)+k
print(k)
