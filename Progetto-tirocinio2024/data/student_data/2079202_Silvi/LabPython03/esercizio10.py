print("questo programma stampa tutti i numeri primi in un intervallo tra 2 e n\n")
n=int(input("inserire numero"))
numeri=[]
primo=True
for i in range (2,n):
    primo=True
    
    if i==2:
        numeri.append(i)
    else:

        for z in range (0,len(numeri)):
        
            if i%numeri[len(numeri)-z-1]==1:
                
                if z==len(numeri)-1:
                    numeri.append(i)
                    primo=True
            else:
                primo=False

    if primo:
        print(numeri[len(numeri)-1])
