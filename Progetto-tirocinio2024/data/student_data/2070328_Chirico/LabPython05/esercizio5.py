s = input('stringa con caratteri ripetuti = ')
n = int(input('distanza tra due caratteri = '))
risultato = False

for i in range(len(s)-n):
    if s[i] == s[i+n]:
        risultato = True

print(risultato)
    
    
