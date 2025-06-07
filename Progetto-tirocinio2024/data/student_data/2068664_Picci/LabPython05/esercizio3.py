s1=input('inserisci stringa:')
s2=input('inserisci stringa:')
risultato=''
for i in range(len(s1)):
    if s1[i] not in s2:
        risultato+=s1[i]
print(risultato)
