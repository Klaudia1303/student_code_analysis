s1 = input('Inserisci una stringa: ')
s2 = input('Inserisci una stringa: ')
s3 = ''

for c in range(len(s1)):
    if s1[c] not in s2:
        s3 = s3+s1[c]
print(s3)
