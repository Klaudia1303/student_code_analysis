print("questo programma stampa termina quando il numero che si inserisce è divisibile per 5 \n")

n=int(input("inserire un numero intero:"))
i=0

while i==0:
    n=int(input("inserire un numero intero:"))
    
    if n%5==0:
        print(n/5)
        i+=1
