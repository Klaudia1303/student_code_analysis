#Due viaggiatori partono insieme a velocità differenti: il primo viaggiatore viaggia alla velocità di 20 
#chilometri al giorno; il secondo viaggia alla velocità di 1 chilometro al giorno il primo giorno, 2 il secondo, 3 
#il terzo e così via (problema posto da Fibonacci nel 1200). Scrivere un programma Python, parametrico 
#rispetto alle due velocità, che stampa il numero di giorni necessari al primo viaggiatore per raggiungere il 
#secondo, senza usare la formula della successione. Usare un ciclo for con mille iterazioni con un break al suo 
#interno.
#il risultato è 39
v1=20
giorno=1
v2=1


for i in range(1,100):
    v1+=20
    v2=v2+(giorno+1)
    giorno=giorno+1
    if v2==v1:
        break
print(giorno)

    
    


    

