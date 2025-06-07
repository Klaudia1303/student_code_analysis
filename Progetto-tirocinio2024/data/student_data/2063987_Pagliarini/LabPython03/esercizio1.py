n=int(input("inserisci un numero maggiore di 2"))
i=0
if n>2:
    while i<=n:
        
        if i%2==0 and i!=0:
            print(i)
        i+=1
else:
    print("il numero deve essere maggiore di 2")
        
