n1=int(input("inserisci un numero intero:"))
n2=int(input("inserisci un numero intero:"))
for i in range(n1+1,2,-1):
    if n1%i!=0:
        continue
    if n2%i==0:
        continue
    print(i)
