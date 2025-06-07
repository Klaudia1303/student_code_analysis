s=input('inserisci una stringa ')
n='*'
while s[0]!=n[len(n)-1]:
    n=s
    s=input('inserisci una stringa ')
print(n,s)
