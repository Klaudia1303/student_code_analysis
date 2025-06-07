n1=int(input('Inserire un numero intero maggiore di 0: '))
n2=int(input('Inserire un seecodo numero intero maggiore di 0: '))
for i in range (n1,0,-1):
    if n1%i==0 and n2%i!=0:
        print(i)
