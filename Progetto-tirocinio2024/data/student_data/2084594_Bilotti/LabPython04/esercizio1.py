a = False
e = 0

while not a:
    i = input('Inserisci una stringa: ')
    var1 = i.count('a')
    var2 = i.count('c')
    e += 1
    if var1 and var2 == True:
         print('Hai inserito:',e,'stringhe')
         a = True
