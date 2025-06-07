n=int(input('Inserire un intero maggiore di 0:'))
n1=n2=1
i=2
while n<=0:
    n=int(input('Valore non valido, inserirne uno maggiore di 0:'))
if n==1:
    print(n1)
elif n>1:
    print(n1,'\n',n2)
while i<n:
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3)
    i+=1
