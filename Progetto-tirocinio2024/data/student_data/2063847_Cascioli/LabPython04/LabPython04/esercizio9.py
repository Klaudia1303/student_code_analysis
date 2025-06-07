i=1
j=0
n=int(input("Inserisci un numero intero maggiore di zero: "))
while(n<=0):
    print("Numero non corretto, reinserire: ")
    n=int(input("Inserisci un numero intero maggiore di zero: "))
while(j<n):
    print(i)
    j+=i
    i+=j
    print(j)


   
    
