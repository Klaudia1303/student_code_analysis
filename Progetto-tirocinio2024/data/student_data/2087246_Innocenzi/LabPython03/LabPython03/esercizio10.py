n=int(input("Inserisci un numero intero positivo (n>1): "))

j=0
l=1
z=2
for i in range(z, n+1):
    while l<i:
        if i%l==0:
            j+=1
        l+=1
    if j<2:
        print(l)
    l=1
    j=0

    

    
