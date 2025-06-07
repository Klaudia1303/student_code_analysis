s1 = input('inserisci una stringa: ')
s2 = input('inserisci una seconda stringa: ')
s3 = ''
for i in range(len(s1)):
    s3 = s3 + s1[i] + s2[i]
print(s3)
