s1 = input('Inserisci una stringa: ')
s2 = input('Inserisci una stringa: ')
n = int(input('Inserisci un intero: '))
s = ''
for i in range(len(s1)):
        k = i-n
        j = i+n+1
        if k < 0:
            k = 0
        if j > len(s1):
            j = len(s1)
        if s1[i] in s2[k:j]:
            s = s + s1[i]
print(s)
