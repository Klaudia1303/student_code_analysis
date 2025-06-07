s=input('Inserisci una stringa ')
n=int(input('Inserisci il numero di ripetizioni delle lettere '))
for i in range(len(s)):
    print(s[i]*n, end='')
