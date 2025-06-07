n=int(input("Inserisci un numero intero:"))
i=0
while(n!=0):
    n=int(input("Inserisci un numero intero:"))
    if(n%3==0):
        i+=n
print("La somma degli interi divisibili per 3 e' : ",i)
