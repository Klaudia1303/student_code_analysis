print("questo programma stampa tutti i divisori di un numero n \n")
n=int(input("inserire il numero:"))
i=1

while i<=n:
    
    if n%i==0:
        print(i)
    i+=1
