s = input('Inserisci una stringa di almeno due caratteri: ')
n = int(input('Inserisci un numero intero positivo: '))
k = False
for i in range(0,len(s)):
    if n+i<len(s):
        if s[i] == s[n+i]:
            k = True
print(k)
