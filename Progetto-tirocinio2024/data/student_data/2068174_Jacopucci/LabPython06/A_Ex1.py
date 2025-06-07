n1=int(input('inserire un numero intero maggiore di 0: '))
n2=int(input('inserire un numero intero maggiore di 0: '))
c=n1
while c>0:
    if (n1%c==0 and c!=n2):
        print (c)
        c-=1
    else:
        c-=1
        
