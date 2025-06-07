s=input('Inserire una stringa di almeno due caratteri: ')
n=int(input('Inserire un intero: '))
risultato=False
for i in range(0,len(s)-n):
    if s[i:i+1]==s[i+n:i+1+n]:
        risultato=True
        break
print(risultato)
