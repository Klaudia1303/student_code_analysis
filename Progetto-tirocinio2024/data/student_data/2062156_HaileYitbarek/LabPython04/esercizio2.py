n=input('inserire numero intero: ')
a=0
while n!='*':
    b=int(n)
    if b>=0:
        a=a+1
        n=input('inserire numero intero: ')
    else:
        n=input('inserire numero intero: ')
print('numero di interi positivi inseriti: ',a)
        
