s = input('Inserisci stringa contenente almeno 2 caratteri: ')
n = int(input('Inserisci intero positivo: '))
same_char = False

for i in range(len(s)-n):
    if s[i] == s[i+n]:
        same_char = True
print(same_char)
