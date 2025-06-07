var1 = input('Inserisci un numero intero: ')
var1 = int(var1)
var2 = input('Inserisci un numero intero: ')
var2 = int(var2)
var3 = 0

while var3 < var2:
    var3 += 1
    if var1 % var3 == 0 or var3 % var1 == 0:
        print(var3)
        
    
