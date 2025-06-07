n=int(input('Inserisci un intero: '))

while n%5!=0: #entra nel ciclo quando il numero inserito non è divisibile per 5
    n=int(input('Inserisci un intero: ')) #printa n finchè non becca un
                                            #numero non divisibile per 5
    
print(n//5) #si usa // perchè altrimenti restituirebbe un float
