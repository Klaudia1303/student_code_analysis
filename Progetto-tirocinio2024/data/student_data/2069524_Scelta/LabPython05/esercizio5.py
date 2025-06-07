s=str(input('Inserisci una stringa con almeno 2 caratteri:'))
n=int(input('Inserisci un numero intero n>0:'))
corretto=False
i=0
while i<len(s)-n:
    if s[i]==s[i+n]:
        corretto=True
    i+=1
print(corretto)
