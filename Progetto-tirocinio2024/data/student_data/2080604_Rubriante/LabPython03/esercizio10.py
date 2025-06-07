n=int(input("Inserire in input un numero intero maggiore di 1: "))
n2=n
ris=0
while n!=0:
    while x!=n2:
        if x%n==0:
            ris+=1
        n+=1
    if ris>0:
        print("numero non primo")
    else:
        print("numero primo")
