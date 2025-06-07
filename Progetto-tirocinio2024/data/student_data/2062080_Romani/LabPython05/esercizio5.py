s=input('Inserire stringa di almeno due caratteri: ')
corretto=False
n=int(input('Inserire numero positivo: '))

for i in range(len(s)-n):
    if s[i]==s[i+n]:
        corretto=True
print(corretto)

