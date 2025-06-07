n1=int(input('inserisci un numero intero: '))
n2=int(input('inserisci un numero intero: '))
i=1
for i in range(n2):
    if (n1*i)<n2 and (n1*i)>0:
        print(n1*i)
