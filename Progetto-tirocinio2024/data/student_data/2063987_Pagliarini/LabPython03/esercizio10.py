n=int(input("inserisci n"))
if n>1:
    i=2
    while i<=n:
        if i==2:
            print(i)
            i+=1
        j=2
        while (j<i and i%j!=0):
            j+=1
            
        if j==i:
            print(i)
        i+=1
        
else:
    print("il numero deve essere maggiore di 1")
