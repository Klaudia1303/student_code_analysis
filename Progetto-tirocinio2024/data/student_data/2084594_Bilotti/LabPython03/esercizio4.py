var1 = input('Inserisci il primo numero intero: ')
var1 = int(var1)
var2 = input('Inserisci il secondo numero intero: ')
var2 = int(var2)

for i in range(10):
    print(i)
    if i == var1:
        break
    print(i+1)
    if i == var2:
        break
    print(i+1)
    
