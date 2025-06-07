print("questo programma stampa tutti i numeri pari compresi tra 2 e n \n")
n=int(input("inserire un numero maggiore di 2:"))
i=2

while i<=n:
    
    if i%2==0:
        print(i)
    i+=1
