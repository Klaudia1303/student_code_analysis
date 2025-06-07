var1 = input('Inserisci un numero intero: ')
var1 = int(var1)

for i in range(1, var1+1):
    if var1%i == 0:
        print(i)
    
