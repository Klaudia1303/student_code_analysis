s = input ('Inserisci una stringa: ')
n = int (input ('Inserisci un numero intero: '))
for i in range(len(s)-2):
    if s[i]==s[i+n]:
        val=True
        break
    else :
        val = False
print (val)
