s1=input('Inserisci una stringa non vuota:')
s2=input('Inserisci una stringa non vuota:')
i=0
risultato=''
for i in range (len(s1)):
    for j in range(len(s2)):
        if s1[i]!=s2[j]:
            break
        else:
            i+=1
            risultato+=s2[j]
print(risultato)
i+=1
