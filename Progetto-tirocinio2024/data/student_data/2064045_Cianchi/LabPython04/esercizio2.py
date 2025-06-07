n=int(input('inserire un numero intero:'))
i=1
while n!='*':
    n=input('inserire un numero intero (* per terminare):')
    if n!='*' and int(n)>=0:
        i+=1
print(i)
