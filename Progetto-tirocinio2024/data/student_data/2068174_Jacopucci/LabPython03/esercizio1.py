n1=int(input('inserire un numero intero maggiore di 2: '))
cont=2
mult=0
while(cont<n1):
    mult=mult+2
    print(mult)
    if(cont%2==0):
        cont=cont+1
    else:
        cont=cont+2
