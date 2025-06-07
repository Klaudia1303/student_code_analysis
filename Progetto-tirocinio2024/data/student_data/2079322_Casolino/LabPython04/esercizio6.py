moltiplicando = int(input('Inserire il moltiplicando: '))
moltiplicatore = int(input('Inserire il moltiplicatore: '))

#sommare il moltiplicando per se stesso,
#quante volte indicato dal moltiplicatore

i = 0 #accumulatore
somma = 0

if moltiplicatore == 0: #se il moltiplicatore è 0, anche la somma è 0,
                        #ovvero il prodotto
    somma = 0
elif moltiplicatore > 0:  
    while i < moltiplicatore:
        somma = somma + moltiplicando
        i += 1
elif moltiplicatore < 0:
    while i > moltiplicatore: 
        somma = somma - moltiplicando
        i -= 1
print(somma)
