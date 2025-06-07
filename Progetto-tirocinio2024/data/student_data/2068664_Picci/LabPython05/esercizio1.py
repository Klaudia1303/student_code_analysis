s1=input('inserisci stringa:')
s2=input('inserisci stringa:')
if len(s1)==len(s2):
    risultato=''
    for i in range(len(s1)):
        risultato += s1[i]
        risultato += s2[i]
    print(risultato)
