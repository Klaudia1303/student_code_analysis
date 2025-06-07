n=int(input("inserisci numero intero positivo "))
i=2
conta1=0
conta2=1
m=2
if n==1:
    print("1")
elif n==2:
    print("1\n1")
else:
    print("1\n1")
    while n-i>0:
        i+=1
        if conta1<conta2:
            conta1=conta2+conta1
        else :
            conta2= conta1+conta2
        m=conta1+conta2
        print(m)
