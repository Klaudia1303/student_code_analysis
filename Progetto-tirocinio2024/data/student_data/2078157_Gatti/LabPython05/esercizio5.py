s = input('inserisci una stringa con almeno due caratteri: ')
n = int(input('inserisci un intero positivo: '))
a = 0
for i in range(len(s) - n):
    if s[i] == s[i + n]:
        print(True)
        a = 1
        break
if a == 0:
    print(False)

