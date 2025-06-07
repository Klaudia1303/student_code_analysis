n=input('Inserire intero: ')
i=0
while n!='*':
    if int(n)<0:
        i+=int(n)
        n=input('Inserire intero: ')
    else:
        n=input('Inserire intero: ')
print(i)
