n1=-1
n2=-1
while n1 < 0 or n2 < 0:
    n1=int(input("Inserire il primo numero intero maggiore di zero: "))
    n2=int(input("Inserire il secondo numero intero maggiore di zero: "))
for i in range(0,n1):
    divisore_n1=n1-i
    resto_n1=n1%divisore_n1
    if resto_n1==0 and divisore_n1>n2:
        print(str(divisore_n1))
    else:
        break

for i in range(0,n2):
    divisore_n1=n1-i
    resto_n1=n1%divisore_n1
    if resto_n1==0 and divisore_n1<=n2:
        divisore_n2=n2-i
        resto_n2=n2%divisore_n2
        if resto_n2==0 and divisore_n1 != divisore_n2:
            print(str(divisore_n2))
        
