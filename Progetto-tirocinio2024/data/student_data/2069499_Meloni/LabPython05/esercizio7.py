s=input('Inserisci una stringa di almeno 2 caratteri ')
x=False
for i in range(len(s)):
    if (s.count(s[i])>=2):
        x=True
print(x)
