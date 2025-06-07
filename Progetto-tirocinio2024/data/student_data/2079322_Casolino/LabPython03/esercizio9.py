n=int(input('Inserisci un numero intero: '))
i=1
m=0
while i<=n: #finchè la condizione i<=n è vera si sta nel ciclo
    if n%i==0: #perchè il numero primo è divisibile per 1 e per sè stesso
        m+=1
    i+=1
if m<3 and n!=0: 
    print('Numero primo')
else:
    print('Non numero primo')
    
#per verificare se un numero è primo è sufficiente provare a dividerlo
#per tutti gli interi minori di esso
#se almeno uno di questi interi è un divisore allora non è primo
