var1 = input('Inserisci una stringa di testo: ')
var1 = str(var1)
var2 = input('Inserisci un numero intero: ')
var2 = int(var2)
var3 = 0

while 0 < len(var1):
    print(var1[var3]*var2, end='')
    var3 += 1
    if var3 == len(var1):
        break

