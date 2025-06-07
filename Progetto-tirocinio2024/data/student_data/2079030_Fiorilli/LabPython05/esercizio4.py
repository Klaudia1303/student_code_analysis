n1=n2=-1
while (n1 or n2)<=0:
    n1=int(input('inserisci un valore intero positivo: '))
    n2=int(input('inserisci un altro valore intero positivo: '))
if n1<n2:
    if n2%n1==0:
        mass=n2//n1
    else:
        mass=n2//n1+1
    for i in range (1,mass):
        print (n1*i)
else:
    print('il primo valore non ha multipli inferiori al secondo')
