var1 = input('Inserisci una stringa: ')
var1 = str(var1)
var2 = 0
var2 = int(var2)

for a in range(len(var1)):
    if var1[a] == var1[len(var1)-a-1]:
        var2 += 1
    else:
        break
    
print('Il livello di palindromicità:',var2)
        

