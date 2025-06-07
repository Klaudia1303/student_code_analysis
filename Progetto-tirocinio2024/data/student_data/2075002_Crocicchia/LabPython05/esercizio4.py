n1=int(input('inserisci un intero positivo: '))
n2=int(input('inserisci un intero positivo: '))
a=1
b=1
while a<n2:
    a=b*n1
    b+=1
    if a<n2:
        print(a)
        
        