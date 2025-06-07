n1=int(input("inserisci un numero intero :"))
n2=int(input("inserisci un numero intero :"))
i1=""
i2=""
while n1<0 or n2<0:
    n1=int(input("inserisci un numero intero :"))
    n2=int(input("inserisci un numero intero :"))
for i in range(1,n2+1):
    div2=n2/i
    i2=i2+str(div2)
for i in range(1,n1+1):
    div1=n1/i
    if str(div1) not in i2 and n1%i==0:
        print (int(div1))
    
