x=int(input("Inserire in input un numero intero: "))
n=2
ris=0
while x!=n:
    if x%n==0:
        ris+=1
    n+=1
if ris>0:
    print("numero non primo")
else:
    print("numero primo")
