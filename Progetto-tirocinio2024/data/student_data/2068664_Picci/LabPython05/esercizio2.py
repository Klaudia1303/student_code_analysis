s=input('inserisci stringa:')
n=int(input('inserisci intero positivo:'))
if n>0:
    risultato=''
    for i in range(len(s)):
        risultato+=s[i]*n
print(risultato)
    
