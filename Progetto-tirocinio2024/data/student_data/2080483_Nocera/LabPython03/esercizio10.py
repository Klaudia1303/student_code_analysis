numero = int(input("inserisci un numero: "))
while numero<1:
    numero = int(input("inserisci un numero: "))
i = 2
while 2<=i<=numero:
    div = 2
    count=0
    while div<=i/2 and count == 0:
        if i%div==0:
            count+=1
        div+=1

    if count==0: 
        print(i)
    i+=1



       
        
            

        
    