s = input('Inserisci una stringa: ')
n = int(input('Inserisci un intero positivo: '))

for i in range(len(s)):
    print(s[i]*n, sep='', end='')
