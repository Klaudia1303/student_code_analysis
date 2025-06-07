base=int(input("Inserisci base triangolo: "))
altezza=(base//2)+1
k=base-2
j=1
for i in range(altezza):
    print(k*' ', '*'*j)
    k-=1
    j+=2
    if(j==base):
        print(k*' ', '*'*j)
        break