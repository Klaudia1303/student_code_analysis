s = input('Inserisci una stringa: ')
n = int(input('Inserisci un intero positivo: '))
c = False
for i in range(len(s)-n):
    if s[i] == s[i+n]:
          c = True
print(c)
            
