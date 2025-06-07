s=str(input('Inserisci stringa '))
n=int(input('Inserisci intero '))
precedente=''
for i in range(len(s)):
    x=s[i]
    y=x*n
    stringa=precedente+y
    precedente=stringa
print(stringa)
