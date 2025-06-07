n=int(input('Inserisci un intero maggiore di 0: '))
i=0
a=1
b=1
if n==1:
    print (1)
elif n>=2:
    print (1,'\n',1)
while i<n-2:
    c=a+b
    print(c)
    a=b
    b=c
    i+=1
