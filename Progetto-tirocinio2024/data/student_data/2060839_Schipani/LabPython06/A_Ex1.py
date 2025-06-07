n1=int(input('inserisci un numero '))
n2=int(input('inserisci un numero '))
for i in range(n1,0,-1):
    if n2%i!=0 and n1%i==0:
        print(i)
