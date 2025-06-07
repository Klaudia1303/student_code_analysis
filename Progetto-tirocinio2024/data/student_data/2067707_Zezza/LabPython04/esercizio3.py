i=0
n=0
while n!='*':
    n=int(n)
    if n<0:
        i=i+n
    n=input('inserisci intero (* per terminare): ')
print(i)
