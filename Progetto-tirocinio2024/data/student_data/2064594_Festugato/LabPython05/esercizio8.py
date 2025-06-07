n = int(input('inserisci un intero positivo dispari maggiore o uguale a 3: '))
#disegno triangolo isoscele di base n dispari
for i in range(1,n+1,2):
    #print(list(range(1,n+1,2)))
    spazio = (' ' * ((n-i)//2))#divisone intera per non dare errore
    print((spazio+('*'*i)+spazio))#ordine per riga
    
    
