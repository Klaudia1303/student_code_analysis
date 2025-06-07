s=input('inserisci una stringa di almeno 2 caratteri: ')
n=int(input('inserisci un intero positivo: '))
b=False
for a in range(len(s)-n):
    if s[a]==s[a+n]:
        b=True
        break
print(b)