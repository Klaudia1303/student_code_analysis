s=''
while len(s)<2:
    s=input('inserisci una stringa di almeno due caratteri: ')
n=0
while n<=0:
    n=int(input('inserisci un intero positivo: '))
controllo=False
for i in range (len(s)-n):
    if s[i]==s[i+n]:
        controllo=True
        break
print (controllo)
