s = input('Inserisci una stringa: ')

l = 0
for i in range(len(s)//2):
    if (s[i] != s[len(s) - 1 - i]):
        break
    l += 1
print(l)
