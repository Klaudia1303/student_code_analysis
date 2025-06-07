n1=int(input('Inserire intero maggiore di 0:'))
n2=int(input('Inserire un altro intero maggiore di 0:'))
if (n1 and n2)<0:
    n1=int(input('Valore non valido, inserirne uno nuovo:'))
    n2=int(input('Inserirne ancora uno:'))
var=1
while (n1 and n2)>0:
    for i in range(0,n1):
        if n1%var==0:
            print(int(n1/var))
            var+=1
    break
