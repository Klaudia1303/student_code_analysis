var1 = input('Inserisci un numero intero: ')
var1 = int(var1)
var2 = input('Inserisci un numero intero: ')
var2 = int(var2)
var3 = 1
var4 = False

while not var4:
    var3 += 1
    if var1 % var3 == 0 and var2 % var3 != 0:
        print(var3)
    elif var3 > var1:
        var4 = True
    else:
        var3 += 1


