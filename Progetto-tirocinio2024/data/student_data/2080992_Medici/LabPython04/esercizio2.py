tot=0
n=0
while n!='*':
    n=str(input('inserisci un numero intero: '))
    if n=='*':
        print(tot)
        break
    else:
        n=int(n)
        if n>0:
            tot+=1
