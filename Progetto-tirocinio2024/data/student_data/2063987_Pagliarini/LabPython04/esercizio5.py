n=int(input("inserici un n maggiore o uguale di 0: "))
fact=n
if n>1:
    while n>1:
        fact=fact*(n-1)
        n=n-1

elif n>=0:
    print(1)
else:
    print("inserisci un n maggiore o uguale a 0: ")
        
print(fact)        
