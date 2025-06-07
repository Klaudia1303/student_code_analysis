
n1=int(input("inserisci un numero intero>0: "))
n2=int(input("inserisci un numero intero>0: "))
i=n1
while i>0:
    if n1%i==0 and n2%i!=0:
        print(i)
    i=i-1
