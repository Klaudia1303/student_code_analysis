n1=int(input('Inserire un numero intero maggiore di 0: '))
n2=int(input('Inserire un altro numero intero maggiore di 0: '))
for i in range (n1,1,-1):
    if n1%i==0:
        divisoren1=i
    if i==divisoren1 and not n2%i==0:
        print(i)
