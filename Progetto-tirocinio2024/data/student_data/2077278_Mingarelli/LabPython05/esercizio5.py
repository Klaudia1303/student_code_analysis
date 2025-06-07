a=False
s=input('inserisci una stringa ')
n=int(input('inserisci un numero intero positivo '))
for i in range(len(s)-n):
        if s[i]==s[i+n]:
            a=True
            
print(a)
