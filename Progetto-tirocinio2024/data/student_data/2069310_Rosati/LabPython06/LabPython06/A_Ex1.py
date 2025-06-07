n1=int(input("Inserisci numero intero maggiore di 0: "))
n2=int(input("Inserisci numero intero maggiore di 0:"))

for i in range(n1,1,-1):
    if n1%i==0 and n2%i!=0:
       print(i)
       
    
