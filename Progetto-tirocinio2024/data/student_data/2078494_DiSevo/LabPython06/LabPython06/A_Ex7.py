s1 = input('Inserisci una prima stringa: ')
s2 = input('Inserisci una seconda stringa: ')

lenmax = 0
smax = ''
for i in range(len(s1)):
    for j in range(i+1, len(s1)+1):
        s = s1[i:j]
        if s in s2:
            l = j - i
            if l >= lenmax:
                lenmax = l
                smax = s
        else:
            break
print(smax)
